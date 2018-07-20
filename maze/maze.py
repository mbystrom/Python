import random as r

class Coord ():
  x = 0
  y = 0
  empty = False

  def __init__ (self,x,y,empty):
    self.x = x
    self.y = y
    self.empty = empty

def generate_matrix (width, height):
  matrix = []
  for i in range(height):
    matrix.append([])
    for j in range(width):
      matrix[i].append(j)
  
  for y in range(height):
    for x in range(width):
      matrix[y][x] = 1
  
  return matrix

def print_matrix (matrix):
  for y in matrix:
    for x in y:
      if x == 0: x = "."
      else: x = "#"
      print(x,end="")
    print("")

def isDrawable(tile,visited):
  isDrawable = True

  if tile.x <= 0 or tile.x >= width - 1:
    isDrawable = False
  elif tile.y <= 0 or tile.y >= height - 1:
    isDrawable = False
  else:
    for y in range(tile.y-1, tile.y+2):
      for x in range(tile.y-1, tile.y+2):
        if x == tile.x and y == tile.y:
          continue
        else:
          for i in visited:
            if x == i.x and y == i.y:
              continue
          if maze[y][x] == 0:
            isDrawable = False

  return isDrawable

def ListEmptyTiles ():
  tiles = []
  for y in range(height):
    for x in range(width):
      if maze[y][x] == 1:
        tile = Coord(x,y,False)
        if isDrawable(tile,[]):
          tiles.append(tile)
      else:
        continue
  return tiles

def DrawMaze ():
  availableCoords = ListEmptyTiles()
  while len(availableCoords) > 0:
    activeCoord = r.choice(availableCoords)
    drawable = [0,]
    lastCoords = []
    while len(drawable) > 0:
      availableCoords.remove(activeCoord)
      drawable = []
      potentialCoords = [t for t in availableCoords if t.x >= activeCoord.x-1 and t.x <= activeCoord.x+1 and t.y >= activeCoord.y-1 and t.y <= activeCoord.y+1]
      for coord in potentialCoords:
        if coord == activeCoord: continue
        if isDrawable(coord,lastCoords):
          drawable.append(coord)
      maze[activeCoord.y][activeCoord.x] = 0
      lastCoords.append(activeCoord)
      activeCoord = r.choice(drawable)
      if len(lastCoords) > 3: lastCoords.pop(0)
    



width = 64
height = 32

maze = generate_matrix(width, height)
print_matrix(maze)
DrawMaze()