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
| Max Marshall    | 2023-01-01 | Created File
| Max Marshall    | 2023-01-02 | Modified class, added documentation,
|                 |            | added test/example in guard
|
|
"""
from Faction import Faction, Factionless, Terrain
from Unit import Shieldbearer, Knight, Spearman, Capital, City
import random


class Cell:
	def __init__(self, faction=Factionless(), unit=None):
		"""
		Creates a Cell, holds Faction and Unit Data

		Inputs:
			- faction -> Faction (deafult Factionless)
			- unit -> Unit (default None)
		"""
		self.faction = faction
		self.unit = unit

	def __str__(self):
		string = "\033[0m"
		string += "\033[{}m".format(self.faction.color+40+(self.faction.bold*60))
		if self.unit is not None:
			string += "\033[1;{0}m{1}".format(37,self.unit)
		else:
			string += " "
		string += "\033[0m"
		return string

	def __repr__(self):
		return str(self)

	def hasUnit(self):
		return self.unit is not None


if __name__ == '__main__':
	x = 80
	y = 22
	factions = [Faction(x) for x in range(1,13)]
	factions.append(Factionless())
	factions.append(Terrain())
	grid = [[Cell(random.choice(factions)) for _ in range(x)] for _ in range(y)]
	for _ in range(20):
		row = random.choice(grid)
		cell = random.choice(row)
		cell.unit = random.choice([Shieldbearer,Knight,Spearman,Capital,City])()
	for row in grid:
		for column in row:
			print(column,end="")
		print()
