from threading import Thread, Event
import time

# class consists of
# name: station name
# buffer: customer queue
# delay_per_item: service time
# CustomerWaiting, busy: possible states of this station
class Station(Thread):
    
    def __init__(self, name, delay_per_item):
      print("Station %s created" % name)
      Thread.__init__(self)
      self.name = name
      self.buffer = []
      self.delay_per_item = delay_per_item
      self.CustomerWaitingEv = Event()
      self.serveEv = None
      self.busy = False
    
    def run(self):
      print("Station %s waiting for customers" % self.name)
      while True:
        self.CustomerWaitingEv.wait()

        if(self.CustomerWaitingEv.is_set()):
          self.busy = True
          self.CustomerWaitingEv.clear()
          self.serveEv = Event((10, self.kundenliste[0]))
          self.buffer.append(Event())

