#NOTE -multi resolution order

class A:
  num = 10

class B(A):
  num = 13

class C(B):
  num = 12

#NOTE - returns the flow of classes
print(C.mro())
print(help(C))
