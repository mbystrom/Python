import random as r

x = int(input("number of passwords to generate: "))
y = int(input("minimum length: "))
passwords = []

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
special = "@%+\/'!#$^?:,(){}[]~`-_."

for i in range(x):
  pw = ''
  for i in range(r.randint(y,20)):
    z = r.randint(1,10)
    if z <= 5:
      pw += r.choice(letters)
    elif z <= 8:
      pw += r.choice(numbers)
    else:
      pw += r.choice(special)
  passwords.append(pw)

print(passwords)
