class A:
  def __init__(self, c) -> None:
    print("Inside class A")
    self.c = c
  print("Print inside A")

  def alpha(self):
    c = self.c + 1
    return c

print('Instantiating A...')
a = A(1)
print(a.alpha())
print('-----------')
class B(A):
   def __init__(self, a):
       print("Inside class B")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)


print("Instantiating B..")
b = B(a)
print(a)


