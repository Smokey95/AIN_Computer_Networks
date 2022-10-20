# class consists of
# statistics variables
# and methods as described in the problem description
from tkinter import E
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
      event = Event(EventQueue.time + walk_time, self.arrival, prio=1)
      return event


    def arrival(self):

      print(EventQueue.time)
      #curr_store = self.einkaufsliste[0][1]
      #curr_store.queue(self)
#
      #curr_store.serve()

      #return "arrival: %d" % self.start


    def leaving(self):
      return "leaving: %d" % self.end


    def __str__(self) -> str:
      return self.name