class Textil:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_square_c(self):
    return self.width / 6.5 + 0.5

  def get_square_j(self):
    return self.height * 2 + 0.3

  @property
  def get_square_full(self):
    return str(f'Общая площадь ткани \n'
               f'{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Jacket(Textil):
  def __init__(self, width, height):
    super().__init__(width, height)
    self.square_j = round(self.height * 2 + 0.3)

  def __str__(self):
    return f'Площадь ткани на костюм - {self.square_j}'

class Coat(Textil):
  def __init__(self, width, height):
    super().__init__(width, height)
    self.square_c = round(self.width / 6.5 + 0.5)

  def __str__(self):
    return f'Площадь ткани на пальто - {self.square_c}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)

print(coat)
print(jacket)
print(coat.get_square_full)
print(jacket.get_square_full)
print(coat.get_square_c())
print(jacket.get_square_j())