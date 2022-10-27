from threading import Thread, Event
import time

debugFactor = 1000

# class consists of
# name: station name
# buffer: customer queue
# delay_per_item: service time
# CustomerWaiting, busy: possible states of this station
class Station(Thread):
    
    def __init__(self, delay_per_item, name):
      print("Station %s created" % name)
      Thread.__init__(self)
      self.name = name
      self.buffer = []
      self.delay_per_item = delay_per_item
      self.CustomerWaitingEv = Event()
      self.busy = False
  
    def run(self):
      
      while True:
        
        print("Station %s waiting for customers" % self.name)                                       # @todo remove after testing
        
        self.CustomerWaitingEv.wait()
        
        print("Customer arrived at %s" % self.name)                                                 # @todo remove after testing

        if(self.CustomerWaitingEv.is_set()):
          self.busy = True
          self.CustomerWaitingEv.clear()

          curr_customer = self.buffer.pop(0)                                                        # curr_customer = tuple with (customer serveEv, serve time)
          time.sleep(curr_customer[1] / debugFactor)                                                # sleeping until customer is finished

          curr_customer[0].serveEv.set()                                                            # setting event to notify customer that he is finished