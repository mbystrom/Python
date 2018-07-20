import random as r
import os
import time

class Coord ():
    x = 0
    y = 0
    empty = False

    def __init__ (self,x,y,empty = True):
        self.x = x
        self.y = y
        self.empty = empty

    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y

    def __ne__ (self, other):
        return self.x != other.x and self.y != other.y


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

def isInBounds(coord):
    if coord.x > 0 and coord.x < width:
        if coord.y > 0 and coord.y < height:
            return True
    return False

def OpenMooreNeighbors (coord):
    neighbors = 0
    #print(f"checking ({coord.x}, {coord.y})")
    for y in range(coord.y - 1, coord.y + 2):
        for x in range(coord.x - 1, coord.x + 2):
            checking = Coord(x,y)
            if isInBounds(checking):
                #print(f"maze at ({y}, {x}): {maze[y][x]}")
                if maze[y][x] == 0:
                    neighbors = neighbors + 1
            else:
                #print(f"maze at ({x}, {y}) does not exist")
                neighbors = neighbors + 1
    #print ("neighbors:",neighbors)
    return neighbors

def NeumannNeighbors (coord):
    neumanns = [
        Coord(coord.x, coord.y - 1),
        Coord(coord.x, coord.y + 1),
        Coord(coord.x - 1, coord.y),
        Coord(coord.x + 1, coord.y)
    ]
    keep = []
    for n in neumanns:
        if isInBounds(n):
            keep.append(n)
    return neumanns
    

def GetTiles ():
    availableTiles = []
    for y in range(height):
        for x in range(width):
            currentTile = Coord(x,y,True)
            if OpenMooreNeighbors(currentTile) == 0:
                availableTiles.append(currentTile)
    return availableTiles

def isDrawable (coord):
    neighbors = NeumannNeighbors(coord)
    for neighbor in neighbors:
        if isInBounds(neighbor):
            if maze[coord.y][coord.x] == 0:
                return False
            else:
                mooreNeighbors = OpenMooreNeighbors(neighbor)
                if mooreNeighbors > 2:
                    return False
        else:
            return False
    return True


def DrawMaze ():
    coords = GetTiles()
    currentTile = r.choice(coords)
    while isDrawable (currentTile):
        nextOptions = NeumannNeighbors(currentTile)
        validOptions = []
        for i in nextOptions:
            print(f"{i.x}, {i.y}")
            if isDrawable(i):
                validOptions.append(i)
        maze[currentTile.y][currentTile.x] = 0
        if len(validOptions) > 0:
            currentTile = r.choice(validOptions)
        os.system('cls'); print()
        print_matrix(maze)
        time.sleep(0.01)
    return maze


def Recurse ():
    # code for recursive backtrack goes here
    return 0

width = 64
height = 32
maze = generate_matrix(width,height)

DrawMaze()
print_matrix(maze)
