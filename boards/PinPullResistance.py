OFF = 0
PULL_DOWN=1
PULL_UP = 2

class PinPullResistance():
  def __init__(self,value,name:str):
    self.value = value
    self.name = name
