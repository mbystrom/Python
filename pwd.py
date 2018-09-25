import secrets

words = ['abbess', 'dysphoria', 'nonarterial', 'muting', 'tendency',
         'tetrachord', 'whirlwind', 'chrysopid', 'choose']

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
special = "@%+\/'!#$^?:,(){}[]~`-_."

num = int(input("number of passwords: "))
passwords = []

for i in range(num):
    pw = ''
    while len(pw) < (secrets.randbelow(5) + 12):
        z = secrets.randbelow(10) + 1
        if z <= 3:
            pw += secrets.choice(words)
        elif z <= 5:
            pw += secrets.choice(letters)
        elif z <= 8:
            pw += secrets.choice(numbers)
        else:
            pw += secrets.choice(special)
    passwords.append(pw)

for i in passwords:
    print(i)
