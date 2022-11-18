my_tuples = (1, 3, 'String', 4.5, 4.5, True)

#NOTE : key diff between list and tuple is we can't add item to tuple once declared

print(type(my_tuples))

print(my_tuples[2])

print(my_tuples.count(4.5))
print(my_tuples.index(3))

for x in my_tuples:
  print('Values in tuple :', x)

