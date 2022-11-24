from threading import Thread, Event
from ClassUtility import *

import time

class Customer(Thread):
  
  served = dict()
  dropped = dict()
  complete = 0
  skippedCount = 0
  duration = 0
  duration_cond_complete = 0
  count = 0

  def __init__(self, einkaufsliste, name):
    print("| Customer |     %5s | created" % name)
    Thread.__init__(self)
    self.duration = time.time_ns()
    self.einkaufsliste = einkaufsliste
    self.name = name
    self.serveEv = Event()
    self.skipped = False
    Customer.count += 1
    

  def run(self):

    while(True):

      # ----------------- Check if customer is done -----------------
      if(len(self.einkaufsliste) == 0):
        self.completeCustomer()
        break
      
      # ----------------- Walk to next station -----------------
      self.printCustomerWait()
      time.sleep(self.getCurrentWalkTime() / Utility.debug_factor)                                  #sleeps until arriving at station
      curr_station = self.getCurrentStation()
      curr_station.setCustomerWaitingEvent()                                                        #wakes up current station
                                     
      # ----------------- Wait for station to be free -----------------
      serving_time = self.getCurrentStation().delay_per_item * self.getCurrentAmount()
      curr_station = self.getCurrentStation()

      if len(curr_station.buffer) < self.getMaxQueueLength():
        curr_station.queueCustomer(self, serving_time)                                                #queueing customer at station buffer                       

        self.serveEv.wait()

        # ----------------- Customer is served -----------------
        if(self.serveEv.is_set()):
          self.serveEv.clear()
          Customer.served[curr_station.name] += 1                                                           # increment served counter

          self.printCustomerServed()                                                                      #removes item from list
      else:
        self.skipped = True
        Customer.dropped[curr_station.name] += 1
        self.printCustomerSkipped()
      
      self.einkaufsliste.pop(0)                                                                   #removes itself from the einkaufsliste
        
  
  def getCurrentWalkTime(self):
    return self.einkaufsliste[0][0]
  
  def getCurrentStation(self):
    return self.einkaufsliste[0][1]
  
  def getCurrentAmount(self):
    return self.einkaufsliste[0][2]
    
  def getMaxQueueLength(self):
    return self.einkaufsliste[0][3]
    
  def printCustomerWait(self):
    print("| Customer |     %5s | walking to: %s" % (self.name, self.getCurrentStation().name))
  
  def printCustomerServed(self):
    print("| Customer |     %5s | served at: %s" % (self.name, self.getCurrentStation().name))
    
  def printCustomerSkipped(self):
    print("| Customer |     %5s | skipped at: %s" % (self.name, self.getCurrentStation().name))
    
  def completeCustomer(self):
    print("| Customer |     %5s | >>> DONE" % self.name)
    if not self.skipped:
      Customer.complete += 1
      Customer.duration_cond_complete += time.time_ns() - self.duration
      Customer.duration += time.time_ns() - self.duration
    else:
      Customer.duration += time.time_ns() - self.duration
      Customer.skippedCount += 1
    
    # ----------------- Check if all customers are done -----------------
    if (Customer.complete + Customer.skippedCount) == Customer.count:
      print("|-------------------------------------------------------------")
      print("| >>> Simulation complete")
      Utility.endStationEv.set()
      for station in Utility.allStations:
        print("| >>> Station %s Thread terminated" % station.name)
        station.CustomerWaitingEv.set()
      Utility.endSimulationEv.set()
      
      
      
      