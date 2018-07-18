import random as r

N = 1
S = 2
E = 4
W = 8

DX       = { E: 1, W: -1, N:  0, S: 0 }
DY       = { E: 0, W:  0, N: -1, S: 1 }
opposite = { E: W, W:  E, N:  S, S: N }

width = 10
height = 10

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


def isOutOfBounds(x, y, grid):
    if x < 0 or x >= width: return True
    if y < 0 or y >= height: return True
    return False

def CarvePassagesFrom(currentX, currentY, grid):
    directions = [N, S, E, W]
    r.shuffle(directions)

    for direction in directions:
        nextX = currentX + DX[direction]
        nextY = currentY + DY[direction]

        if not isOutOfBounds(nextX, nextY, grid): 
            grid[currentY][currentX] |= direction
            grid[nextY][nextX] |= opposite[direction]
            CarvePassagesFrom(nextX, nextY, grid)

def PrintMaze(grid):
    
    # first line
    print(" ", end="")
    for i in range(width):
        print(" _", end="")
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

maze = generate_matrix(width, height)
maze = CarvePassagesFrom(0, 0, maze)
PrintMaze(maze)
