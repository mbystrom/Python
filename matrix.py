# a tool for creating and printing 2D matrices
# manipulation of values is done by "matrix[y-coord][x-coord]
# (0, 0) is in the top left corner

def generate_matrix (width, height, value = 0):
    # generates a 2D matrix of width "width" and height "height"
    # with initial value "value"

    matrix = []

    for y in range(height):
        
        matrix.append([])

        for x in range(width):

            matrix[y].append(value)

    return matrix

def print_matrix (matrix):
    # prints the a 2D matrix like the one generated above

    for i in matrix:
        for j in i:
            print(j, end="")
        print("")

