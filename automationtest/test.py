import os

os.chdir('./test')

files = os.listdir(os.getcwd())

for filename in files:
    extension = filename.split('.')
    if extension[1] == 'txt':
        f = open(filename, 'w')
        f.write("Hello World!")
        f.close()
