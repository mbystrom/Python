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
    
    
};

const int height = 20;
const int width = 20;

bool isOut (int x, int y);
void CarveMaze (int cx, int cy, int (*grid)[height][width]);
void PrintMaze (int (*grid)[height][width]);

int main()
{
    int map[height][width] = { 0 };
    CarveMaze(0, 0, &map);
    PrintMaze(&map);
}


void CarveMaze (int cx, int cy, int (*grid)[height][width])
{
    const Directions directions;
    int _dirs[4] = { directions.N, directions.S, directions.E, directions.W };
    std::random_shuffle(_dirs[0], _dirs[4]); // some error in random_shuffle here?
    
    std::map<int, int> DX {
        { directions.N, 0 },
        { directions.S, 0 },
        { directions.E, 1 },
        { directions.W, -1 }
    };
    
    std::map<int, int> DY {
        { directions.N, -1 },
        { directions.S, 1 },
        { directions.E, 0 },
        { directions.W, 0 }
    };
    
    std::map<int, int> Opposite {
        { directions.N, directions.S },
        { directions.S, directions.N },
        { directions.E, directions.W },
        { directions.W, directions.E }
    };
    
    for (uint i = 0; i < (sizeof(_dirs)/sizeof(_dirs[0])); i++) {
        int nx = cx + DX[_dirs[i]];
        int ny = cy + DY[_dirs[i]];
        
        if (isOut(nx,ny)) continue;
        
        if (*grid[ny][nx] == 0) {
            *grid[cy][cx] |= _dirs[i];
            *grid[ny][nx] |= Opposite[_dirs[i]];
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


void PrintMaze(int (*grid)[height][width])
{
    using namespace std;
    const Directions directions;
    
    for (int x = 0; x < width; x++) {
        cout << "__";
    }
    cout << endl;
    for (int y = 0; y < height; y++) {
        cout << "|";
        for (int x = 0; x < width; x++) {
            if ((*grid[y][x] & directions.S) != 0) {
                cout << " ";
            } else {
                cout << "_";
            }
            
            if ((*grid[y][x] & directions.E) != 0) {
                if (((*grid[y][x] | *grid[y][x+1]) & directions.S) != 0) {
                    cout << " ";
                } else {
                    cout << "_";
                }
            } else {
                cout << "|";
            }
        }
        cout << endl;
    }
}
