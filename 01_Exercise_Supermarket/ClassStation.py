# class consists of
# name: station name
# buffer: customer queue
# delay_per_item: service time
# CustomerWaiting, busy: possible states of this station
class Station():
  # please implement here
  
  def __init__(self, delay_per_item, name):
    self.name = name
    self.buffer = []
    self.delay_per_item = delay_per_item
    self.CustomerWaiting = False
    self.busy = False
    
  def lineUp(self, customer):
    self.buffer.append(customer)
    self.CustomerWaiting = True
  
  def __str__(self):
    return self.name