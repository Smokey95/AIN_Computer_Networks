class Event:
    """
    ### Class consists of instance variables:
    timeStamp: Time stamp when a event occurs
    work: job to be done
    args: list of arguments for job to be done
    prio: used to give leaving, being served, and arrival different priorities
    """
    counter = 0

    def __init__(self, timeStamp, work, args=(), prio=255):
        self.t = timeStamp
        self.n = Event.counter
        self.work = work
        self.args = args
        self.prio = prio
        Event.counter += 1


    def process(self):
      self.work(*self.args)


    def __lt__(self, other):
      return self.t < other.t

    def __le__(self, other):
      return self.t <= other.t
    
    def __gt__(self, other):
      return self.t > other.t
    
    def __ge__(self, other):
      return self.t >= other.t
      
    def __eq__(self, other):
      return self.t == other.t

    #def __gt__(self, other):
    #    if self.t > other.t:
    #        return self.t > other.t
    #    else:
    #        return self.t > other.t
    
    #def __le__(self, other):
    #    if self.t = other.t:
    #        return self.prio <= other.prio
    #    else:
    #        return self.t <= other.t
    
    def __str__(self):
      return "[Time: %4d, Work: %s, EventID: %d]\n" % (self.t, self.work, self.n)
    
    def __repr__(self):
      return "[Time: %4d, Work: %s, EventID: %d]\n" % (self.t, self.work, self.n)