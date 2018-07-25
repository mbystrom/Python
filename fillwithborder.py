import random as r
import matrix
import time
import os

N = 1
S = 2
E = 4
W = 8
 
DX = { 
  N: 0,
  S: 0,
  E: -1,
  W: 1
}

DY = {
  N: -1,
  S: 1,
  E: 0,
  W: 0
}


width = 80
height = 30
grid = matrix.generate_matrix(width, height, 0)


def isInBounds (x,y):
  if x < 0 or x >= width: return False
  if y < 0 or y >= height: return False
  return True


def FillFrom (queue, value, region):
  index = len(queue) - 1

  point = queue[index]
  directions = [N, S, E, W]
  r.shuffle(directions)

  grid[point['y']][point['x']] = value

  for direction in directions:
    newX = point['x'] + DX[direction]
    newY = point['y'] + DY[direction]
    
    if isInBounds(newX, newY):

      if grid[newY][newX] != 0: continue

      grid[newY][newX] = value
      queue.append({'x': newX, 'y': newY})

      if region == 1:
        region1.append({ 'x': newX, 'y': newY })
      elif region == 2:
        region2.append({ 'x': newX, 'y': newY })
  queue.pop(index)
  return queue


def TilesLeft ():
  for y in range(height):
    for x in range(width):
      if grid[y][x] == 0:
        return True
  return False

def GetEdgeTiles (primary, secondary):
  edgeTiles = []

  directions = [N, S, E, W]
  for tile in primary:
    for direction in directions:
      adjacent = {
        'x': tile['x'] + DX[direction],
        'y': tile['y'] + DY[direction]
      }
      if adjacent in secondary:
        edgeTiles.append(tile)
  return edgeTiles

def FillEdges (tiles):
  for tile in tiles:
    grid[tile['y']][tile['x']] = '#'


fill1Queue = [ {'x': r.randint(0,width-1), 'y': r.randint(0,height-1)} ]
fill2Queue = [ {'x': r.randint(0,width-1), 'y': r.randint(0,height-1)} ]
region1 = []
region2 = []

loops = 0

while TilesLeft():
  while len(fill1Queue) > 0 or len(fill2Queue) > 0:

    if (len(fill1Queue) > 0):
      fill1Queue = FillFrom(fill1Queue, "*", 1)
    if (len(fill2Queue) > 0):
      fill2Queue = FillFrom(fill2Queue, ".", 2)
    
    loops += 1
  

matrix.print_matrix(grid)
print("took", loops, "loops to finish")

reg1edge = GetEdgeTiles(primary=region1, secondary=region2)
reg2edge = GetEdgeTiles(primary=region2, secondary=region1)
print(reg1edge)
print(reg2edge)
FillEdges(reg2edge)
matrix.print_matrix(grid)
