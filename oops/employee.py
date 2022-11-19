class Employees:
  def __init__(self, name, last) -> None:
    self.name = name
    self.last = last

class Supervisors(Employees):
  def __init__(self, name, last, password) -> None:
    super().__init__(name, last)
    self.password = password

class Chefs(Employees):
  def leave_request(self, days):
    return "May I take leave for " + str(days) + " days."  # type: ignore

Pavan = Employees("Pavan", "H")
Naveen = Chefs("Pavan", "H")
Mahesh  = Supervisors("Mahesh", "Nellur", "apple#123")

print(Naveen.leave_request(3))
print(Mahesh.password)
