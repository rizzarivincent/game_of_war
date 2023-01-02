#!/bin/bash
################################################################################
# setup
################################################################################
#	Copyright (C) 2023  Vincent Rizzari and Max Marshall   
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see https://www.gnu.org/licenses/.
#________________
#|_File_History_|_______________________________________________________________
#|_Programmer______|_Date_______|_Comments______________________________________
#| Max Marshall    | 2023-01-02 | Created File
#|
#|
#|

source .venv/bin/activate

# Get file directory
FILE_LOC="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

python3 $FILE_LOC/../src/main.py

deactivate
