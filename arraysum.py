def sumArray (arr):
  s = 0
  for i in range(len(arr)):
    if type(arr[i]) == list:
      s += sumArray(arr[i])
    else:
      s += arr[i]

  return s

print(sumArray([2,5,6,4,[2,4],9,[2,[11,4,4],6],8]) == 67)