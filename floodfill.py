# a flood fill algorithm using one or multiple seeds
# easy selection of one of four algorithms
# 1. traditional oldest-first (forest-fire)
# 2. newest first
# 3. random from queue
# 4. varied - random selection of the 3 above (on a per-loop basis)

import random as r
import matrix
import time
import os

# initializes directions
# actual values of N, S, E, and W unimportant
N = 1
S = 2
E = 4
W = 8

# initializes relative x and y values according to direction 
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

def isInBounds (x,y):
  # makes sure the point specified is in bounds
  # 99% sure this is O(1)
  if x < 0 or x >= width: return False
  if y < 0 or y >= height: return False
  return True

def SelectIndex (_max):
  # select different fill patterns
  # oldest is most common in flood fill
  # varied seems to create more organic shapes, especially on large areas
  
  oldest = 0
  newest = _max
  random = r.randint(0, _max)

  # varied has even chance of returning oldest, newest or random
  options = [oldest, newest, random]
  varied = r.choice(options)

  # change to return whichever fill pattern you prefer
  return random

def FillFrom (queue, value):
  # fills available points around first queue item with specified value
  # removes current point from the queue so it can't be called again
  # returns list of points

  # pass len(queue) - 1 because arrays count from 0 and lengths from 1
  index = SelectIndex(len(queue) - 1)

  point = queue[index]
  directions = [N, S, E, W]
  r.shuffle(directions)     # randomize directions to not favor N/W

  grid[point['y']][point['x']] = value

  for direction in directions:
    newX = point['x'] + DX[direction]
    newY = point['y'] + DY[direction]
    
    if isInBounds(newX, newY):

      if grid[newY][newX] != 0: continue

      grid[newY][newX] = value
      queue.append({'x': newX, 'y': newY})
  queue.pop(index)
  return queue

def TilesLeft ():
  # gets the number of tiles remaining in the array
  for y in range(height):
    for x in range(width):
      if grid[y][x] == 0:
        return True
  return False

width = 230
height = 70
grid = matrix.generate_matrix(width, height, 0)


# set starting points to random values
fill1Queue = [ {'x': r.randint(0,width-1), 'y':r.randint(0,height-1)} ]
fill2Queue = [ {'x': r.randint(0,width-1), 'y':r.randint(0,height-1)} ]
fill3Queue = [ {'x': r.randint(0,width-1), 'y':r.randint(0,height-1)} ]

while TilesLeft():
  while len(fill1Queue) > 0 or len(fill2Queue) > 0 or len(fill3Queue) > 0:
    # if a queue has tiles left, sets the queue to the result
    # of the floodfill method
    # specifies different values for each queue

    if (len(fill1Queue) > 0):
      fill1Queue = FillFrom(fill1Queue, "*")
    if (len(fill2Queue) > 0):
      fill2Queue = FillFrom(fill2Queue, "#")
    if (len(fill3Queue) > 0):
      fill3Queue = FillFrom(fill3Queue, ".")
    
    # draw the fill each loop
    os.system('cls')
    matrix.print_matrix(grid)
  

matrix.print_matrix(grid)
