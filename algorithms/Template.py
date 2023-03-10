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
|
|
|
"""

class Template:
	def __init__(self,Faction):
		"""
		This should not need to be modified.
		"""
		self.faction = Faction
		self.grid = [[]]

	def get_move(self, new_units):
		"""
		Modify this function and make any additional functions/variables/imports/etc
		as required.
		"""
		return self.grid


if __name__ == '__main__':
	# Algo Testing
	test = Template()
