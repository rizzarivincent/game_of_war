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
| Max Marshall    | 2023-01-02 | Created File
|
|
|
"""
from Unit import Unit


def combat(location,grids,combat_grid):
	x, y = location
	scores = {}
	for grid in grids:
		scores[grid[y][x]] = 0
	for cell in scores:
		adj_units = get_adj(location, cell.faction, grids, combat_grid)
		for unit in adj_units:
			scores[cell] += cell.unit.score[type(unit)]
	winning_cell = None
	lowest_score = 1000
	for cell in scores:
		if scores[cell] < lowest_score:
			winning_cell = cell
			lowest_score = scores[cell]
	return winning_cell


def get_adj(location, faction, grids, combat_grid):
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
						if grid[j][i].unit is not None:
							if grid[j][i].faction is not faction:
								units.append(grid[j][i].unit)
	return units


def in_combat(proposed_maps,bounds):
	x_bounds, y_bounds = bounds
	combat_grid = [[False for _ in range(len(x_bounds))] for _ in range(len(y_bounds))]
	for x in range(x_bounds[0],x_bounds[1]):
		for y in range(y_bounds[0],y_bounds[1]):
			count = 0
			for prop_map in proposed_maps:
				if prop_map[y][x].unit is not None:
					count += 1
			if count > 1:
				combat_grid[y][x] = True
	return combat_grid


if __name__ == '__main__':
	pass
