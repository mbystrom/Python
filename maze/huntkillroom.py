import random as r
import matrix

N, S, E, W = 1, 2, 4, 8

DX = { N: 0, S: 0, E: 1, W: -1 }
DY = { N: -1, S: 1, E: 0, W: 0 }
Opposite = { N: S, S: N, E: W, W: E }

width = 50
height = 40

minRoomSize = 3
maxRoomSize = 8
roomAttempts = 25

grid = matrix.generate_matrix(width, height, 0)


# FUNCTIONS
def isIn (x, y):
  if x < 0 or x >= width: return False
  if y < 0 or y >= height: return False
  return True

def AddRoom (xPos, yPos, roomWidth, roomHeight):
  # check if room is drawable
  drawable = True
  for y in range(roomHeight):
    for x in range(roomWidth):
      realX = x + xPos
      realY = y + yPos
      
      if not isIn(realX, realY): 
        drawable = False
        break
      
      if grid[realY][realX] != 0:
        drawable = False
        break
  
  # add room to grid
  if drawable:
    for y in range(roomHeight):
      for x in range(roomWidth):
        realX = x + xPos
        realY = y + yPos

        if y > 0: grid[realY][realX] |= N
        if y < (roomHeight - 1): grid[realY][realX] |= S
        if x > 0: grid[realY][realX] |= W    
        if x < (roomWidth - 1): grid[realY][realX] |= E


def PlaceRooms (attempts):
  for i in range(attempts):
    size = r.randint(minRoomSize, maxRoomSize)
    irregularity = r.randint(0, minRoomSize)
    xy = r.randint(0,1)

    roomWidth = size
    roomHeight = size // 2
    if xy == 0: roomHeight += irregularity
    else: roomWidth += irregularity
    
    xPos = r.randint(0, width - (roomWidth+1))
    yPos = r.randint(0, height - (roomHeight+1))

    AddRoom(xPos, yPos, roomWidth, roomHeight)

def walk (x, y):
  dirs = [N, S, E, W]
  r.shuffle(dirs)

  for _dir in dirs:
    nx = x + DX[_dir]
    ny = y + DY[_dir]

    if isIn(nx, ny) and grid[ny][nx] == 0:
      grid[y][x] |= _dir
      grid[ny][nx] |= Opposite[_dir]
      return (nx, ny)
  
  return (-1, -1)

def hunt ():
  for y in range(height):
    for x in range(width):
      if grid[y][x] != 0: continue
      
      neighbors = []
      
      if y > 0 and grid[y-1][x] != 0: neighbors.append(N)
      if y+1 < height and grid[y+1][x] != 0: neighbors.append(S)
      if x+1 < width and grid[y][x+1] != 0: neighbors.append(E)
      if x > 0 and grid[y][x-1] != 0: neighbors.append(W)
      
      if len(neighbors) > 0:
        direction = r.choice(neighbors)
        nx = x + DX[direction]
        ny = y + DY[direction]

        grid[y][x] |= direction
        grid[ny][nx] |= Opposite[direction]

        return (nx, ny)
  return (-1, -1)

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

# MAIN STUFF

PlaceRooms(roomAttempts)

go = True
point = (0, 0)

while go:
  x = point[0]
  y = point[1]

  point = walk(x, y)

  if point == (-1, -1):
    point = hunt()
    if point != (-1,-1):
      go = True
    else:
      go = False

PrintMaze()
