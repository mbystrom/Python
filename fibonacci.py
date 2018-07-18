import time

def fib (n):
    if n <= 1:
        print("base case reached - fuckin wait literally double the time you already have\n\n...\n...\n\n..\n\n... loser")
        return n
    else:
        return fib(n-1) + fib(n-2)

x = []
for i in range(1,11):
    x.append(fib(i))

for i in x:
    print(i)

y = 500
t = time.time()
z = fib(y)
runtime = time.time() - t
print(f"{z} is the {y}th fibonacci number \nfuck me, that took {runtime} seconds to complete")
