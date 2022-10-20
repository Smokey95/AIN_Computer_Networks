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
      Customer.count += 1


    def begin(self):
      walk_time = self.einkaufsliste[0][0]
      station = self.einkaufsliste[0][1]
      event = [Event(EventQueue.time + walk_time, self.arrival, prio=1, args=(str(station), self.name))]
      return event


    def arrival(self):
      curr_station = self.einkaufsliste[0][1]
      amount = self.einkaufsliste[0][2]
      #max_customer = self.einkaufsliste[0][3]
      if not curr_station.isBusy() and not curr_station.isCustomerWaiting():
        curr_station.queue(self)
        if curr_station.serve() is not self:
          print("Error wrong customer got served :(")
          event = None
        else:
          event = [Event(EventQueue.time + (amount * curr_station.delay_per_item), self.leaving, prio=1, args=(str(curr_station), self.name))]
        return event
      elif curr_station.isBusy() or curr_station.isCustomerWaiting():
        curr_station.queue(self)
        event = None
        return event
      else:
        print("Error: Station is busy or customer is waiting")
        return None
      #elif station.isFull(max_customer):
      #  Customer.dropped[station.name] += 1
      #  return None


    def leaving(self):
      
      new_event = None
      
      curr_station = self.einkaufsliste[0][1]
      self.einkaufsliste.pop(0)                                                                     # remove current station from list
      
      if len(self.einkaufsliste) != 0:                                                              # check if there are more stations to visit
        walk_time = self.einkaufsliste[0][0]
        new_event = [Event(EventQueue.time + walk_time, self.arrival, prio=1, args=(str(self.einkaufsliste[0][1]), self.name))]
      else:
        self.end = EventQueue.time
        Customer.complete += 1
        Customer.duration += self.end - self.start
        new_event = None
        #if self.end - self.start > 60:
        #  Customer.duration_cond_complete += self.end - self.start
      
      if(curr_station.isCustomerWaiting()):
        print("There was a customer waiting")
        next_customer = curr_station.leave()  
        if(next_customer is not None):
          new_event.append(Event(EventQueue.time + (next_customer.einkaufsliste[0][2] * next_customer.einkaufsliste[0][1].delay_per_item), next_customer.leaving, prio=1, args=(str(next_customer.einkaufsliste[0][1]), next_customer.name)))
        else:
          print("Error: No customer waiting")
      else:
        curr_station.busy = False
      
      return new_event


    def __str__(self) -> str:
      return self.name