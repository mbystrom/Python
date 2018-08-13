import matrix as m;import random as r
N,S,E,W=1,2,4,8
DX={N:0,S:0,E:1,W:-1}
DY={N:-1,S:1,E:0,W:0}
o={N:S,S:N,E:W,W:E}
g=m.generate_matrix(10,10)
def c(x,y):
 d=[N,S,E,W];r.shuffle(d)
 for i in d:
  b=x+DX[i];n=y+DY[i]
  if (x>0 and x<10) and (y>0 and y<10) and g[n][b]==0:
   g[y][x]|=i
   g[n][b]|=o[i]
   c(b,n)
def p():
 print(" _"*11)
 for y in range(10):
  print(" |",end="")
  for x in range(10):
   if g[y][x]&S!=0:print(" ",end="")
   else:print("_",end="")
   if g[y][x]&E!=0:
    if(g[y][x]|g[y][x+1])&S!=0:print(" ",end="")
    else:print("_",end="")
   else:print("|",end="")
  print("")
c(0,0);p()
