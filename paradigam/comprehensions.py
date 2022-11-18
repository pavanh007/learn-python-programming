#NOTE : [<expression> for x in <sequence> if <condition>]

data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 19, 21, 13]

adding3 = [x+3  for x in data]
print('By adding 3 to all element :', adding3)

mul2 = [x*2  for x in data]
print('By multiply 2 by to all element :', adding3)

multiplier = [x for x in data if x%2 ==0]
print('2 multiplier element :', adding3)

divAfterNeg = [x-1 for x in data if x%4 ==0]
print('Divisible by 4-1  :', adding3)

a = [[96], [69]]

print(''.join(list(map(str, a))))

z = ["alpha", "bravo", "charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)


def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)
a = sum(5)
print(a)

numbers = [15, 30, 47, 82, 95]


def lesser(numbers):
   return numbers < 50


small = list(map(lesser, numbers))
print(small)
