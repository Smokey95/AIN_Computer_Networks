from heapq import heappush, heappop, heapify

class EventQueue:
  """
  ### Class EventQueue
  Describe the event queue. Class consists of:
    q:        event queue
    time:     current time
    evCount:  counter of all popped events
    methods push, pop, and start as described in the problem description
  """
    
  q = []
  time = 0
  evCount = 0
    
    
  def __init__(self):
    heapify(self.q)


  def push(self, ev):
    heappush(self.q, ev)


  def pop(self):
    ev = heappop(self.q)
    self.time = ev.t
    self.evCount += 1
    return ev


  def start(self):
    self.printHeader()
    
    while len(self.q) > 0:
      ev = self.pop()
      EventQueue.time = ev.t
      new_ev = ev.work()
      print("| %4d | %s" %(EventQueue.time, str(ev)))
      while(new_ev is not None and new_ev.__len__() > 0):
        self.push(new_ev.pop(0))
    self.printEnd()
    

  def printHeader(self):
    print("===========================================================================================")
    print("| Time | Event                                                                             ")
    print("|------+-----------------------------------------------------------------------------------")
  
  def printEnd(self):
    print("==========================================================================================")
  
  def __str__(self):
    return "%s" % str(self.q)
    