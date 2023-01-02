from Cell import Cell
from Faction import Faction

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
  print("Please enter your initialization type (random / custom / seed / empty)")
  initType = str(input())

  # Initializing board, other variables
  board = initializeBoard(rows, cols, numFactions, initType)
  factions = [Faction(x + 1) for x in range(numFactions)]

  # Main loop
  # while (True):
  #   board = tick(board, rows, cols, numFactions)
  
def tick(board, rows, cols, numFactions):
  newBoard = initializeEmpty(rows, cols)
  for i in range(rows):
    for j in range(cols):
      newBoard[i][j] = nextState(board, i, j)
  return newBoard

def nextState(board, i, j):
  info = getInfo(board, i, j)
  return Cell(Faction(0))

def getInfo(board, i, j):
  return 0

def initializeBoard(rows, cols, numFactions, type):
  if type == 'random':
    return initializeRandom(rows, cols, numFactions)
  elif type == 'custom':
    return
  elif type == 'seed':
    return
  elif type == 'empty':
    return initializeEmpty(rows, cols)
  else:
    return initializeEmpty(rows, cols)

def initializeEmpty(rows, cols):
  return [[Cell(Faction(0)) for _ in range(rows)] for _ in range(cols)]

def initializeRandom(rows, cols, numFactions):
  return [[]]

def retrieveIntInput(default):
  userInput = input()
  if (userInput == '' or not userInput.isdigit()):
    return default
  return int(userInput)

if __name__ == '__main__':
  main()
