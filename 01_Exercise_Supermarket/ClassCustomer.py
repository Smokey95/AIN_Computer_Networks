# class consists of
# statistics variables
# and methods as described in the problem description
from ClassEventQueue import EventQueue
from ClassEvent import Event

class Customer():
    
    served = dict()
    dropped = dict()
    complete = 0
    duration = 0
    duration_cond_complete = 0
    count = 0
    
    
    def __init__(self, einkaufsliste, name, start):
      self.einkaufsliste = einkaufsliste
      self.name = name
      self.start = start
      self.end = 0
      self.skipped = False
      Customer.count += 1


    def begin(self):
      curr_walk_time  = self.getWalkTime()
      curr_station    = self.getStation()
      curr_time       = self.getCurrentTime()
      
      return [Event(curr_time + curr_walk_time, self.arrival, prio=3, args=(str(curr_station), self.name))]


    def arrival(self):
      curr_station    = self.getStation()
      curr_amount     = self.getAmount()
      max_customer    = self.getMaxCustomer()
      
      if not curr_station.isBusy() and not curr_station.isCustomerWaiting():
        curr_station.queue(self)
        if curr_station.serve() is not self:
          print("| XXXX | Error wrong customer got served :(")
          event = None
        else:
          event = [Event(EventQueue.time + (curr_amount * curr_station.delay_per_item), self.leaving, prio=1, args=(str(curr_station), self.name))]
        return event
      elif curr_station.isBusy() or curr_station.isCustomerWaiting():
        if len(curr_station.buffer) < max_customer:
          curr_station.queue(self)
          event = None
          return event
        else:
          self.skipped = True
          Customer.dropped[curr_station.name] += 1
          event = self.leaving()
          print("| %4d | CUSTOMER %s SKIPPED" % (EventQueue.time, self.name))
          return event
      else:
        print("Error: Station is busy or customer is waiting")
        return None


    def leaving(self):
      
      new_event = None
      
      curr_station = self.getStation()
      self.einkaufsliste.pop(0)                                                                     # remove current station from list
      
      if len(self.einkaufsliste) != 0:                                                              # check if there are more stations to visit
        walk_time = self.getWalkTime()
        new_event = [Event(EventQueue.time + walk_time, self.arrival, prio=3, args=(str(self.einkaufsliste[0][1]), self.name))]
      else:
        self.end = EventQueue.time
        
        if not self.skipped:
          Customer.complete += 1
          Customer.duration_cond_complete += self.end - self.start
          Customer.duration += self.end - self.start
        else:
          Customer.duration += self.end - self.start
        new_event = None
        #if self.end - self.start > 60:
        #  Customer.duration_cond_complete += self.end - self.start
      
      if(curr_station.isCustomerWaiting()):
        next_customer = curr_station.leave()
        print("| %4d | There was a customer waiting! Customer: %s" % (EventQueue.time, str(next_customer)))  
        if(next_customer):
          if(new_event):
            new_event.append(Event(EventQueue.time + (next_customer.einkaufsliste[0][2] * next_customer.einkaufsliste[0][1].delay_per_item), next_customer.leaving, prio=1, args=(str(next_customer.einkaufsliste[0][1]), next_customer.name)))
          else:
            new_event = [Event(EventQueue.time + (next_customer.einkaufsliste[0][2] * next_customer.einkaufsliste[0][1].delay_per_item), next_customer.leaving, prio=1, args=(str(next_customer.einkaufsliste[0][1]), next_customer.name))]
        else:
          print("| XXXX | Error: No customer waiting")
      else:
        curr_station.busy = False
      
      return new_event


    def getCurrentTime(self):
      return EventQueue.time
  
    def getWalkTime(self):
      return self.einkaufsliste[0][0]
      
    def getStation(self):
      return self.einkaufsliste[0][1]
      
    def getAmount(self):
      return self.einkaufsliste[0][2]
      
    def getMaxCustomer(self):
      return self.einkaufsliste[0][3]
    
    def __str__(self) -> str:
      return self.name