def bill_total(bill):
  total = 0.00
  for key, value in bill.items():
    total += value
  return total

def calcualte_tax(percent, bill_total):
  return round((percent * bill_total)/ 100.0, 2)

food_bill = {
  1: 31.12,
  2: 34.12,
  5: 93.12,
  3: 73.12,
  4: 13.12,
}

food_total = bill_total(food_bill)
tax_total =  calcualte_tax(15, food_total)

print("Overall :", food_total + tax_total)

