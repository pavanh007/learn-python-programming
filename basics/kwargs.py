def sum_of(*args):
  sum = 0
  for x in args:
    sum += x
  return sum

print(sum_of(3, 4, 10, 11))


def bill_sum(**kwargs):
  sum = 0
  for key, value in kwargs.items():
    sum += value
  return round(sum)


print(bill_sum(coffe=3, cake=4))


def total_fruits(**kwargs):
    print(kwargs, type(kwargs))


total_fruits(banana=5, mango=7, apple=8)