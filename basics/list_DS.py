#NOTE - BUILT-IN DS : list, tuple, dict, set

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list2 = ['pavan', 'H', 'CS', 1998, True]
list2 = ['pavan', ['H', 'CS', 1998], True]

print('Getting value by index :', list1[4]) #get from list
print('Before adding :',  list1)

list1.insert(0, 2) # inserting to list by specifying index : 0
print('After inserting :', list1, sep=' ')


list1.append(7)  # append at the end of the list
print('After appending :',list1, sep=' ')

list1.extend([8, 9, 10]) # we can extend the list
print('By extending : ', list1)

list1.pop(4)
print('By poping element : ', list1)

for x in list1:
  print('Value :', x)

