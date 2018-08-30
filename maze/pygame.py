from enum import Enum
import random as r
from msvcrt import getch
import os

_map = [
    ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','#','#','#','#','#','#','#','#','#','#','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'],
    ['#','.','.','.','#','#','#','.','#','#','#','#','#','#','#','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
]

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vec):
            print("other is Vec!")
            x = self.x + other.x
            y = self.y + other.y
            return Vec(x, y)
        if isinstance(other, Direction):
            print("other is Direction!")
            x = self.x + other.value.x
            y = self.y + other.value.y
            return Vec(x, y)

class Direction(Enum):
    N = Vec(0, -1)
    S = Vec(0, 1)
    E = Vec(1, 0)
    W = Vec(-1, 0)

class Player:
    def __init__(self, vec, glyph):
        self.pos = vec
        self.glyph = glyph
        self.health = 100

    def move(self, direction):
        newPos = self.pos + direction
        if _map[newPos.y][newPos.x] == '.':
            self.pos = newPos


def Render(player):
    print('\n'*100)
    for y in range(len(_map)):
        for x in range(len(_map[0])):
            if player.pos.y == y and player.pos.x == x:
                print(player.glyph, end='')
            else:
                print(_map[y][x], end='')
        print()

def GetInput():
    key = ord(getch())
    if key == 224 or key == 0:
        key = ord(getch())
    return key

possibleVecs = []
for y in range(len(_map)):
    for x in range(len(_map[0])):
        if _map[y][x] == '.':
            possibleVecs.append(Vec(x,y))

playerPos = r.choice(possibleVecs)
player = Player(playerPos, '@')

print("execution begun!")
while True:
    Render(player)
    key = GetInput()

    if key == 72:
        player.move(Direction.N)
    elif key == 80:
        player.move(Direction.S)
    elif key == 75:
        player.move(Direction.W)
    elif key == 77:
        player.move(Direction.E)
    elif key == 27:
        break
