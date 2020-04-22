class Led(Module):
  def __init__(self,positive, negative, color, name):
    self.positive=positive
    self.negative=negative
    self.color=color
    self.name=name

  def update(self,positiveVolt,negativeVolt):
    pass

  def getVoltage(self,pin):
    pass

  def getResistance(self,positive,negative):
    pass