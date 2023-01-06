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
| Vincent Rizzari | 2023-01-01 | Created File
| Max Marshall    | 2023-01-05 | Remade game loop, added algo selection
|
|
"""
import random
from Cell import Cell
from Faction import Faction
from Algorithm import Algorithm
from Unit import Knight, Shieldbearer, Spearman, Capital, City
import utils
import state


def main():
  # Reading in user input
  print("Welcome to the Game of War!")
  # Read number of rows
  print("Please enter the height of your game board (Default: 20):")
  rows = retrieveIntInput(20)
  # Read number of columns
  print("Please enter the width of your game board (Default: 40):")
  cols = retrieveIntInput(40)
  # Read number of factions
  print("Please enter the number of factions in your game (2 - 6) (Default: 2)")
  numFactions = retrieveIntInput(2)
  if (numFactions < 2):
    print("Too few factions")
    return
  if (numFactions > 6):
    print("Too many factions")
    return
  # Read initialization type
  print("Please enter your initialization type (random / blobs / custom / seed / empty) (Default: random)")
  initType = str(input())

  # Initializing board, other variables
  factions = [Faction(x+1) for x in range(numFactions)]
  board = initializeBoard(rows, cols, factions, initType)

  # Add in special events
  # TODO: Add support for events
  events = []
  updates = input("Enter Events, separated by commas: ")
  for update in updates.split(","):
    update = update.strip()
    if utils.check_event(update):
      events.append(utils.load_event(update))
      print("{} LOADED".format(update))

  # Add in win conditions
  # TODO: Add support for win conditions
  conditions = []
  conds = input("Enter Conditions, separated by commas: ")
  for cond in conds.split(","):
    cond = cond.strip()
    if utils.check_condition(cond):
      conditions.append(utils.load_condition(cond))
      print("{} LOADED".format(cond))

  if len(conditions) == 0:
    conditions = [utils.load_condition("Endless")]

  # Adding players
  controllers = []
  i=1
  for faction in factions:
    file = input("Enter Algorithm Name for Faction {} of {}: ".format(i,len(factions)))
    exists = utils.find_algo(file)
    while not exists:
      print("Algorithm not found. If Human Player, enter \"Human\". Try again.")
      file = input("Enter Algorithm Name for Faction {} of {}: ".format(i,len(factions)))
      exists = utils.find_algo(file)
    faction.name = input("Enter Faction Name: ")
    controller = Algorithm(faction,file)
    controllers.append(controller)
    i+=1

  print(rows)
  print(cols)
  print(numFactions)
  print(initType)

  turn = 0

  for i in range(len(conditions)):
    conditions[i] = conditions[i](controllers,board,[Knight,Shieldbearer,Spearman, City, Capital])
  for j in range(len(events)):
    events[j] = events[j](controllers,board,[Knight,Shieldbearer,Spearman, City, Capital])

  # Main loop
  while (True):
    # Event update
    for event in events:
      board = event.update(board, turn)
    printBoard(board)
    # Send board to players
    for controller in controllers:
      controller.push_grid(board)
    # Get updated boards
    new_boards = []
    for controller in controllers:
      units = [Knight(), Spearman()]
      validated = False
      time = 0
      while not validated:
        new_board, new_time = controller.get_move(units)
        time += new_time
        validated, valid_board, reason = state.validate(new_board, controller.faction, board, units)
        if not validated:
          print("FAILED")
          print(reason)
          input()
          controller.report_failure(reason)
          controller.push_grid(board)
      new_boards.append(valid_board)
      print("Board Added")
    # Recombine new boards
    board = state.combine_boards(new_boards,board)
    won, winner = state.check_win(board,conditions)
    turn += 1
    if won:
      break
  utils.print_victory(len(board[0]), len(board), winner)


def printBoard(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      print(board[i][j], end="")
    print()

def nextState(board, i, j):
  info = getInfo(board, i, j)
  return Cell(Faction(0))

def getInfo(board, i, j):
  return 0

def initializeBoard(rows, cols, factions, type):
  if type == 'random' or type == '':
    return initializeRandom(rows, cols, factions)
  elif type == 'blobs':
    return initializeBlobs(rows, cols, factions)
  elif type == 'custom':
    return initializeCustom(rows, cols, factions)
  elif type == 'seed':
    return initializeSeed(rows, cols, factions)
  elif type == 'empty':
    return initializeEmpty(rows, cols, factions)
  else:
    return initializeEmpty(rows, cols, factions)

def initializeEmpty(rows, cols, factions):
  return [[Cell(factions[0]) for _ in range(cols)] for _ in range(rows)]

def initializeRandom(rows, cols, factions):
  return [[Cell(random.choice(factions)) for _ in range(cols)] for _ in range(rows)]

def initializeBlobs(rows, cols, factions):
  # TODO: Implement this
  return initializeEmpty(rows, cols, factions)

def initializeCustom(rows, cols, factions):
  # TODO: Implement this
  return initializeEmpty(rows, cols, factions)

def initializeSeed(rows, cols, factions):
  # TODO: Implement this
  return initializeEmpty(rows, cols, factions)

def retrieveIntInput(default):
  userInput = input()
  if (userInput == '' or not userInput.isdigit()):
    return default
  return int(userInput)

if __name__ == '__main__':
  main()
