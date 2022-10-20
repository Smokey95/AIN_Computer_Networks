from heapq import heappush, heappop, heapify
import os

# class consists of
# q: event queue
# time: current time
# evCount: counter of all popped events
# methods push, pop, and start as described in the problem description

class EventQueue:
    
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
    while len(self.q) > 0:
      ev = self.pop()
      EventQueue.time = ev.t

      new_ev = ev.work(*ev.args)
      if new_ev is not None:
        self.push(new_ev)

      
      
  def __str__(self):
    return "%s" % str(self.q)
    