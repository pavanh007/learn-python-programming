class Recipe():
  def __init__(self, dish, items, time) -> None:
    self.dish = dish
    self.items = items
    self.time = time

  def contents(self):
    print('The {} has  {} and takes {} min to prepare.'.format(self.dish, self.items, self.time))

pizza = Recipe("Pizza", ['Cheese', 'bread', 'tomato'], 45)
pizza.contents()

