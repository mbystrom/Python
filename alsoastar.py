import matrix
import random as r

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Point(x, y)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

class Directions:
  N  = Point(0, -1)
  S  = Point(0, 1)
  E  = Point(1, 0)
  W  = Point(-1, 0)
  NE = Point(1, -1)
  SE = Point(1, 1)
  NW = Point(-1, -1)
  SW = Point(-1, 1)

  All = [N, NE, E, SE, S, SW, W, NW]
  Cardinal = [N, S, E, W]
  Diagonal = [NE, NW, SE, SW]

class Node:
  def __init__(self, pos=None, parent=None):
    self.pos = pos
    self.parent = parent

    self.g = 0
    self.f = 0
    self.h = 0
  
  def __eq__(self, other):
    return self.pos == other.pos

def heuristic(node1, node2):
  dX = abs(node2.pos.x - node1.pos.x)
  dY = abs(node2.pos.y - node1.pos.y)
  if dX > dY: return dX
  else: return dY

def getLowestF(ls):
  current = ls[0]
  for i in ls:
    if i.f < current.f:
      current = i
  return current

def isOut(pos, maze):
  if pos.x < 0 or pos.x >= len(maze[0]): return True
  if pos.y < 0 or pos.y >= len(maze): return True
  return False

def neighbors(node, maze):
  neighbors = []
  for direction in Directions.All: # change into 'Directions.Cardinal' for 4-way movement
    newPos = node.pos + direction
    if isOut(newPos, maze) or maze[newPos.y][newPos.x] != 0: continue
    newNode = Node(newPos, node)
    if direction in Directions.Diagonal:
      newNode.g = node.g + 1.414
    else: 
      newNode.g = node.g + 1
    neighbors.append(newNode)
  return neighbors

def constructPath(node):
  path = [node.pos,]
  while node.parent is not None:
    node = node.parent
    path.append(node.pos)
  return reversed(path)

def aStar(start, goal, maze):
  start.g = 0
  start.h = heuristic(start, goal)
  start.f = start.g + start.h

  openList = [start,]
  closedList = []
  while len(openList) > 0:
    current = getLowestF(openList)
    if current == goal:
      return constructPath(current)
    openList.remove(current)
    closedList.append(current)
    for neighbor in neighbors(current, maze):
      if neighbor not in closedList:
        neighbor.h = heuristic(neighbor, goal)
        neighbor.f = neighbor.g + neighbor.h
        if neighbor not in openList:
          openList.append(neighbor)
        else:
          for openNeighbor in openList:
            if neighbor.pos == openNeighbor.pos:
              if neighbor.g < openNeighbor.g:
                openNeighbor.g = neighbor.g
                openNeighbor.parent = neighbor.parent

maze = [[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]]


def validPoints(maze):
  points = []
  for y in range(len(maze)):
    for x in range(len(maze[0])):
      if maze[y][x] == 0:
        points.append(Point(x,y))
  return points

points = validPoints(maze)
startPos = r.choice(points)
endPos = r.choice(points)

start = Node(startPos, None)
end = Node(endPos, None)

path = aStar(start, end, maze)

for y in range(len(maze)):
  for x in range(len(maze[0])):
    if maze[y][x] == 0:
      maze[y][x] = '.'
    else:
      maze[y][x] = '#'

for i in path:
  maze[i.y][i.x] = 'X'

matrix.print_matrix(maze)

# https://www.growingwiththeweb.com/2012/06/a-pathfinding-algorithm.html
