import heapq
import os

# class consists of
# q: event queue
# time: current time
# evCount: counter of all popped events
# methods push, pop, and start as described in the problem description

class EventQueue:
    
  def __init__(self):
    self.q = []
    self.time = 0
    self.evCount = 0
# please implement here