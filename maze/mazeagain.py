import random as r

class Coord ():
  x = 0
  y = 0
  filled = True
  walls = {
    'left': True,
    'right': True,
    'top': True,
    'bottom': True
  }

  def __init__ (self, x, y, filled = True, walls = {
                'left': True,
                'right': True,
                'top': True,
                'bottom': True
                }):
    self.x = x
    self.y = y
    self.filled = filled
    self.walls = walls

  def __eq__ (self, other):
    return self.x == other.x and self.y == other.y and self.walls == other.walls and self.filled == other.filled

  def __ne__ (self, other):
    return self.x != other.x and self.y != other.y and self.walls != other.walls and self.filled != other.filled

def generate_matrix (width, height):
    
  matrix = []

  for i in range(height):
    matrix.append([])
  
    for j in range(width):
      matrix[i].append(j)

  for y in range(height):
    for x in range(width):
      walls = {
        'left': True,
        'right': True,
        'top': True,
        'bottom': True
      }
      cell = Coord(x, y)
      matrix[y][x] = cell

  return matrix

def isValid (coord):
  if coord.x not in bounds['x']:
    return False
  if coord.y not in bounds['y']:
    return False
  if maze[coord.y][coord.x] != coord:
    return False
  
  return True

def Carveable (coord):
  carveable = []
  x = coord.x
  y = coord.y
  for _dir in ['N', 'S', 'E', 'W']:
    
    if _dir == 'N':
      nextCoord = Coord(x, y - 1, True)
      if isValid(nextCoord):
        carveable.append({ 'coord': nextCoord, 'direction': _dir })
    
    elif _dir == 'S':
      nextCoord = Coord(x, y + 1)
      if isValid(nextCoord):
        carveable.append({ 'coord': nextCoord, 'direction': _dir })
    
    elif _dir == 'E':
      nextCoord = Coord(coord.x - 1, coord.y)
      if isValid(nextCoord):
        carveable.append({ 'coord': nextCoord, 'direction': _dir })
    
    elif _dir == 'W':
      nextCoord = Coord(coord.x + 1, coord.y)
      if isValid(nextCoord):
        carveable.append({ 'coord': nextCoord, 'direction': _dir })
    
  return carveable


def Carve (fromCoord, toCoord, direction):
  print("Carving!")
  if direction == 'N':
    # Set fromCoord properties
    maze[fromCoord.x][fromCoord.y].filled = False
    maze[fromCoord.x][fromCoord.y].walls['top'] = False

    # Set toCoord properties
    maze[toCoord.x][toCoord.y].filled = False
    maze[toCoord.x][toCoord.y].walls['bottom'] = False
  
  elif direction == 'S':
    # Set fromCoord propertie
    maze[fromCoord.x][fromCoord.y].filled = False
    maze[fromCoord.x][fromCoord.y].walls['bottom'] = False
    
    # Set toCoord properties
    maze[toCoord.x][toCoord.y].filled = False
    maze[toCoord.x][toCoord.y].walls['top'] = False
  
  elif direction == 'E':
    # Set fromCoord propertie
    maze[fromCoord.x][fromCoord.y].filled = False
    maze[fromCoord.x][fromCoord.y].walls['right'] = False
    
    # Set toCoord properties
    maze[toCoord.x][toCoord.y].filled = False
    maze[toCoord.x][toCoord.y].walls['left'] = False
  
  elif direction == 'W':
    # Set fromCoord propertie
    maze[fromCoord.x][fromCoord.y].filled = False
    maze[fromCoord.x][fromCoord.y].walls['left'] = False
    
    # Set toCoord properties
    maze[toCoord.x][toCoord.y].filled = False
    maze[toCoord.x][toCoord.y].walls['right'] = False

  
def GetCells ():
  availableCells = []
  for y in maze:
    for x in y:
      testCoord = Coord(x, y, False, walls = {
        'left': True,
        'right': True,
        'top': True,
        'bottom': True
      })
      
      if maze[y][x] == testCoord and maze[y][x].filled == True:
        availableCells.append(maze[y][x])
  
  return availableCells

def GenerateMaze ():
  cells = []
  start = { 'x': r.randint(0, width - 1), 'y': r.randint(0, height - 1) }
  startCoord = Coord(start['x'], start['y'], True)
  cells.append(startCoord)
  print(cells, len(cells))

  while len(cells) > 0:
    print("Starting Generation!")
    index = len(cells) - 1
    cell = cells[index]
    print("cell is", cell); print("len(cells) is", len(cells))

    uncarvedCells = Carveable(cell)
    print("available cells are", uncarvedCells)

    if len(uncarvedCells) > 0:
      nextCell = r.choice(uncarvedCells)

      Carve(cell, nextCell['coord'], nextCell['direction'])
      cells.append(nextCell['coord'])
    else:
      del cells[index]


def DrawMaze ():
  # top row
  for i in range(width*2 + 1):
    print("#", end="")
  print("")

  for y in maze:
    print("#", end="") # left wall of the maze
    for x in y:
      if x.filled == True:
        print("#", end="")
      else:
        print(".", end="")
      if x.walls["right"] == True:
        print("#", end="")
      else:
        print(".", end="")
    print("")

    # now we need to print connectors, if they exist, into the row below
    print("#", end="") # left wall of lower row
    for x in y:
      if x.walls['bottom'] == True:
        print("#", end="")
      else:
        print(".", end="")
      print("#", end="") # I'm like 99% sure it's impossible to go here
    print("")
      


width = 20
height = 20
bounds = {
  'x': range(width),
  'y': range(height)
}

maze = generate_matrix(width, height)
GenerateMaze()
DrawMaze()

'''
for y in bounds['y']:
  for x in bounds['x']:
    print(maze[y][x].filled)
    print("(", maze[y][x].x, ", ", maze[y][x].y, ")", sep="")
    print(maze[y][x].walls)
'''