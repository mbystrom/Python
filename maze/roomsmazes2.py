import random as r
import matrix
import time

start = time.time()

width = 81
height = 41
roomAttempts = 20

N,S,E,W = 1,2,4,8

DX = { N: 0, S: 0, E: 2, W: -2 }
DY = { N: -2, S: 2, E: 0, W: 0 }

class Tile:
  def __init__ (self, x, y, isFloor=False):
    self.x = x
    self.y = y
    self.isFloor = isFloor

  def __eq__ (self, other):
    if (self.x == other.x and self.y == other.y and self.isFloor == other.isFloor):
      return True
    else:
      return False
  
  def __neq__ (self, other):
    if (self == other):
      return False
    else:
      return True
  

class Region:
  def __init__ (self, tiles):
    self.tiles = tiles
    self.edges = []

    for tile in self.tiles:
      for direction in [N,S,E,W]:
        nx = tile.x + (DX[direction]//2)
        ny = tile.y + (DY[direction]//2)
        if not grid[ny][nx].isFloor:
          self.edges.append(tile)

def gmatrix (width, height):
  matrix = []

  for y in range(height):    
    matrix.append([])
    for x in range(width):
      matrix[y].append(Tile(x, y, False))

  return matrix

def PrintMaze ():
  for row in grid:
    for tile in row:
      if tile.isFloor: print(".", end="")
      else: print("#", end="")
    print("")

def isOut (x, y):
  if x < 1 or x >= width-1: return True
  if y < 1 or y >= height-1: return True
  return False

def PlaceRooms (roomAttempts):
  minSize = 4
  maxSize = 8
  for i in range(roomAttempts):
    roomWidth = r.randint(minSize, maxSize)
    roomHeight = r.randint(minSize, maxSize)
    xPos = r.randint(1, (width - roomWidth - 1))
    yPos = r.randint(1, (height - roomHeight - 1))

    if (xPos % 2 == 0): xPos += 1
    if (yPos % 2 == 0): yPos += 1
    if (roomWidth % 2 == 1): roomWidth += 1
    if (roomHeight % 2 == 1): roomHeight += 1

    canPlaceRoom = True
    for y in range(yPos-1, yPos+roomHeight+2):
      for x in range(xPos-1, xPos+roomWidth+2):
        if (isOut(x, y) or grid[y][x].isFloor):
          canPlaceRoom = False
          break
    
    if not canPlaceRoom: continue

    for y in range(yPos, yPos+roomHeight+1):
      for x in range(xPos, xPos+roomWidth+1):
        grid[y][x].isFloor = True

def CarveMaze (cx, cy):
  directions = [N, S, E, W]
  r.shuffle(directions)

  grid[cy][cx].isFloor = True

  for direction in directions:
    nx = cx + DX[direction]
    ny = cy + DY[direction]

    if isOut(nx, ny): continue

    if not grid[ny][nx].isFloor:
      betweenX = cx + (DX[direction]//2)
      betweenY = cy + (DY[direction]//2)
      grid[ny][nx].isFloor = True
      grid[betweenY][betweenX].isFloor = True
      CarveMaze(nx, ny)

def CarveableTiles ():
  carveable = []
  for y in range(1, len(grid)-1, 2):
    for x in range(1, len(grid[0])-1, 2):
      neighbors = 0
      for direction in [N,S,E,W]:
        nx = x + (DX[direction]//2)
        ny = y + (DY[direction]//2)

        if isOut(nx, ny): continue

        if grid[ny][nx].isFloor: neighbors += 1
      if neighbors == 0:
        carveable.append(Tile(x, y, False))

  return carveable

def NotInRooms (flags):
  notInRoom = []
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if not grid[y][x].isFloor: continue
      if flags[y][x] == 1: continue
      notInRoom.append(grid[y][x])
  
  return notInRoom

def GetRegion (start, flags):
  regionTiles = []
  queue = [start,]

  while len(queue) > 0:
    tile = queue[0]
    regionTiles.append(tile)
    queue.pop(0)

    flags[tile.y][tile.x] = 1
    for direction in [N,S,E,W]:
      x = tile.x + (DX[direction]//2)
      y = tile.y + (DY[direction]//2)

      if isOut(x, y) or flags[y][x] == 1: continue

      currentTile = Tile(x, y, True)
      if grid[y][x].isFloor:
        flags[y][x] = 1
        queue.append(currentTile)
  
  return Region(regionTiles)

def GetRegions ():
  flags = matrix.generate_matrix(width, height, 0)
  notInRoom = NotInRooms(flags)
  
  regions = []
  while len(notInRoom) > 0:
    region = GetRegion(notInRoom[0], flags)
    regions.append(region)
    notInRoom = NotInRooms(flags)
  
  return regions

def ConnectRegions ():
  regions = GetRegions()
  
  for i in range(len(regions)):
    for j in range(len(regions)):
      if i == j: continue

      connectors = []

      for tile in regions[i].edges:
        for direction in [N,S,E,W]:
          x = tile.x + DX[direction]
          y = tile.y + DY[direction]

          for checkTile in regions[j].edges:
            if x == checkTile.x and y == checkTile.y:
              connectX = tile.x + (DX[direction]//2)
              connectY = tile.y + (DY[direction]//2)
              connectors.append(Tile(connectX, connectY, True))
      
      if len(connectors) > 0:
        connector = r.choice(connectors)
        grid[connector.y][connector.x].isFloor = True

def TilesToUncarve ():
  tiles = []

  for row in grid:
    for tile in row:
      if not tile.isFloor: continue

      neighbors = 0
      for direction in [N,S,E,W]:
        nx = tile.x + (DX[direction]//2)
        ny = tile.y + (DY[direction]//2)

        if isOut(nx, ny) or not grid[ny][nx].isFloor:
          neighbors += 1
      if neighbors >= 3:
        tiles.append(tile)
  
  return tiles

def UnCarve ():
  uncarve = TilesToUncarve()
  while len(uncarve) > 0:
    for tile in uncarve:
      grid[tile.y][tile.x].isFloor = False
    uncarve = TilesToUncarve()

################################################

grid = gmatrix(width, height)

PlaceRooms(roomAttempts)

carveable = CarveableTiles()
while len(carveable) > 0:
  CarveMaze(carveable[0].x, carveable[0].y)
  carveable = CarveableTiles()

startConnecting = time.time()
ConnectRegions()
finishConnecting = time.time()

startUncarving = time.time()
UnCarve()
finishUncarving = time.time()

PrintMaze()

end = time.time()

print(f"That took {end-start} seconds to run!")
print(f"It took {finishConnecting-startConnecting} seconds just to connect!")
print(f"It took {finishUncarving-startUncarving} seconds just to uncarve!")
