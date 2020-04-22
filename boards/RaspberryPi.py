from Pin import Pin
from Module import Module

class RaspberryPi(env):
  def __init__(self,env):
    self.env = env
    self.modules = {
      "LED" : Module("LED")
    }
    self.pins = {
      "1" : Pin(1, Pin.INPUT_PIN, Pin.STATE_HIGH),
      "2" : Pin(1, Pin.OUTPUT_PIN, Pin.STATE_LOW),
    }
    # Start the run process everytime an instance is created.
    self.action = env.process(self.run())

  def run(self):
    while True:
      print('Booting raspberry pi %d'%env.now)
      boot_time=3
      yield env.timeout(boot_time)

      print("Starting services at %d" % env.now)
      service_start_time=3
      yield env.timeout(service_start_time)

  def shutdown(self):
    pass

  def reboot(self):
    pass

  def add_module(self,module):
    pass

  def digital_input(self,pin,value):
    pass

  def digital_out(self,pin):
    pass