from msvcrt import getch

while True:
    key = ord(getch())
    if key == 27:
        break
    elif key == 224 or key == 0:
        print("special key! key was", key)
        key = ord(getch())
        print(key)
    else:
        print(key)
