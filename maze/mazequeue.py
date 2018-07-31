import matrix
import random as r

N = 1
S = 2
E = 4
W = 8

DX       = { E: 1, W: -1, N:  0, S: 0 }
DY       = { E: 0, W:  0, N: -1, S: 1 }
opposite = { E: W, W:  E, N:  S, S: N }

width = 20
height = 15

def isOut (x, y):
  if x < 0 or x >= width: return True
  if y < 0 or y >= height: return True
  return False

maze = matrix.generate_matrix(width, height, 0)
dirs = [N,S,E,W]
r.shuffle(dirs)
stack = [{'x': 0, 'y': 0, 'directions': dirs}]

while len(stack) > 0:
  index = len(stack)-1

  currentTile = stack[index]
  currentX = currentTile['x']
  currentY = currentTile['y']
  _directions = currentTile['directions']

  for direction in _directions:
    nextX = currentX + DX[direction]
    nextY = currentY + DY[direction]

    if isOut(nextX, nextY): continue
    
    if maze[nextY][nextX] == 0:
      maze[currentY][currentX] |= direction
      maze[nextY][nextX] |= opposite[direction]
      directions = [N,S,E,W]
      r.shuffle(directions)
      stack.append({'x': nextX, 'y': nextY, 'directions': directions})
  
  stack.pop(index)



# print maze
# first line
print("  ", end="")
for i in range(width - 1):
  print("__", end="")
print("")

for y in range(height):

  # prints the west border
  print(" |", end="")
  for x in range(width):

    # print a space if the coordinate contains south (is open)
    if maze[y][x] & S != 0:
      print(" ", end="")
    else:
      print("_", end="")
    
    # print either underscore or space if coordinate contains east
    if maze[y][x] & E != 0:

      # print a space if combined this and next tile contains south
      if (maze[y][x] | maze[y][x+1]) & S != 0:
        print(" ", end="")
      else:
        print("_", end="")
    else:
      print("|", end="")    # print wall if east bit ot in coordinate
  print("")