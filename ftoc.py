def ftoc (fahr, bound, step):
  if fahr <= bound:
    cel = (fahr * 5) / 9
    print("%3.0d %6.1f" % (fahr, cel))
    ftoc(fahr+step, bound, step)


for fahr in range(0,120,20):
  cel = (fahr * 5) / 9
  print("%3.0d %6.1f" % (fahr, cel))

ftoc(0,100,20)
