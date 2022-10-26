from threading import Thread, Event
import time

class Customer(Thread):
  
  served = dict()
  dropped = dict()
  complete = 0
  duration = 0
  duration_cond_complete = 0
  count = 0

  def __init__(self, einkaufsliste, name, start_time):
    self.einkaufsliste = einkaufsliste
    self.name = name
    self.start_time = start_time
    print("Customer %s created" % self.name)
    self.serveEv = Event()
    Thread.__init__(self)

  def run(self):

    time.sleep(self.start_time)

    while(True):
      if(self.serveEv.is_set()):
        self.serveEv.clear()
        self.serve()
        break
    print("Customer started")


# please implement here