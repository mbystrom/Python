x=input();z=1;r=False
while z>0:
    print((' '*z).join(x))
    if r:z-=1
    else:z+=1
    if z>=len(x):r=True
