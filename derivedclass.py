
class Base:

  def __init__ (self, num, num2):
    self.num = num
    self.num2 = num2
  
  def addNums(self):
    return self.num + self.num2

class Derived(Base):

  def __init__ (self, num, num2, nummm):
    Base.__init__(self, num, num2)
    self.nummm = nummm

  def etc (self):
    return self.nummm**self.num

base = Base(1, 2)
deriv = Derived(3, 4, 5)

print(f"Base: {base.num} + {base.num2} = {base.addNums()}")
print(f"Derived: nummm = {deriv.nummm}. sum of derived numbers: {deriv.addNums()}")
print(f"Derived etc: {deriv.etc()}")

arr = []
arr.append(base)
arr.append(deriv)

arr.append(Derived(3, 4, 1))

print(arr[0].addNums())
print(arr[2].etc())
