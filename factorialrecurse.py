# a simple program demonstrating recursive functions

def factorial (n):
  if n == 0:
    return 1
  else:
    return (n * factorial(n-1))

print(f"factorial of 5 is {factorial(5)}")