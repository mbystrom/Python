import sys, os, time
import matrix
import random as r
from msvcrt import getch

# 1000 is the default recursion limit (raise it for larger mazes)
sys.setrecursionlimit(1000)

N = 1
S = 2
E = 4
W = 8

DX = { E: 1, W: -1, N:  0, S: 0 }
DY = { E: 0, W:  0, N: -1, S: 1 }

opposite = { E: W, W:  E, N:  S, S: N }

# globals for width and height of the maze
width = 30
height = 15



# Functions for creating the maze
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


# Functions preparing the game
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


# Functions for the game loop
def GetTileAt(x, y):
    return maze[y][x]

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
    if GetTileAt(posX, posY) == '.' or GetTileAt(posX, posY) == 'x':
        return {'x': posX, 'y': posY}
    else:
        return pos


# --------------------------------------
# ------- MAIN BODY BEGINS HERE --------
# --------------------------------------
grid = matrix.generate_matrix(width, height)

CarvePassagesFrom(0, 0)

maze = CreateASCIIMaze(grid)

availableTiles = GetTiles(maze, '.')
startPoint = r.choice(availableTiles)
destination = r.choice(availableTiles)

playerPosition = startPoint
lastPlayerPosition = startPoint

cont = True


maze[destination['y']][destination['x']] = 'x'
exittype = ''


# ------------ THE GAME LOOP ------------
while cont:

    move = True

    if lastPlayerPosition != playerPosition:
        maze[lastPlayerPosition['y']][lastPlayerPosition['x']] = '.'
    
    maze[playerPosition['y']][playerPosition['x']] = '@'
    lastPlayerPosition = playerPosition

    matrix.print_matrix(maze)

    if playerPosition == destination:
        cont = False
        move = False
        exittype = 'win'

    if move == True:
        # key handler
        key = ord(getch())
        validKeys = [27, 224, 72, 80, 75,
                    77, 50, 52, 54, 56]
        if key == 224 or key == 0:
            key = ord(getch())
        
        if key in validKeys:

            if key == 27:
                cont = False
                exittype = 'quit'
            
            else:
                playerPosition = MovePlayer(key, playerPosition)

        os.system('cls')
        
if (exittype == 'quit'):
    print('spoilsport!')
elif (exittype == 'win'):
    print('you win!!\ngood job!')
else:
    print('p sure there was an error somewhere')


