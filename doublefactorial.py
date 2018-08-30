def doubleFact(n):
    if n < 2: return 1
    return n * doubleFact(n-2)

assert (doubleFact(4)==8), "Double factorial of 4 should be 8!"
print(doubleFact(4))

assert (doubleFact(5)==15), "Double factorial of 5 should be 15!"
print(doubleFact(5))

assert (doubleFact(10)==3840), "Double factorial of 10 should be 3840!"
print(doubleFact(10))
