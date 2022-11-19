
from abc import ABC, abstractmethod

class BANK(ABC):
  def basicInfo(self):
    print("This is generic bank")
    return "Generic bank: 0"

  @abstractmethod
  def withdraw(self):
    pass

class Swiss(BANK):
  bal = 1000
  def __init__(self) -> None:
    super().__init__()

  def basicInfo(self):
    print("This is swiss bank")
    return "swiss bank : "+ str(self.bal) 

  def withdraw(self, amount):
    if(amount < self.bal):
      print("Withdraw amount:", amount)
      print("New Balance :", self.bal - amount )
      return self.bal - amount
    else:
      print("Insufficient funds...")
      return self.bal

swiss = Swiss()
swiss.withdraw(100)