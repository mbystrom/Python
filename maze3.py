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
        print("fuckin dummy the x is wrong")
        return True
    if y < 0 or y >= height - 1:
        print("fuckin dummy the y is wrong")
        return True
    print("it's in bounds.. but you'll fuck up soon")
    return False

def CarvePassagesFrom(currentX, currentY, depth):
    directions = [N, S, E, W]
    print("directions are", directions)
    r.shuffle(directions)
    depth += 1
    print(f"depth is now {depth}")

    for direction in directions:
        nextX = currentX + DX[direction]
        nextY = currentY + DY[direction]
        print(f"({nextX}, {nextY})")

        if isOutOfBounds(nextX, nextY, grid):
            continue

        print("current grid value before zero check:",grid[currentY][currentX])
        if grid[nextY][nextX] == 0:
            print("passed zero check")
            grid[currentY][currentX] = (grid[currentY][currentX] | direction)
            grid[nextY][nextX] = (grid[nextY][nextX] | opposite[direction])
            print("current is now", grid[currentY][currentX])
            print("next is now", grid[nextY][nextX])
            CarvePassagesFrom(nextX, nextY, depth)
        else: print("failed zero check")
        
    print("fuck you")

def PrintMaze(grid):
    
    # first line
    print("  ", end="")
    for i in range(width - 2):
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
CarvePassagesFrom(0, 0, 0)
PrintMaze(grid)
