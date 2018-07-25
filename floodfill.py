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

def isInBounds(x,y):
  # makes sure the point specified is in bounds
  # 99% sure this is O(1)
  if x < 0 or x >= width: return False
  if y < 0 or y >= height: return False
  return True

def FillFrom(queue, value):
  # fills available points around first queue item with specified value
  # removes current point from the queue so it can't be called again
  # returns list of points

  # change index for different fill patterns
  # 0 = oldest first, len(queue) - 1 = newest first, r.randint(0, len(queue) - 1) = random value
  # could even select those three and r.choice one of them
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
  queue.pop(index)
  return queue

def TilesLeft():
  # gets the number of tiles remaining in the array
  for y in range(height):
    for x in range(width):
      if grid[y][x] == 0:
        return True
  return False

width = 50
height = 20
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
