class PaySlip():
  def __init__(self, name, payment, amount) -> None:
    self.name = name
    self.payment = payment
    self.amount = amount
  
  def pay(self):
    self.payment = "yes"

  def status(self):
    if self.payment == 'yes':
      return self.name +  " is paid " + str(self.amount)
    else:
      return self.name + " is not paid yet"

Nathan = PaySlip('Nathan', 'no', 1200)
Rajesh = PaySlip('Rajesh', 'yes', 1200)

print(Nathan.status(),"\n",Rajesh.status())
Nathan.pay()
print(Nathan.pay())
print(Nathan.status(), "\n",Rajesh.status())
