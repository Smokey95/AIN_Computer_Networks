import heapq

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


  def queue(self, customer):
    self.buffer.append(customer)
    self.CustomerWaiting = True


  def serve(self):
    self.busy = True
    customer = self.buffer.pop(0)
    if len(self.buffer) == 0:
      self.CustomerWaiting = False
    customer.served(self.name)
    
    return customer


  def isBusy(self):
    return self.busy


  def isCustomerWaiting(self):
    return self.CustomerWaiting


  def __str__(self):
    return self.name