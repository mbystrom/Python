#include <iostream>

int add (int *num)
{
    *num += 17;
}

int main()
{
    int x = 12;
    add( &x );
    std::cout << x << std::endl;
}
