
def convertToNumber (stri):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  nums = []
  for i in stri:
    try:
      num = letters.index(i)
    except: continue
    if num > 26:
      num -= 26
    nums.append(num)
  return nums

def convertToString (arr):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  string = ''
  for i in arr:
    letter = letters[i]
    string += letter
  return string

def reversecaesar (cipher, shiftamount):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  numeric = convertToNumber(cipher)
  changednums = []
  for num in numeric:
    num -= shiftamount
    if num < 0:
      num += 26
    changednums.append(num)
  change = convertToString(changednums)
  return change

go = True
while go:
  stringtoreverse = input('\nEnter a string to decrypt: ')
  potentials = []

  for i in range(26):
    potential = reversecaesar(stringtoreverse, i)
    potentials.append(potential)

  for i in potentials:
    print(i, "\n\n")
  
  while True:
    yn = input("Decrypt another string? (y/n) ")
    if yn.casefold() == 'y': break
    elif yn.casefold() == 'n':
      go = False
      break
    else:
      print("invalid input")