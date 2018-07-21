import random as r

directions = {
  'N': 1,
  'S': 2,
  'E': 4,
  'W': 8
}

class Room ():

  def __init__ (self, xPos, yPos, width, height):
    self.width = width
    self.height = height
    self.xPos = xPos
    self.yPos = yPos
    self.tiles = generate_matrix(width, height)

  def FillTiles (self):
    for y in range(self.height):
      for x in range(self.width):
        if y > 0:
          self.tiles[y][x] |= directions['N']
        if y < (self.height - 1):
          self.tiles[y][x] |= directions['S']
        if x > 0:
          self.tiles[y][x] |= directions['W']
        if x < (self.width - 1):
          self.tiles[y][x] |= directions['E']



def generate_matrix (width, height):
  matrix = []

  for i in range(height):
    matrix.append([])

    for j in range(width):
      matrix[i].append(j)

  for y in range(height):
    for x in range(width):
      matrix[y][x] = 0

  return matrix

room1 = Room(0,0,5,4)
room1.FillTiles()
for i in room1.tiles:
  print("| ", end="")
  for j in i:
    print(j, end=" | ")
  print("")
  