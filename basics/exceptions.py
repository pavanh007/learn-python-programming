def divided_by(a,b):
  return a / b

try:
  print(divided_by(10, 0))
except Exception as e:
  print(e.__class__)
  print('Something went wrong! ::', e)