import os

files = os.listdir('./testdir')

for filename in files:
    print(f'{filename}:')
    f = open('./testdir/'+filename, 'r')
    newFile = []
    for line in f:
        newLine = line.replace('for', 'blefd')
        newFile.append(newLine)
    f.close()
    f = open('./testdir/'+filename, 'w')
    f.writelines(newFile)
    print(newFile)
