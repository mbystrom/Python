def generate_matrix (width, height):
  matrix = []
  for i in range(height):
    matrix.append([])
    for j in range(width):
      matrix[i].append(j)
  
  for y in range(height):
    for x in range(width):
      matrix[y][x] = 1
  
  return matrix

def print_matrix (matrix):
  for y in matrix:
    for x in y:
      print(x,end="")
    print("")