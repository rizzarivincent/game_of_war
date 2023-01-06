"""
	Copyright (C) 2023  Vincent Rizzari and Max Marshall   

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see https://www.gnu.org/licenses/.
________________
|_File_History_|________________________________________________________________
|_Programmer______|_Date_______|_Comments_______________________________________
| Max Marshall    | 2023-01-05 | Created File
| Max Marshall    | 2023-01-06 | Fixed logic in validate/get_cells()
|
|
"""
from combat import combat, in_combat

def validate(new_grid, faction, old_grid, new_units=[]):
	"""
	Decides whether a controller-submitted-grid is valid or not

	Inputs:
		- new_grid -> the controller's submitted grid
		- faction -> the Faction of the controller
		- old_grid -> the previous grid

	Outputs:
		- valid -> Boolean if valid or not
		- valid_grid -> the grid modified to be read by combine_grids()
		- reason -> string explaining what was invalid
	"""
	# Other land removal
	total_units = 0
	old_total_units = 0
	for j in range(len(new_grid)):
		for i in range(len(new_grid[0])):
			cell = new_grid[j][i].copy()
			if cell.faction is not faction:
				new_grid[j][i] = None
			else:
				if old_grid[j][i].faction is not faction:
					if cell.unit is None:
						return False, new_grid, "Took land that did not belong to you:\
							 ({},{})".format(i,j)
					if cell.unit in new_units:
						return False, new_grid, "Placed a unit in a cell which did not belong to you: ({},{})".format(i,j)
				# Unit checks
				if cell.unit is not None:
					if not find_unit(cell.unit, old_grid, i, j, new_units):
						return False, new_grid, "Unit unaccounted for:\n\
							Location: ({},{})\nType: {}\n\
								Hash: {}".format(i,j,type(cell.unit,cell.unit.hash))
			if old_grid[j][i].faction == faction and old_grid[j][i].unit is not None:
				old_total_units += 1

	# Check totals
	if total_units > old_total_units + len(new_units):
		return False, new_grid, "Added additional units:\nPrevious: {} Units\nAdded: {} Units\nSubmitted: {} Units"\
				.format(old_total_units, len(new_units), total_units)

	return True, new_grid, "Success"


def combine_boards(board_list, prev_board):
	"""
	Combines together the assorted player moves into a new board

	Inputs:
		- board_list -> List of new boards
		- prev_board -> previous (current accepted) board

	Outputs:
		- new_board -> 2d list of cells
	"""
	board = [[None for _ in prev_board[0]] for _ in prev_board]
	battle_map = in_combat(board_list,\
		[[0,len(prev_board[0])],[0,len(prev_board)]])

	for j in range(len(prev_board)):
		for i in range(len(prev_board[0])):
			if battle_map[j][i]:
				board[j][i] = combat([i,j],board_list,battle_map)
			else:
				unit_cells, cells = get_cells(board_list,i,j)
				if len(unit_cells) != 0:
					board[j][i] = unit_cells[0].copy()
					continue
				assert len(cells)<=1, "Cell claimed by multiple combatants without combat"
				if len(cells) > 0:
					board[j][i] = cells[0].copy()
	return board


def get_cells(boards, i, j):
	"""
	Gets all cells at indices in boards

	Inputs:
		- boards -> list of 2d arrays of Cells
		- i, j -> indices to desired cell
	
	Outputs:
		- list of Cell objects
	"""
	unit_cells = []
	cells = []
	for board in boards:
		if board[j][i] is not None:
			if board[j][i].hasUnit():
				unit_cells.append(board[j][i])
			cells.append(board[j][i])
	return unit_cells, cells

def find_unit(unit, grid, i, j, new_units):
	"""
	Checks whether a unit has violated its movement contract

	Inputs:
		- unit -> the unit in question
		- grid -> the previous grid to check against
		- i,j -> the location of the unit in the grid
		- new_units -> the list of units allowed to add this turn
	"""
	for new_unit in new_units:
		if new_unit.hash == unit.hash:
			return True
	for x in range(max(i-unit.movement,0),min(i+unit.movement+1,len(grid[0]))):
		for y in range(max(j-unit.movement,0),min(j+unit.movement+1,len(grid))):
			if grid[y][x] is not None:
				if grid[y][x].hasUnit():
					if grid[y][x].unit.hash is unit.hash:
						return True
	return False


def check_win(board, conditions):
	"""
	Checks for win coditions

	Inputs:
		- board -> the current game state
		- conditions -> a list of functions checking if won or not

	Ouput:
		- whether the game has completed (boolean)
		- winner (Faction)
	"""
	winning_faction = None
	for condition in conditions:
		win, faction = condition.check_win(board)
		if not win:
			return False, None
		if winning_faction is not None and faction is not winning_faction:
			return False, None
		winning_faction = faction
	return True, winning_faction


if __name__ == '__main__':
	pass
