import random as r
import matrix
import time

N, S, E, W = 1, 2, 4, 8

DX = { N: 0, S: 0, E: 1, W: -1 }
DY = { N: -1, S: 1, E: 0, W: 0 }
Opposite = { N: S, S: N, E: W, W: E }

width = 100
height = 100

def isOut (x, y):
  if x < 0 or x >= width: return True
  if y < 0 or y >= height: return True
  return False

def walk (tile):
  directions = [N,S,E,W]
  r.shuffle(directions)

  for direction in directions:
    nx = tile['x'] + DX[direction]
    ny = tile['y'] + DY[direction]

    if isOut(nx, ny): continue
    
    if grid[ny][nx] == 0:
      grid[tile['y']][tile['x']] |= direction
      grid[ny][nx] |= Opposite[direction]
      return {'x': nx, 'y': ny}

def FindNext (search):
  for i in range(len(search)):
    tile = search[i]
    
    directions = [N,S,E,W]
    r.shuffle(directions)
    
    for direction in directions:
      nx = tile['x'] + DX[direction]
      ny = tile['y'] + DY[direction]

      if isOut(nx, ny): continue
      
      if grid[ny][nx] == 0:
        grid[tile['y']][tile['x']] |= direction
        grid[ny][nx] |= Opposite[direction]
        return {'x': nx, 'y': ny}
    search.pop(i)

def TilesRemaining ():
  tiles = 0
  for y in range(height):
    for x in range(width):
      if grid[y][x] == 0:
        tiles += 1
  return tiles


def PrintMaze():
  print("  ", end="")
  for i in range(width):
    print("__", end="")
  print("")
  for y in range(height):
    print(" |", end="")
    for x in range(width):
      if grid[y][x] & S != 0:
        print(" ", end="")
      else:
        print("_", end="")

      if grid[y][x] & E != 0:
        if (grid[y][x] | grid[y][x+1]) & S != 0:
          print(" ", end="")
        else:
          print("_", end="")
      else:
        print("|", end="")
    print("")

start = time.time()

grid = matrix.generate_matrix(width, height)

stack = [{'x': 0, 'y': 0}]
visited = []

while TilesRemaining() > 0:
  while len(stack) > 0:
    currentTile = stack.pop(-1)
    
    nextTile = walk(currentTile)
    visited.append(currentTile)
    
    if nextTile != None:
      stack.append(nextTile)

  stackAdd = FindNext(visited)
  if stackAdd != None:
    stack.append(stackAdd)

PrintMaze()
print(f"that took {time.time() - start} seconds to run!")