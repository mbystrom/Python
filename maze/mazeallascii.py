import matrix
import random as r

width  = 81
height = 41

N,S,E,W  = 1,2,4,8
DX       = { N: 0,  S: 0, E: 2, W: -2 }
DY       = { N: -2, S: 2, E: 0, W:  0 }

def isOut (x, y):
  if x < 1 or x >= width  - 1: return True
  if y < 1 or y >= height - 1: return True
  return False

def CarveMaze(x, y):
  directions = [N, S, E, W]
  r.shuffle(directions)

  maze[y][x] = '.'
  
  for direction in directions:
    nextX = x + DX[direction]
    nextY = y + DY[direction]

    if isOut(nextX, nextY): continue

    if maze[nextY][nextX] == '#':
      betweenX = x + (DX[direction]//2)
      betweenY = y + (DY[direction]//2)
      maze[nextY][nextX] = '.'
      maze[betweenY][betweenX] = '.'

      CarveMaze(nextX, nextY)

maze = matrix.generate_matrix(width, height, '#')
CarveMaze(1,1)

matrix.print_matrix(maze)
