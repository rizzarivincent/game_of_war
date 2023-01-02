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
| Max Marshall    | 2023-01-02 | Added name, __str__() rep, Factionless, Terrain
|
|
"""

class Faction:
	def __init__(self,color,name="team"):
		"""
		Creates a new Faction

		Inputs:
			- color -> int in [0,7]
			- name -> string

		Color Table:
			0 -> Black
			1 -> Red
			2 -> Green
			3 -> Yellow
			4 -> Blue
			5 -> Magenta
			6 -> Cyan
			7 -> White

			Black is reserved for factionless, and white is impassable terrain,
			leaving 6 remaining available for factions
		"""
		self.color = color%7
		self.bold = int(color/(6+1))
		self.color += self.bold
		self.name = name

	def __str__(self):
		return "\033[{0};{1}m{2}\033[0m".format(self.bold,self.color+30,self.name)

	def __repr__(self):
		return str(self)


class Factionless(Faction):
	def __init__(self):
		self.color = 0
		self.bold = 0
		self.name = "Factionless"


class Terrain(Faction):
	def __init__(self):
		self.color = 7
		self.bold = 1
		self.name = "Terrain"


if __name__ == '__main__':
	for i in range(12):
		print(Faction(i+1))
