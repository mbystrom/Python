def GetPrime (x):
  import math

  wall = math.ceil(math.sqrt(x))
  isPrime = True

  for i in range(2,wall):
    if x % i == 0:
      isPrime = False
      break
  return isPrime

x = int(input("enter a number for primality check: "))

if GetPrime(x):
  print("your number is prime")
else:
  print("your number is not prime")