# Constants to represent current state of pin
HIGH = 1
LOW = 0

class PinState():
  def __init__(self,value,name):
    self.value = value
    self.name = name