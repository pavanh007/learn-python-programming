def d():
  animal = 'elephant'
  def e():
    nonlocal animal
    animal = 'cat'
    print('Inside nested function: ' + animal)
  print('Before calling the function :' + animal)

  e()
  print("After nested function: " + animal)

animal = 'camel'
d()
print('Global animal :', animal)
