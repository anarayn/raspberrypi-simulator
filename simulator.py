import simpy
from boards.RaspberryPi import RaspberryPi

env = simpy.Environment()

env.process(RaspberryPi(env))

env.run(until=15)