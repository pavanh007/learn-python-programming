with open('sample.txt', 'r') as file:
  print(file.read(12)) # read the specific characters
  print(file.readline()) #read first line

with open('sample.txt', 'r') as file:
  data = file.readlines() #in the form of array of values
  for x in data:
    print(x)