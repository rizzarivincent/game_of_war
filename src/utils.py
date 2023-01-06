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
import os.path as path

def find_algo(name):
	algo_loc = path.join("..","algorithms")
	return path.exists(path.join(algo_loc,"{}.py".format(name)))

def print_winner(x,y,faction):
	"""
	TODO: Make this way cooler, like a screen wipe
	"""
	faction.print("{} WINS".format(faction.name))


if __name__ == '__main__':
	pass
