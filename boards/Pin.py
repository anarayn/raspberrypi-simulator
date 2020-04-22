# Indicates whether pin is analog or digital
ANALOG = 0
DIGITAL = 1

class Pin():
  def __init__(self,address:int,name:str, mode, state):
    self.address = address
    self.name = name
    self.mode = mode
    # Support Pull resistance
    # Supported pull pin resistance
    # support pin edges
    # support pin events
    # Supported pin edges
