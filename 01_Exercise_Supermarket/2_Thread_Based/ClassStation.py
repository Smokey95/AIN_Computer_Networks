from threading import Thread, Event
import time

from ClassCustomer import Customer
from ClassUtility import *

# class consists of
# name: station name
# buffer: customer queue
# delay_per_item: service time
# CustomerWaiting, busy: possible states of this station
class Station(Thread):
    
    def __init__(self, delay_per_item, name):
      print("| Station  |  %8s | created" % name)
      Thread.__init__(self)
      self.name = name
      self.buffer = []
      self.delay_per_item = delay_per_item
      self.CustomerWaitingEv = Event()
      self.busy = False
  
    def run(self):
      
      while True:
        
        if(len(self.buffer) != 0):
          self.CustomerWaitingEv.set()
        
        # ----------------- waiting for customer -----------------  
        print("| Station  |  %8s | waiting for customer" % self.name)
        self.CustomerWaitingEv.wait(utility.station_timeout)
        
        if utility.endStationEv.is_set():
          break
        
        # ----------------- customer arrived -----------------
        if(self.CustomerWaitingEv.is_set()):
          self.busy = True
          self.CustomerWaitingEv.clear()

          curr_customer = self.buffer.pop(0)                                                        # curr_customer = tuple with (customer serveEv, serve time)
          print("| Station  |  %8s | Customer arrived: %s" % (self.name, curr_customer[0].name))                                                 # @todo remove after testing
          time.sleep(curr_customer[1] / utility.debug_factor)                                                # sleeping until customer is finished

          curr_customer[0].serveEv.set()                                                            # setting event to notify customer that he is finished
        # ----------------- customer timeout -----------------  
        else:
          print("| Station  |  %8s | TIMEOUT" % self.name)
          break
