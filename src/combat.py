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
| Max Marshall    | 2023-01-02 | Created File, finished basic combat system
| Max Marshall    | 2023-01-02 | Added documentation
| Max Marshall    | 2023-01-05 | Fixed for Cell = None
|
"""


def combat(location,grids,combat_grid):
	"""
	Determines the outcome of a contested cell

	Inputs:
		- location -> [x,y] indices of 2D array
		- grids -> 2D arrays of cells proposed by players
		- combat_grid -> 2D array of bools (from in_combat())
	
	Outputs:
		- Cell (with faction and unit of winner)
	"""
	x, y = location
	scores = {}
	for grid in grids:
		if grid[x][y] is not None:
			scores[grid[y][x]] = 0
	for cell in scores:
		adj_units = get_adj(location, cell.faction, grids, combat_grid)
		for unit in adj_units:
			scores[cell] += cell.unit.fight(type(unit))
	winning_cell = None
	lowest_score = 1000
	for cell in scores:
		if scores[cell] < lowest_score:
			winning_cell = cell
			lowest_score = scores[cell]
	return winning_cell


def get_adj(location, faction, grids, combat_grid):
	"""
	Gets all adjacent opponents to combat square

	Inputs:
		- location -> [x,y]
		- faction -> Faction of combatant to find opponents to
		- grids -> Proposed moves for each faction
		- combat_grid -> 2D array of boolean values (from call to in_combat())

	Outputs:
		- List of Units
	"""
	units = []
	x,y = location
	x_min = max(x-1,0)
	x_max = min(x+2,len(grids[0][0]))
	y_min = max(y-1,0)
	y_max = min(y+2,len(grids[0]))
	for i in range(x_min,x_max):
		for j in range(y_min,y_max):
			for grid in grids:
				if i == x and j == y: # Center of Battle
					if grid[j][i].faction != faction:
						units.append(grid[j][i].unit)
				else:
					if combat_grid[j][i] is False:
						if grid[j][i] is not None:
							if grid[j][i].hasUnit():
								if grid[j][i].faction is not faction:
									units.append(grid[j][i].unit)
	return units


def in_combat(proposed_maps,bounds):
	"""
	Finds all contested cells

	Inputs:
		- proposed_maps -> List of (2D arrays of Cells) submitted by players
		- bounds -> [[x_min,x_max],[y_min,y_max]]
	
	Outputs:
		- 2D array of bools (True = contested, else False)
	"""
	x_bounds, y_bounds = bounds
	combat_grid = [[False for _ in range(x_bounds[0],x_bounds[1])] for _ in range(y_bounds[0],y_bounds[1])]
	for x in range(x_bounds[0],x_bounds[1]):
		for y in range(y_bounds[0],y_bounds[1]):
			count = 0
			for prop_map in proposed_maps:
				if prop_map[y][x] is None:
					continue
				if prop_map[y][x].unit is not None:
					count += 1
			if count > 1:
				combat_grid[y][x] = True
	return combat_grid


if __name__ == '__main__':
	from Unit import Shieldbearer,Knight,Spearman
	from Cell import Cell
	from Faction import Faction
	# A little proof of concept
	# 2 Factions, 2 contested Cells, several allies/opponents
	factions = [Faction(1),Faction(2)]
	x = 4
	y = 4
	grid = [
		[Cell(),Cell(),Cell(),Cell()],
		[Cell(),Cell(),Cell(),Cell()],
		[Cell(),Cell(),Cell(),Cell()],
		[Cell(),Cell(),Cell(),Cell()]
	]
	state_1 = [
		[Cell(),Cell(),Cell(),Cell()],
		[Cell(),Cell(),Cell(factions[0],Knight()),Cell()],
		[Cell(factions[0],Shieldbearer()),Cell(factions[0],Shieldbearer()),Cell(),Cell()],
		[Cell(),Cell(factions[0],Shieldbearer()),Cell(),Cell()]
	]
	state_2 = [
		[Cell(),Cell(),Cell(),Cell()],
		[Cell(),Cell(),Cell(factions[1],Spearman()),Cell()],
		[Cell(),Cell(factions[1],Spearman()),Cell(factions[1],Spearman()),Cell()],
		[Cell(),Cell(),Cell(),Cell()]
	]
	combat_map = in_combat([state_1,state_2],[[0,x],[0,y]])
	#print(combat_map)
	print("\033[0m",end="")
	print("#"*(x+2))
	for j in range(y):
		for i in range(x):
			if combat_map[j][i] == True:
				grid[j][i] = combat([i,j],[state_1,state_2],combat_map)
			else:
				for state in [state_1,state_2]:
					if state[j][i].faction.color != 0:
						grid[j][i] = state[j][i]
	for row in grid:
		print("#",end="")
		for column in row:
			print(column,end="")
		print("#")
	print("#"*(x+2))
