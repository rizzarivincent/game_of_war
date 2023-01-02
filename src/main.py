import Cell
import Faction

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
  print("Please enter your initialization type (random / custom / seed)")
  initType = str(input())

  # Initializing board, other variables
  board = initializeBoard(rows, cols, numFactions, initType)

  # Main loop
  while (True):
    board = tick(board, rows, cols, numFactions)
  
def tick(board, rows, cols, numFactions):
  newBoard = initializeEmpty(rows, cols)
  for i in range(rows):
    for j in range(cols):
      newBoard[i][j] = nextState(board, i, j)

def nextState(board, i, j):
  info = getInfo(board, i, j)
  return Cell()

def getInfo(board, i, j):
  return 0

def initializeBoard(rows, cols, numFactions, type):
  if type == 'random':
    return initializeRandom(cols, rows, numFactions)
  elif type == 'custom':
    return
  elif type == 'seed':
    return
  elif type == 'empty':
    return initializeEmpty(cols, rows)

def initializeEmpty(rows, cols):
  return [[Cell() for _ in range(rows)] for _ in range(cols)]

def initializeRandom(rows, cols, numFactions):
  return [[]]

def retrieveIntInput(default):
  input = input()
  if (input == '' or not input.isdigit()):
    return default
  return int(input)

if __name__ == '__main__':
  main()
