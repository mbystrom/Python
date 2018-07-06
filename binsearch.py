def search (arr, targetValue):
  min = 0
  max = len(arr)
  guess = (min + max) // 2
  for i in range(len(arr)):
    guess = (min + max) // 2
    print(guess)
    if arr[guess] == targetValue:
      return guess;
    elif arr[guess] < targetValue:
      min = guess + 1
    else:
      max = guess - 1
  return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

result = search(primes, 73)
print("found prime at index ", result)