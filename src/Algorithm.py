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
| Max Marshall    | 2023-01-02 | Created File, added module loading
| Max Marshall    | 2023-01-05 | Added get_move(), central to use
|
|
"""
import sys
sys.path.append("../algorithms/") 
# Add algorithms to path

import time

class Algorithm:
	def __init__(self, faction, filename):
		"""
		Facillitates the loading of Algorithms

		Inputs:
			- faction -> Faction
			- filename -> name of file in algorithms to load
			NOTE: filename must match class name in file
		"""
		self.faction = faction
		self.debug = True
		self.load_algo(filename)

	def load_algo(self, filename):
		"""
		Loads designated algo from algorithms file
		"""
		module = __import__(filename)
		self.algo = getattr(module,filename)(self.faction)

	def push_grid(self,grid):
		"""
		Pushes current grid to algo.
		"""
		self.algo.grid = [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]
		if self.debug:
			self.faction.print("PUSHED_GRID:")
			for y in range(len(self.algo.grid)):
				for x in range(len(self.algo.grid[0])):
					print(self.algo.grid[y][x],end="")
				print()

	def get_move(self,units=[]):
		"""
		Gets moves from the Algorithm
		"""
		start_time = time.time_ns()
		move = self.algo.get_move(units)
		stop_time = time.time_ns()
		return move, (stop_time-start_time)

	def print_failure(self,string):
		"""
		Passes on failure reason to algo
		"""
		try:
			self.algo.print_failure(string)
		except NameError:
			pass


if __name__ == '__main__':
	from Faction import Faction
	from Cell import Cell
	import random
	x=80
	y=22
	faction = Faction(1)
	factions = [faction,Faction(2),Faction(3)]
	grid = [[Cell(random.choice(factions)) for _ in range(x)] for _ in range(y)]
	test = Algorithm(faction,"Factionless")
	test.push_grid(grid)
	_, time = test.get_move()
	print(time)
