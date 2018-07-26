import random as r
import matrix

N = 1
S = 2
E = 4
W = 8

DX = {
    N: 0,
    S: 0,
    E: -1,
    W: 1
}

DY = {
    N: -1,
    S: 1,
    E: 0,
    W: 0
}

width = 100
height = 40
grid = matrix.generate_matrix(width, height, 0)


def isInBounds (x, y):
    if x < 0 or x >= width:
        return False
    
    if y < 0 or y >= height:
        return False
    
    return True

def Flood (queue, value, way):
    if way == 'oldest': index = 0
    elif way == 'newest': index = len(queue) - 1
    point = queue[index]

    directions = [N, S, E, W]
    r.shuffle(directions)
    
    try:
        grid[point['y']][point['x']] = value
    except:
        print("point was", point)
        exit()

    for direction in directions:
        nextX = point['x'] + DX[direction]
        nextY = point['y'] + DY[direction]

        if isInBounds(nextX, nextY):
            if grid[nextY][nextX] != 0: continue
            grid[nextY][nextX] = value

            queue.append({'x': nextX, 'y': nextY})
    
    queue.pop(index)

    return queue

def TilesRemain ():
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 0:
                return True
    return False

TLCornerSeed = {'x': r.randint(0, (width // 4)), 'y': r.randint(0, (height // 4))}
TLQueue = [TLCornerSeed]

TRCornerSeed = {'x': r.randint((width - (width // 4)), width-1), 'y': r.randint(0, (height // 4))}
TRQueue = [TRCornerSeed]

BLCornerSeed = {'x': r.randint(0, (width // 4)), 'y': r.randint((height - (height // 4)), height-1)}
BLQueue = [BLCornerSeed]

BRCornerSeed = {'x': r.randint(width - (width // 4), width-1), 'y': r.randint((height - (height // 4)), height-1)}
BRQueue = [BRCornerSeed]

centerSeed = {'x': r.randint(width // 2.5, width - (width // 2.5)), 'y': r.randint(height // 2.5, height - (height // 2.5))}
centerQueue = [centerSeed]

loops = 0
while TilesRemain():
    while len(centerQueue) > 0 or len(TLQueue) > 0 or len(TRQueue) > 0 or len(BLQueue) > 0 or len(BRQueue) > 0:
        if len(centerQueue) > 0:
            centerQueue = Flood(centerQueue, '.', 'newest')
        if len(TLQueue) > 0:
            TLQueue = Flood(TLQueue, '#', 'oldest')
        if len(TRQueue) > 0:
            TRQueue = Flood(TRQueue, '#', 'oldest')
        if len(BLQueue) > 0:
            BLQueue = Flood(BLQueue, '#', 'oldest')
        if len(BRQueue) > 0:
            BRQueue = Flood(BRQueue, '#', 'oldest')
        
        loops += 1

matrix.print_matrix(grid)
