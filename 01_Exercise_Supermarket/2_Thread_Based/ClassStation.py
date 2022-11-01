from threading import Thread, Event, Lock
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
      self.bufferLock = Lock()
      self.delay_per_item = delay_per_item
      self.CustomerWaitingEv = Event()
      self.cweLock = Lock()
      self.busy = False
  
    def run(self):
      
      while True:
        
        if(self.getCurrentBufferLength() != 0):
          self.setCustomerWaitingEvent()
        
        # ----------------- waiting for customer -----------------  
        print("| Station  |  %8s | waiting for customer" % self.name)
        self.CustomerWaitingEv.wait(utility.station_timeout)
        
        if utility.endStationEv.is_set():
          break
        
        # ----------------- customer arrived -----------------
        if(self.CustomerWaitingEv.is_set()):
          self.busy = True
          self.clearCustomerWaitingEvent()

          curr_customer = self.getCurrentCustomer()                                                 # curr_customer = tuple with (customer serveEv, serve time)
          print("| Station  |  %8s | Customer arrived: %s" % (self.name, curr_customer[0].name))
          time.sleep(curr_customer[1] / utility.debug_factor)                                       # sleeping until customer is finished

          curr_customer[0].serveEv.set()                                                            # setting event to notify customer that he is finished
        # ----------------- customer timeout -----------------  
        else:
          print("| Station  |  %8s | TIMEOUT" % self.name)
          break
    
      
    def getCurrentCustomer(self):
      '''
      returns the first customer in the buffer
      '''
      self.bufferLock.acquire()
      curr_customer = self.buffer.pop(0)
      self.bufferLock.release()
      return curr_customer
      
    def getCurrentBufferLength(self):
      '''
      returns the length of the buffer
      '''
      self.bufferLock.acquire()
      curr_len = len(self.buffer)
      self.bufferLock.release()
      return curr_len
      
    def queueCustomer(self, customer, serving_time):
      '''
      queues customer at station buffer
      '''
      self.bufferLock.acquire()
      self.buffer.append((customer, serving_time))
      self.bufferLock.release()
      
    def setCustomerWaitingEvent(self):
      '''
      sets the CustomerWaitingEv event
      '''
      self.cweLock.acquire()
      self.CustomerWaitingEv.set()
      self.cweLock.release()
      
    def clearCustomerWaitingEvent(self):
      '''
      clears the CustomerWaitingEv event
      '''
      self.cweLock.acquire()
      self.CustomerWaitingEv.clear()
      self.cweLock.release()
    