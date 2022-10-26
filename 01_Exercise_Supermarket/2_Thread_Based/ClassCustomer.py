from threading import Thread
import time

class Customer(Thread):
  served = dict()
  dropped = dict()
  complete = 0
  duration = 0
  duration_cond_complete = 0
  count = 0

  def __init__():
    Thread.__init__(self)
# please implement here