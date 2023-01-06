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
| Max Marshall    | 2023-01-05 | Added find, check and load,print_victory()
|
|
"""
import os.path as path
import sys
sys.path.append(path.join("..","conditions"))
sys.path.append(path.join("..","on_update"))
sys.path.append("..")


def yesno(string):
	no = ["n","no"]
	value = input(string)
	if value.lower() in no:
		return False
	return True


def find_algo(name):
	algo_loc = path.join("..","algorithms")
	return path.exists(path.join(algo_loc,"{}.py".format(name)))


def print_victory(x,y,faction):
	"""
	TODO: Make this way cooler, like a screen wipe
	"""
	faction.print("{} WINS".format(faction.name))


def check_condition(name):
	return path.exists(path.join(path.join("..","conditions"),"{}.py".format(name)))


def load_condition(name):
	module = __import__("conditions.{}".format(name))
	script = getattr(module,name)
	return script


def check_event(name):
	return path.exists(path.join(path.join("..","on_update"),"{}.py".format(name)))


def load_event(name):
	module = __import__("on_update.{}".format(name))
	script = getattr(module,name)
	return script



if __name__ == '__main__':
	pass
