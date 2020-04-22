INPUT_PIN = 0
OUTPUT_PIN = 1
STATE_HIGH = 1
STATE_LOW = 0

class Pin():
  def __init__(self,number,typ, state):
    self.number = number
    self.type = typ
    self.state = state
