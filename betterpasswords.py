import secrets

words = ['abbess', 'dysphoria', 'kalamazoo', 'nonarterial', 'muting',
         'tendency', 'whirlwind', 'chrysopid', 'choose']

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'

specials_list = ["@%+\/'!#$^?:,(){}[]~`-_.",
                 "@.-_"]
specials = ""
numPass = 0
while True:
    try:
        numPass = int(input("number of passwords: "))
        break
    except:
        print("invalid input")

while True:
    try:
        for index, item in enumerate(specials_list):
            print(index+1, item)
        selection = int(input(
          "which set of special characters would you like? (choose the number) "))
        specials = specials_list[selection-1]
        break
    except:
        print("invalid input")


passwords = []
for i in range(numPass):
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
            pw += secrets.choice(specials)
        
    passwords.append(pw)


print("\n\n\n")
for i in passwords:
    print(i)
