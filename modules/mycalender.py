import sys
locations = sys.path
for i in locations:
  print(i)


import calendar
leap = calendar.leapdays(2000, 2024)
print(leap)
isleap = calendar.isleap(2024)
print(isleap)