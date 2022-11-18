trail = 'reversal'

#NOTE : str[start:stop:step]
new_trail =trail[::-1]
print(new_trail)

def string_reverse(str):
  if len(str) == 0:
    return str
  else:
    return string_reverse(str[1:]) + str[0]
  
str = 'reversal'

print(string_reverse(str))