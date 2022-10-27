from threading import Thread, Event
from ClassUtility import *

import time

class Customer(Thread):
  
  served = dict()
  dropped = dict()
  complete = 0
  duration = 0
  duration_cond_complete = 0
  count = 0

  def __init__(self, einkaufsliste, name, start_time):
    print("| Customer |     %5s | created" % name)
    Thread.__init__(self)
    self.einkaufsliste = einkaufsliste
    self.name = name
    self.start_time = start_time
    self.serveEv = Event()
    Customer.count += 1
    

  def run(self):

    time.sleep(self.start_time / utility.debug_factor)

    while(True):

      if(len(self.einkaufsliste) == 0):
        self.completeCustomer()
        break


      time.sleep(self.einkaufsliste[0][0] / utility.debug_factor)                                            #sleeps until arriving at station
      self.einkaufsliste[0][1].CustomerWaitingEv.set()                                              #wakes up current station

      serving_time = self.einkaufsliste[0][1].delay_per_item * self.einkaufsliste[0][2]             
      self.einkaufsliste[0][1].buffer.append((self, serving_time))                                  #queues itself into the buffer of the current station

      while(True):
        
        self.printCustomerWait()
        self.serveEv.wait()
        
        if(self.serveEv.is_set()):
          self.serveEv.clear()
          
          self.printCustomerServed()
          self.einkaufsliste.pop(0)                                                               #removes itself from the einkaufsliste
          break
  
  
  def printCustomerWait(self):
    print("| Customer |     %5s | walking to: %s" % (self.name, self.einkaufsliste[0][1].name))
  
  def printCustomerServed(self):
    print("| Customer |     %5s | served at:  %s" % (self.name, self.einkaufsliste[0][1].name))
    
  def completeCustomer(self):
    print("| Customer |     %5s | DONE" % self.name)
    Customer.complete += 1
    if Customer.complete == Customer.count:
      utility.endSimulationEv.set()