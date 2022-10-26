from threading import Thread
import time

# class consists of
# name: station name
# buffer: customer queue
# delay_per_item: service time
# CustomerWaiting, busy: possible states of this station
class Station(Thread):
    def __init__(self, name, buffer, delay_per_item):
      print("Station created")
      Thread.__init__(self)
      #self.name = name
      #self.buffer = buffer
      #self.delay_per_item = delay_per_item
      ##self.CustomerWaiting = False
      #self.busy = False
    
    def run(self):
      print("Station started")