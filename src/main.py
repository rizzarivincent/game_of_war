from Cell import Cell
from Faction import Faction
import random

def main():
  # Reading in user input
  print("Welcome to the Game of War!")
  # Read number of rows
  print("Please enter the height of your game board (Default: 30):")
  rows = retrieveIntInput(30)
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
  factions = [Faction(x) for x in range(numFactions + 1)]
  board = initializeBoard(rows, cols, factions, initType)

  print(rows)
  print(cols)
  print(numFactions)
  print(initType)

  printBoard(board=board)

  # Main loop
  while (True):
    printBoard(board)
    board = tick(board, rows, cols, factions)
  
def tick(board, rows, cols, factions):
  newBoard = [[nextState(board, i, j) for j in range(cols)] for i in range(rows)]
  return newBoard

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
