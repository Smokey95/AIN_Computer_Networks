class Event:
    """
    ### Event Class
    """
    counter = 0                                                                                     # global event count class variable     

    def __init__(self, timeStamp, work, args=(), prio=255):
      """
      ### Event constructor
      Args: 
        timeStamp:  Time stamp when a event occurs
        work:       job to be done
        args:       list of arguments for job to be done
        prio:       used to give leaving, being served, and arrival different priorities
      """
      self.t          = timeStamp
      self.work       = work
      self.args       = args  #What should that be?
      self.prio       = prio
      self.id         = Event.counter
      Event.counter  += 1   
    
    def __lt__(self, other):
      if self.t < other.t:
        return True
      elif self.t == other.t:
        return self.prio < other.prio
      else:
        return False

    
    def __le__(self, other):
      if self.t < other.t:
        return True
      elif self.t == other.t:
        return self.prio <= other.prio
      else:
        return False


    def __str__(self):
      return "Event(time: %4d, prio: %3d, id: %2d, work: %7s, args: %s)" % (self.t, self.prio, self.id, self.work.__name__, self.args)
      
    def __repr__(self):
      return "Event(time: %4d, prio: %3d, id: %2d, work: %7s, args: %s)" % (self.t, self.prio, self.id, self.work.__name__, self.args)
      
    def getCustomerName(self):
      return self.work