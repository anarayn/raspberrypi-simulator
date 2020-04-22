class Connector(Module):
  def __init__(self,pin1, pin2, name):
    self.pin1=pin1
    self.pin2=pin2
    self.name=name

  def update(self,pin1Voltage,pin2Voltage):
    pass

  def getVoltage(self,pin):
    pass

  def getResistance(self,pin1,pin2):
    pass