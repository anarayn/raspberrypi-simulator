# Indicates whether pin is analog or digital
DIGITAL_INPUT = 0
DIGITAL_OUTPUT = 1
PWM_OUTPUT = 2
GPIO_CLOCK = 3
SOFT_PWM_OUTPUT = 4
SOFT_TONE_OUTPUT = 5
PWM_TONE_OUTPUT = 6
ANALOG_INPUT = 7
ANALOG_OUTPUT = 8

class Pin():
  def __init__(self,value,name:str,direction):
    self.value = value
    self.name = name
    self.direction=direction

