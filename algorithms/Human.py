"""
	Copyright (C) 2023  Max Marshall   

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
| Max Marshall    | 2023-01-06 | Fleshed out most of UI
| Max Marshall    | 2023-01-06 | Bug fixes for Add/Move/PrintScreen
|
"""
import os
from utils import yesno


class Human:
	def __init__(self, faction):
		self.faction = faction
		self.grid = [[]]
		self.debug = False

	def get_move(self, units):
		existing = []
		new_grid = []
		for y in range(len(self.grid)):
			new_row = []
			for x in range(len(self.grid[0])):
				if self.grid[y][x].faction == self.faction:
					if self.grid[y][x].unit is not None:
						if self.grid[y][x].unit.movement > 0:
							existing.append([x,y])
				new_row.append(self.grid[y][x])
				if self.grid[y][x].unit is not None:
					print(self.grid[y][x].unit)
			new_grid.append(new_row)
		done = False
		while not done:
			for i in range(len(existing)):
				new_grid = self.move(existing[i], new_grid)
			self.print_location(new_grid,-1,-1,"")
			print("\n\n")
			done = yesno("All Units Moved. Continue? (Y/n): ")
		done = False
		while not done:
			for i in range(len(units)):
				new_grid = self.add(units, i, new_grid)
			self.print_location(new_grid,-1,-1,"")
			print("\n\n")
			done = yesno("All Units Added. Continue? (Y/n): ")
		return new_grid

	def move(self, location, grid):
		x_directions = {
			"q":-1, "w": 0, "e": 1,
			"a":-1, "s": 0, "d": 1,
			"z":-1, "x": 0, "c": 1
		}
		y_directions = {
			"q":-1, "w":-1, "e":-1,
			"a": 0, "s": 0, "d": 0,
			"z": 1, "x": 1, "c": 1
		}
		self.print_location(grid, location[0], location[1], \
			"Move {}".format(self.grid[location[1]][location[0]].unit))
		direction = ""
		print()
		print()
		print()
		while not direction in x_directions:
			print("\033[1A",end="")
			direction = input().lower()
		dest = [location[0]+x_directions[direction],\
						location[1]+y_directions[direction]]
		if dest[0] != location[0] or dest[1] != location[1]: 
			grid[dest[1]][dest[0]] = self.grid[location[1]][location[0]].copy()
			grid[location[1]][location[0]].unit = None
		return grid

	def add(self, units, i, grid):
		loc = [0,0]
		x_directions = {
			"q":-1, "w": 0, "e": 1,
			"a":-1, "s": 0, "d": 1,
			"z":-1, "x": 0, "c": 1,
			"Q":-10, "W": 0, "E": 10,
			"A":-10, "S": 0, "D": 10,
			"Z":-10, "X": 0, "C": 10
		}
		y_directions = {
			"q":-1, "w":-1, "e":-1,
			"a": 0, "s": 0, "d": 0,
			"z": 1, "x": 1, "c": 1,
			"Q":-10, "W":-10, "E":-10,
			"A": 0, "S": 0, "D": 0,
			"Z": 10, "X": 10, "C": 10
		}
		done = False
		while not done:
			self.print_location(grid, loc[0], loc[1], "Add Unit")
			print(units)
			print(" "*(3*i+1)+"^")
			direction = ""
			print()
			while not direction in x_directions:
				print("\033[1A",end="")
				direction = input()
			loc = [loc[0]+x_directions[direction],
						loc[1]+y_directions[direction]]
			loc[0] = max(0,min(len(grid[0])-1,loc[0]))
			loc[1] = max(0,min(len(grid)-1,loc[1]))
			if direction == "s":
				done = True
		grid[loc[1]][loc[0]].faction = self.faction
		grid[loc[1]][loc[0]].unit = units[i]
		return grid

	def print_location(self, grid, x ,y, action):
		length, width = os.get_terminal_size()
		if length < len(grid) + 5 or width < len(grid[0]):
			print("\033[8;{};{}t".format(len(grid)+5,len(grid[0])))
			offset = 5
			length = len(grid) + 5
		else:
			offset = length - len(grid) - 5
		# Wipe
		print("\033[H",end="")
		#print("\033[{}B".format(offset),end="")
		for _ in range(length):
			print("\033[K")
		print("\033[H",end="")
		print("\033[{}B".format(offset),end="")
		self.faction.print("{} -> {}".format(self.faction.name,action))
		# Print Screen with Underlined cursor
		for j in range(len(grid)):
			for i in range(len(grid[0])):
				if i == x and j == y:
					print("\033[4m",end="")
				print(grid[j][i],end="")
			print()

	def report_failure(self, string):
		print(string)


if __name__ == '__main__':
	test = Human()
