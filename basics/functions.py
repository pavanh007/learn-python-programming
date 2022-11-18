def sum(x, y):
  return x + y

print(sum(3, 4))

def tax_calculation(bill, tax_rate):
  return (bill * tax_rate) / 100.00

print('Total tax:', tax_calculation(175.00, 15))

#NOTE - SCOPING 

#NOTE - LEGB : local, enclosing, global and built-in

#GLOBAL
global_scop = 10

def fn1():
  local_scop_fn1 = 2
  def fn2():
    local_scop_fn2 = 4
    print('My global variable: ', global_scop)
    print(local_scop_fn1)
    print('My local to fn2 variable: ', local_scop_fn2)
  fn2()

fn1()
