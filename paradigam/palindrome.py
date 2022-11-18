def isPalindrome(input):
  startIndex = 0
  endIndex = len(input) - 1

  for x in input:
     if input[startIndex] != input[endIndex]:
      return False
  return True

print(isPalindrome('navan'))
print(isPalindrome('pavan'))
