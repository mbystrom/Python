import sys
import matrix
import random as r

# 1000 is the default recursion limit (raise it for larger mazes)
# 1000 only barely supports the current 50x40 maze
sys.setrecursionlimit(1000)

N = 1
S = 2
E = 4
W = 8

DX = { E: 1, W: -1, N:  0, S: 0 }
DY = { E: 0, W:  0, N: -1, S: 1 }

opposite = { E: W, W:  E, N:  S, S: N }

# globals for width and height of the maze
width = 10
height = 5


def isOutOfBounds(x, y):
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

        print("#", end="")

        for x in range(width-1):
            if grid[y][x] == 0:
                print("#", end="")
            else:
                print(".", end="")

            if grid[y][x] & E != 0:
                print(".", end="")
            else:
                print("#", end="")
        
        print("")

        print("#", end="")
        for x in range(width-1):
            
            if grid[y][x] & S != 0:
                print(".", end="")
            else:
                print("#", end="")
            
            print("#", end="")
        
        print("")

def CreateASCIIMaze (grid):
    maze = []
    firstLine = []
    firstLine.append('#')
    for i in range(width-1):
        firstLine.append('#')
        firstLine.append('#')
    maze.append(firstLine)

    for y in range(height-1):
        line = ['#',]
        for x in range(width-1):
            if grid[y][x] == 0: line.append('#')
            else: line.append('.')
            if grid[y][x] & E == 0: line.append('#')
            else: line.append('.')
        maze.append(line)
        line = ['#',]
        for x in range(width-1):
            if grid[y][x] & S == 0: line.append('#')
            else: line.append('.')
            line.append('#')
        maze.append(line)
    return maze

def GetTiles (grid, search):
    matchingTiles = []

    for y in range(len(grid)-1):
        
        for x in range(len(grid[0])-1):
            
            if grid[y][x] == search:
                matchingTiles.append({'x': x, 'y': y})

    return matchingTiles


grid = matrix.generate_matrix(width, height)

CarvePassagesFrom(0, 0)

maze = CreateASCIIMaze(grid)
matrix.print_matrix(maze)

availableTiles = GetTiles(maze, '.')
startPoint = r.choice(availableTiles)
destination = r.choice(availableTiles)

playerPosition = startPoint
lastPlayerPosition = startPoint

cont = True




def MovePlayer (key, pos):
    posX = pos['x']
    posY = pos['y']
    direction = 0

    if key == 72 or key == 56:
        direction = N
    if key == 80 or key == 50:
        direction = S
    if key == 75 or key == 52:
        direction = W
    if key == 77 or key == 54:
        direction = E
    
    posX += DX[direction]
    posY += DY[direction]

# the game loop
while cont:

    if lastPlayerPosition != playerPosition:
        maze[lastPlayerPosition['y']][lastPlayerPosition['x']] = '.'
    
    maze[playerPosition['x']][playerPosition['y']] = '@'
    lastPlayerPosition = playerPosition

    matrix.print_matrix(maze)

    # key handler
    key = ord(getch())
    validKeys = [27, 224, 72, 80, 75,
                 77, 50, 52, 54, 56]
    if key == 224 or key == 0:
        key = ord(getch())
    
    if key in validKeys:
        if key == 27:
            cont = False
        else:
            playerPosition = MovePlayer(key, playerPosition)
        

