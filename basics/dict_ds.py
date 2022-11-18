#DICTIONARY is ordered, changeable and non duplicate collection of key-value pair of items


sample_dict = {
  1: "pavan",
  'second': "kiran",
  3: "eshwar"
  }

print(type(sample_dict))

print(sample_dict[1])

sample_dict[3] = 'you'
print(sample_dict[3])
# del sample_dict[3]
print(sample_dict)

for key, value in sample_dict.items():
  print(key, ":", value)

for value in sample_dict.values():
  print(value)


