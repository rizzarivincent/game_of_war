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
|
|
|
"""
from Faction import Faction
from Unit import Unit, Shieldbearer, Knight, Spearman
import random

class Cell:
	def __init__(self, faction, unit=None, capital=False):
		self.faction = faction
		self.unit = unit
		self.capital = capital

	def __str__(self):
		string = "\033[0m\033"
		if self.capital:
			string += "[{}m".format(self.faction.color+100)
		else:
			string += "[{}m".format(self.faction.color+40)
		if self.unit is not None:
			string += "\033[1;{0}m{1}".format(37,self.unit)
		else:
			string += " "
		string += "\033[0m"
		return string

	def __repr__(self):
		return str(self)




if __name__ == '__main__':
	x = 80
	y = 22
	factions = [Faction(1),Faction(2),Faction(0),Faction(3),Faction(4),Faction(5),Faction(6)]
	grid = [[Cell(random.choice(factions)) for _ in range(x)] for _ in range(y)]
	for _ in range(20):
		row = random.choice(grid)
		cell = random.choice(row)
		cell.unit = random.choice([Shieldbearer,Knight,Spearman])()
	for row in grid:
		for column in row:
			print(column,end="")
		print()
