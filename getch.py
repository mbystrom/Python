from msvcrt import getch

while True:
    key = ord(getch())
    if key == 27:
        break
    elif key == 224 or key == 0:
        key = ord(getch())
        print(key)
    else:
        print(key)
