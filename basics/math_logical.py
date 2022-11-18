#math operator
num1 = 10
num2 = 15

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#boolean
a = True
b = False

if a and not(b):
  print("Both are true")
elif a or b:
  print("One is false")
else:
  print('Both are false')

bill_total = 110
if bill_total > 100:
  print("Bill is greater than 100!")

cash_money = 110

if bill_total == cash_money:
  print("Pay as in bill")
else:
  print("Pay extra tips")

http_status = 200

if http_status == 200 or http_status == 201:
  print('Success')
elif http_status == 400:
  print('Bad request')
elif http_status == 404:
  print('Not found')
elif http_status == 500 or http_status == 501:
  print('Server Error')
else:
  print('Unknown')

match http_status:
  case 200 | 201:
    print('Success')
  case 400:
    print('Not found')
  case 500 | 501:
    print('Server Error')
  case _ :
    print('Unknown')

friends = ['naveen', 'nithin', 'shivu', 'vinay', 'jagdev', 'darshan']

print('In for loop:')
for idx, friend in enumerate(friends):
  print(idx, friend)

count = 0
print('In while loop:')
while count < len(friends):
  print(friends[count])
  count += 1


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

count = 0
#outer loop
for x in list1:
  count += 1
  #inner loop
  for y in list2:
    count += 1
# 90 becuase outer loop runs 9 times and innner loop runs (9 * 9) times
print(count) 

import time
start_time = time.time()
#outer loop
for i in range(10):
  #inner loop
  for j in range(10):
    print(i, end=" ")
  print()

print(round(time.time() - start_time, 2))

