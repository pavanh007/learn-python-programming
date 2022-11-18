def find_factorial(num):
  if num<0:
    return 0
  else:
    factorial = 1
    for i in range(1, num + 1):
      factorial = factorial * i
    return factorial

print(find_factorial(10))

def find_factorial_of(number):
  if number == 1:
    return number
  else:
    return number * find_factorial_of(number-1)

num = 10
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", find_factorial_of(num))
