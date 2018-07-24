#include <iostream>
#include <string>
#include <algorithm>
#include <map>

struct Directions
{
    const short N = 1;
    const short S = 2;
    const short E = 4;
    const short W = 8;
    
    const std::map<int, int> DX {
        { N, 0 },
        { S, 0 },
        { E, 1 },
        { W, -1 }
    };
    
    const std::map<int, int> DY {
        { N, -1 },
        { S, 1 },
        { E, 0 },
        { W, 0 }
    };
    
    const std::map<int, int> Opposite {
        { N, S },
        { S, N },
        { E, W },
        { W, E }
    };
};

const int height = 20;
const int width = 20;

bool isOut (int x, int y);

void CarveMaze (int cx, int cy, int (*grid)[height][width])
{
    const Directions directions;
    int _dirs[4] = { directions.N, directions.S, directions.E, directions.W };
    std::random_shuffle(_dirs[0], _dirs[4]);
    
    for (uint i = 0; i < (sizeof(_dirs)/sizeof(_dirs[0])); i++) {
        int nx = cx + directions.DX[_dirs[i]];
        int ny = cy + directions.DY[_dirs[i]];
        
        if (isOut(nx,ny)) continue;
        
        if (*grid[ny][nx] == 0) {
            *grid[cy][cx] |= _dirs[i]
            *grid[ny][nx] |= directions.Opposite[_dirs[i]]
            CarveMaze(nx, ny, &*grid);
        }
    }
}

bool isOut (int x, int y)
{
    if (x < 0 || x >= width) return true;
    
    if (y < 0 || y >= height) return true;
    
    return false;
}

int main()
{
    int map[height][width] = { 0 };
    CarveMaze(0, 0, &map);
}
