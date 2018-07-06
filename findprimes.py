def GetPrime (x):
  import math

  wall = math.ceil(math.sqrt(x))
  isPrime = True

  for i in range(2,wall):
    if x % i == 0:
      isPrime = False
      break
  return isPrime

_max = int(input("How many prime numbers do you want? "))

primes = [2,]
i = 3
while len(primes) < _max:
  isPrime = GetPrime(i)
  if isPrime:
    primes.append(i)
  i += 1

print(primes)