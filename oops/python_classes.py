class MyClass:
  a = 5
  print("Hello world!!")

  def hello(self):
    print("hello you!!")
myClass = MyClass()
print(myClass.a)
print(myClass.hello())


class myFirstClass():
  index = 'Author-Book'
  print('Who wrote this?')

  def __init__(self, philosopher, book) -> None:
    self.philosopher = philosopher
    self.book = book

  def hand_list(self):
    print('{} wroke the book: {}'.format(self.philosopher, self.book))


whodunit = myFirstClass("Pluto", "Republic")
whodunit.hand_list()

#NOTE - without __init__ also

class mySecondClass():
  index = 'Author-Book'
  print('Who wrote this?')

  def hand_list(self, philosopher, book):
    print('{} wroke the book: {}'.format(philosopher, book))


whodunit = mySecondClass()
whodunit.hand_list("Pluto", "Republic")

