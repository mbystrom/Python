import sys
import random as r

# 1000 is the default recursion limit (raise it for larger (>50x40) mazes)
sys.setrecursionlimit(1000)

# directions correspond to bits
N = 1
S = 2
E = 4
W = 8

# see assignment of nextX and nextY, that's why these are important
DX = { E: 1, W: -1, N:  0, S: 0 }
DY = { E: 0, W:  0, N: -1, S: 1 }

# this allows us to open the next tile towards the current tile
opposite = { E: W, W:  E, N:  S, S: N }

# globals for width and height of the maze
width = 40
height = 17


def generate_matrix (width, height):
    # a simple process that slaps height lists of length width into a list
    # now depracated due to matrix.py module

    matrix = []

    for i in range(height):
        matrix.append([])
    
        for j in range(width):
            matrix[i].append(j)

    for y in range(height):
        for x in range(width):
            matrix[y][x] = 0

    return matrix


def isOutOfBounds(x, y):
    # check to make sure a coordinate is inside the area of the maze

    if x < 0 or x >= width - 1:
        return True
    if y < 0 or y >= height - 1:
        return True
    return False

def CarvePassagesFrom(currentX, currentY):
    # this is where the magic happens
    # recursively grows a maze from coordinates given in the first call

    directions = [N, S, E, W]
    r.shuffle(directions)

    for direction in directions:
        nextX = currentX + DX[direction]
        nextY = currentY + DY[direction]

        if isOutOfBounds(nextX, nextY):
            continue

        if grid[nextY][nextX] == 0:
            grid[currentY][currentX] |= direction
            grid[nextY][nextX] |= opposite[direction]
            CarvePassagesFrom(nextX, nextY)


def PrintMaze(grid):
    # first line
    print("#", end="")
    for i in range(width - 1):
        print("##", end="")
    print("")

    for y in range(height-1):

        # prints the west border
        print("#", end="")

        for x in range(width-1):

            # prints "#" if the cell is closed, otherwise "."
            if grid[y][x] == 0:
                print("#", end="")
            else:
                print(".", end="")
            
            # prints an opening to the cell on the right, if one exists
            if grid[y][x] & E != 0:
                print(".", end="")
            else:
                print("#", end="")
        
        # newline for the potential connections to open tiles below
        print("")

        # west wall of the maze
        print("#", end="")
        for x in range(width-1):
            
            # prints an opening to the cell below, if one exists
            if grid[y][x] & S != 0:
                print(".", end="")
            else:
                print("#", end="")
            
            # prints a '#' in between the potential openings
            # yes it's kind of weird but the mazes look fine
            print("#", end="")
        
        # prints a newline so the whole process can begin again
        print("")

# create a matrix usin width and height globals
grid = generate_matrix(width, height)

# start recursion at the very beginning of our maze
CarvePassagesFrom(0, 0)

# print out our finished maze
PrintMaze(grid)
