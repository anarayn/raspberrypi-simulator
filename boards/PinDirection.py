# Constants to indicate whether pin is for input or output
INPUT = 0
OUTPUT = 1

class PinDirection():
  def __init__(self,value:str,name:str):
    self.value = value
    self.name = name