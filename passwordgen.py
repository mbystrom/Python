import secrets as s

x = int(input("number of passwords to generate: "))
passwords = []

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
special = "@%+\/'!#$^?:,(){}[]~`-_."

for i in range(x):
  pw = ''
  for i in range(s.randbelow(10) + 10):
    z = s.randbelow(10) + 1
    if z <= 5:
      pw += s.choice(letters)
    elif z <= 8:
      pw += s.choice(numbers)
    else:
      pw += s.choice(special)
  passwords.append(pw)

print(passwords)
