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

  def __init__(self, einkaufsliste, name):
    print("| Customer |     %5s | created" % name)
    Thread.__init__(self)
    self.einkaufsliste = einkaufsliste
    self.name = name
    self.serveEv = Event()
    Customer.count += 1
    

  def run(self):

    while(True):

      # ----------------- Check if customer is done -----------------
      if(len(self.einkaufsliste) == 0):
        self.completeCustomer()
        break
      
      # ----------------- Walk to next station -----------------
      self.printCustomerWait()
      time.sleep(self.getCurrentWalkTime() / utility.debug_factor)                                  #sleeps until arriving at station
      self.getCurrentStation().CustomerWaitingEv.set()                                              #wakes up current station
      
      # ----------------- Wait for station to be free -----------------
      serving_time = self.getCurrentStation().delay_per_item * self.getCurrentAmount()            
      self.einkaufsliste[0][1].buffer.append((self, serving_time))                                  #queues itself into the buffer of the current station
        
      self.serveEv.wait()
      
      # ----------------- Customer is served -----------------
      if(self.serveEv.is_set()):
        self.serveEv.clear()
        
        self.printCustomerServed()
        self.einkaufsliste.pop(0)                                                               #removes itself from the einkaufsliste
        
  
  def getCurrentWalkTime(self):
    return self.einkaufsliste[0][0]
  
  def getCurrentStation(self):
    return self.einkaufsliste[0][1]
  
  def getCurrentAmount(self):
    return self.einkaufsliste[0][2]
    
  def printCustomerWait(self):
    print("| Customer |     %5s | walking to: %s" % (self.name, self.getCurrentStation().name))
  
  def printCustomerServed(self):
    print("| Customer |     %5s | served at: %s" % (self.name, self.getCurrentStation().name))
    
  def completeCustomer(self):
    print("| Customer |     %5s | >>> DONE" % self.name)
    Customer.complete += 1
    
    # ----------------- Check if all customers are done -----------------
    if Customer.complete == Customer.count:
      print("|-------------------------------------------------------------")
      print("| >>> Simulation complete")
      utility.endStationEv.set()
      for station in utility.allStations:
        print("| >>> Station %s Thread terminated" % station.name)
        station.CustomerWaitingEv.set()
      utility.endSimulationEv.set()
      
      
      
      