#NOTE - set remove the duplicate and set element is not accessable by index
set_a = {1, 2, 3, 4, 5, 5}
set_b = { 5, 6, 7, 8, 9}

print('Ref set :', set_a)
print('Ref set :', set_b)

set_a.add(6) #Addding element
print('After adding 6 :', set_a)

set_a.remove(2) # removing
print('After removing 2 :', set_a)

set_a.discard(3)
print('After discard 3 :', set_a)

print('After .union() keyword  : ', set_a.union(set_b))
print('After union |(symbol) : ', set_a |set_b)

print('After .intersection() keyword  : ', set_a.intersection(set_b))
print('After intersection &(symbol) : ', set_a & set_b)

print('After difference :', set_a.difference(set_b))
print('After difference -(symbol) :', set_a - set_b)

print('After symmetric_difference :',
      set_a.symmetric_difference(set_b)) #except union elements
print('After difference ^(symbol) :', set_a ^ set_b)
