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
| Max Marshall    | 2023-01-02 | Created File, 3 Base Units
| Max Marshall    | 2023-01-02 | Added Capital, City
| Max Marshall    | 2023-01-05 | Added movement and hash values for validation
|
"""
import random

class Unit:
	def __init__(self, char):
		self.char = char
		self.score = {}
		self.movement = 1
		self.hash = random.getrandbits(16)

	def __str__(self):
		return self.char

	def __repr__(self):
		return self.char

	def fight(self,opponent):
		if opponent in self.score:
			return self.score[opponent]
		return 1

	def __eq__(self, object):
		return self.hash == object.hash


class Shieldbearer(Unit):
	def __init__(self):
		super().__init__("U")
		self.score[Shieldbearer] = 1
		self.score[Knight] = 2
		self.score[Spearman] = 0.5
		self.score[Capital] = 1
		self.score[City] = 1
		self.name = "Shieldbearer"

class Knight(Unit):
	def __init__(self):
		super().__init__("@")
		self.score[Shieldbearer] = 0.5
		self.score[Knight] = 1
		self.score[Spearman] = 2
		self.score[Capital] = 1
		self.score[City] = 1
		self.name = "Knight"

class Spearman(Unit):
	def __init__(self):
		super().__init__("/")
		self.score[Shieldbearer] = 2
		self.score[Knight] = 0.5
		self.score[Spearman] = 1
		self.score[Capital] = 1
		self.score[City] = 1
		self.name = "Spearman"

class Capital(Unit):
	def __init__(self):
		super().__init__("P")
		self.movement = 0
		self.score[Shieldbearer] = 0.334
		self.score[Knight] = 0.334
		self.score[Spearman] = 0.334
		self.score[Capital] = 0.334
		self.score[City] = 0.334
		self.name = "Capital"

class City(Unit):
	def __init__(self):
		super().__init__("h")
		self.movement = 0
		self.score[Shieldbearer] = 0.75
		self.score[Knight] = 0.75
		self.score[Spearman] = 0.75
		self.score[Capital] = 0.75
		self.score[City] = 0.75
		self.name = "Capital"


if __name__ == '__main__':
	test = Unit()
