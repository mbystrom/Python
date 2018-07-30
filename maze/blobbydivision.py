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


width = 30
height = 10
grid = matrix.generate_matrix(width, height, 0)

start = time.time()

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
      
      tile = {'x': newX, 'y': newY}

      grid[newY][newX] = value
      queue.append(tile)

      if region == 1:
        region1.append({ 'x': newX, 'y': newY })
      elif region == 2:
        region2.append({ 'x': newX, 'y': newY })
  queue.pop(index)
  return queue


def GetTiles ():
  tiles = []
  for y in range(height):
    for x in range(width):
      if grid[y][x] == 0:
        tiles.append({'x': x, 'y': y})
  return tiles

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
    grid[tile['y']][tile['x']] = '-'

def TilesLeftInRegion (region):
  left = 0
  for i in region:
    if grid[i['y']][i['x']] == 0:
      left += 1
  return left

def ResetMap ():
  for y in range(height):
    for x in range(width):
      if grid[y][x] != '-':
        grid[y][x] = 0

regions = []
regions.append(GetTiles())

loops = 0

while len(regions) > 0:
  activeRegion = 0
  while TilesLeftInRegion(regions[activeRegion]) > 4:
    fill1Queue = [ {'x': r.randint(0,width-1), 'y': r.randint(0,height-1)} ]
    fill2Queue = [ {'x': r.randint(0,width-1), 'y': r.randint(0,height-1)} ]
    region1 = []
    region2 = []
    while len(fill1Queue) > 0 or len(fill2Queue) > 0:

      if (len(fill1Queue) > 0):
        fill1Queue = FillFrom(fill1Queue, "*", 1)
      if (len(fill2Queue) > 0):
        fill2Queue = FillFrom(fill2Queue, ".", 2)
      
      loops += 1
      print(loops)
  reg1edge = GetEdgeTiles(region1, region2)
  FillEdges(reg1edge)
  if len(region1) > 4: regions.append(region1)
  if len(region2) > 4: regions.append(region2)
  regions.pop(0)
  ResetMap()
  # os.system('cls')
  matrix.print_matrix(grid)
  
for y in range(height):
  for x in range(width):
    if grid[y][x] == '-':
      grid[y][x] = '#'
    else:
      grid[y][x] = '.'

end = time.time()
elapsed = end - start

matrix.print_matrix(grid)
print("took", loops, "loops to finish")
print("that's", elapsed, "seconds!")

