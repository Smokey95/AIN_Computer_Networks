from threading import Thread, Event
import time

debugFactor = 1000

class Customer(Thread):
  
  served = dict()
  dropped = dict()
  complete = 0
  duration = 0
  duration_cond_complete = 0
  count = 0

  def __init__(self, einkaufsliste, name, start_time):
    print("Customer %s created" % name)
    Thread.__init__(self)
    self.einkaufsliste = einkaufsliste
    self.name = name
    self.start_time = start_time
    self.serveEv = Event()
    

  def run(self):

    time.sleep(self.start_time / debugFactor)

    while(True):

      time.sleep(self.einkaufsliste[0][0] / debugFactor) 
                                                 #sleeps until arriving at station
      self.einkaufsliste[0][1].CustomerWaitingEv.set()                                              #wakes up current station

      serving_time = self.einkaufsliste[0][1].delay_per_item * self.einkaufsliste[0][2]             
      self.einkaufsliste[0][1].buffer.append((self, serving_time))                          #queues itself into the buffer of the current station

      while(True):
        print("Customer %s waiting to be served at %s" % (self.name, self.einkaufsliste[0][1].name))#waiting at station to be served
        self.serveEv.wait()
        print("Bliblablubb")
        if(self.serveEv.is_set()):
          self.serveEv.clear()
          
          print("Customer %s served" % self.name)
          self.einkaufsliste.pop(0)                                                               #removes itself from the einkaufsliste
          break

    print("Customer started")


# please implement here