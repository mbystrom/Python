import sys
import random as r

N = 1
S = 2
E = 4
W = 8

DX       = { E: 1, W: -1, N:  0, S: 0 }
DY       = { E: 0, W:  0, N: -1, S: 1 }
opposite = { E: W, W:  E, N:  S, S: N }

width = 50
height = 40
depth = 0

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


def isOutOfBounds(x, y, grid):
    if x < 0 or x >= width - 1:
        return True
    if y < 0 or y >= height - 1:
        return True
    return False

def CarvePassagesFrom(currentX, currentY):
    directions = [N, S, E, W]
    r.shuffle(directions)

    for direction in directions:
        nextX = currentX + DX[direction]
        nextY = currentY + DY[direction]

        if isOutOfBounds(nextX, nextY, grid):
            continue

        if grid[nextY][nextX] == 0:
            grid[currentY][currentX] |= direction
            grid[nextY][nextX] |= opposite[direction]
            CarvePassagesFrom(nextX, nextY)


def PrintMaze(grid):
    
    # first line
    print("  ", end="")
    for i in range(width - 1):
        print("__", end="")
    print("")

    for y in range(height-1):
        print(" |", end="")
        for x in range(width-1):
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

grid = generate_matrix(width, height)
CarvePassagesFrom(0, 0)
PrintMaze(grid)
