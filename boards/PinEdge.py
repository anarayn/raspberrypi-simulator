# Indicates whether pin is analog or digital
NONE = 0
BOTH = 1
RISING = 2
FALLING = 3

class Pin():
  def __init__(self,value,name:str):
    self.value = value
    self.name = name
