#file handling :
#NOTE - open function
# open(FILE_NAME or FILE_LOCATION, MODE(r(read), rb(read binary), r+(read&& write), w(write), a(append)))
#file.close()

file = open('test.txt', mode='r')
data = file.readline()
print(data)
file.close()

#NOTE - with open method
with open('test.txt', mode='r') as file:
  data =file.readline()
  print(data)


try:
  with open('sample/newFile.txt', 'w') as file:
    file.writelines(["\nThis is new file created👍🏻", "\nThis is second sentence."])
except FileNotFoundError as e:
  print('Error', e) 

