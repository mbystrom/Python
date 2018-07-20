import sys
import random as r

# 1000 is the default recursion limit (raise it for larger mazes)
# 1000 only barely supports the current 50x40 maze
sys.setrecursionlimit(3000)

# directions correspond to bits
N = 1
S = 2
E = 4
W = 8

# see assignment of nextX and nextY, that's why these are important
# they allow us to assign direction without a bunch of ifs
DX = { E: 1, W: -1, N:  0, S: 0 }
DY = { E: 0, W:  0, N: -1, S: 1 }

# this allows us to open the next tile towards the current tile
#  _______
# |_|_|_|_  <- corridors would look like that otherwise
# because corridors would only be open from one side
opposite = { E: W, W:  E, N:  S, S: N }

# globals for width and height of the maze
width = 115
height = 70


def generate_matrix (width, height):
    # a simple process that slaps height lists of length width into a list

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
    # prints out our maze

    # first line
    print("  ", end="")
    for i in range(width - 1):
        print("__", end="")
    print("")

    for y in range(height-1):

        # prints the west border
        print(" |", end="")
        for x in range(width-1):

            # print a space if the coordinate contains south (is open)
            if grid[y][x] & S != 0:
                print(" ", end="")
            else:
                print("_", end="")
            
            # print either underscore or space if coordinate contains east
            if grid[y][x] & E != 0:

                # print a space if combined this and next tile contains south
                if (grid[y][x] | grid[y][x+1]) & S != 0:
                    print(" ", end="")
                else:
                    print("_", end="")
            else:
                print("|", end="")    # print wall if east bit ot in coordinate
        print("")

# create a matrix usin width and height globals
grid = generate_matrix(width, height)

# start recursion at the very beginning of our maze
CarvePassagesFrom(0, 0)

# print out our finished maze
PrintMaze(grid)
