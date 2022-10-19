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
        self.t          = timeStamp
        self.work       = work
        self.args       = args
        self.prio       = prio
        self.id         = Event.counter
        Event.counter  += 1


    def process(self):
      self.work(*self.args)
      
    def __lt__(self, other):
      return self.t < other.t
    
    def __le__(self, other):
      return self.t <= other.t

    def __str__(self):
      return "Event(time: %4d, prio: %3d, id: %2d, work: %s, args: %s)\n" % (self.t, self.prio, self.id, self.work, self.args)
    
    def __repr__(self):
      return "Event(time: %4d, prio: %3d, id: %2d, work: %s, args: %s)\n" % (self.t, self.prio, self.id, self.work, self.args)