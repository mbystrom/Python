'''
To-do:
1. Flood fill to get regions
2. Make sure all regions are connected
3. Add extra connectors
4. Uncarve unused tiles
'''

import sys, time
import matrix
import random as r

start = time.time()

sys.setrecursionlimit(3000)

N = 1
S = 2
E = 4
W = 8

DX = { E: 1, W: -1, N:  0, S: 0 }
DY = { E: 0, W:  0, N: -1, S: 1 }

opposite = { E: W, W:  E, N:  S, S: N }

width = 50
height = 20
grid = matrix.generate_matrix(width, height, 0)

minRoomSize = 3
maxRoomSize = 8
roomAttemps = 25
tilesInRooms = []


def isOut (x, y):
  if x < 0 or x >= width: return True
  if y < 0 or y >= height: return True
  
  return False

def CarveMaze (currentX, currentY):
  directions = [N, S, E, W]
  r.shuffle(directions)
  for direction in directions:
    nextX = currentX + DX[direction]
    nextY = currentY + DY[direction]

    if isOut (nextX, nextY): continue

    if grid[nextY][nextX] == 0:
      grid[currentY][currentX] |= direction
      grid[nextY][nextX] |= opposite[direction]
      CarveMaze(nextX, nextY)


def AddRoom (xPos, yPos, roomWidth, roomHeight):
  # check if room is drawable
  drawable = True
  for y in range(roomHeight):
    for x in range(roomWidth):
      realX = x + xPos
      realY = y + yPos
      
      if isOut(realX, realY): 
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

        tilesInRooms.append({'x': realX, 'y': realY})


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

def GetEmptyTiles ():
  empty = []
  for y in range(height):
    for x in range(width):
      
      if grid[y][x] == 0:
        empty.append({'x': x, 'y': y})
  
  return empty


def CreateASCIIMaze (grid):
    maze = []
    firstLine = []
    firstLine.append('#')
    for i in range(width):
        firstLine.append('#')
        firstLine.append('#')
    maze.append(firstLine)

    for y in range(height):
        line = ['#',]
        for x in range(width):
            if grid[y][x] == 0: line.append('#')
            else: line.append('.')
            if grid[y][x] & E == 0: line.append('#')
            else: line.append('.')
        maze.append(line)
        line = ['#',]
        for x in range(width):
            if grid[y][x] & S == 0: line.append('#')
            else: line.append('.')
            
            if grid[y][x] == 15 or (grid[y][x] == 14 and {'x': x, 'y': y} in tilesInRooms) \
              or (grid[y][x] == 6 and {'x': x, 'y': y} in tilesInRooms) \
              or (grid[y][x] == 7 and {'x': x, 'y': y} in tilesInRooms):
                line.append('.')
            else:
              line.append('#')
        maze.append(line)
    return maze

def TilesNotInRooms ():
  notInRoom = []
  for y in range(height):
    for x in range(width):
      position = {'x': x, 'y': y}
      if asciiMaze[y][x] == '.' and position not in tilesInRooms:
        notInRoom.append(position)
  return notInRoom

def GetWalls ():
  walls = []
  for y in range(height):
    for x in range(width):
      position = {'x': x, 'y': y}
      if asciiMaze[y][x] == '#':
        walls.append(position)
  return walls

def Flood (stack):
  index = len(stack['queue']) - 1 
  point = stack['queue'][index]
  directions = [N, S, E, W]
  for direction in directions:
    newX = point['x'] + DX[direction]
    newY = point['y'] + DY[direction]
    if isOut(newX, newY): continue
    if asciiMaze[newY][newX] != '.': continue
    newPoint = {'x': newX, 'y': newY}
    if newPoint in stack['list']: continue
    stack['queue'].append(newPoint)
    stack['list'].append(newPoint)
  stack['queue'].pop(index)
  return stack

def FillFrom (point):
  stack = {'queue': [point,], 'list': [point,]}
  while len(stack['queue']) > 0:
    stack = Flood(stack)
  return stack['list']

PlaceRooms(roomAttemps)

emptyTiles = GetEmptyTiles()
while len(emptyTiles) > 0:
  target = r.choice(emptyTiles)
  CarveMaze(target['x'], target['y'])
  emptyTiles = GetEmptyTiles()

asciiMaze = CreateASCIIMaze(grid)

tilesInRooms = []
regions = []

notInRoom = TilesNotInRooms()
while len(notInRoom) > 0:
  region = FillFrom(notInRoom[0])
  for i in region: tilesInRooms.append(i)
  regions.append(region)
  notInRoom = TilesNotInRooms()

while len(regions) > 1:
  walls = GetWalls()
  possibleConnectors = []

  for wall in walls:
    directions = [N, S, E, W]
    adjacentTiles = []
    positionX = wall['x']
    positionY = wall['y']
    for direction in directions:
      newX = positionX + DX[direction]
      newY = positionY + DY[direction]

      if asciiMaze[newY][newX] == '.':
        adjacentTiles.append({'x': newX, 'y': newY})
    
    tilesWithRegions = []
    for region in regions:
      for tile in adjacentTiles:
        if tile in region:
          tilesWithRegions.append({'tile': tile, 'region': region})
    
    for i in range(len(tilesWithRegions)):
      if i == 0: continue
      if tilesWithRegions[i]['region'] != tilesWithRegions[0]['region']:
        possibleConnectors.append(wall)
  connector = r.choice(possibleConnectors)

  asciiMaze[connector['y']][connector['x']] = '.'

  tilesInRooms = []
  regions = []

  notInRoom = TilesNotInRooms()
  while len(notInRoom) > 0:
    region = FillFrom(notInRoom[0])
    for i in region: tilesInRooms.append(i)
    regions.append(region)
    notInRoom = TilesNotInRooms()

matrix.print_matrix(asciiMaze)

end = time.time()
elapsed = end - start
print("yikes that took", elapsed, "seconds to run!")
