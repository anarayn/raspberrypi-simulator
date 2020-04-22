# Constants to indicate whether pin is for input or output
INPUT = 0
OUTPUT = 1

class PinDirection():
  # Hashmap to maintain pins

  def __init__(self,name:str):
    self.name = name
  
  def createDigitalPin(provider:str,addres:int,name:str):
    pass
  

# protected static Pin createPin(String providerName, int address, String name, EnumSet<PinMode> modes,
#                                    EnumSet<PinPullResistance> resistance, EnumSet<PinEdge> edges) {
#         Pin pin = new PinImpl(providerName, address, name, modes, resistance, edges);
#         pins.put(name, pin);
#         return pin;
#     }