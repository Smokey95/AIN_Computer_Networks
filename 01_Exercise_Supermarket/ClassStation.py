# class consists of
# name: station name
# buffer: customer queue
# delay_per_item: service time
# CustomerWaiting, busy: possible states of this station
class Station():
  # please implement here
  
  def __init__(self, operatingTime, name):
    self.operatingTime = operatingTime
    self.name = name
    
  def __str__(self) -> str:
    return self.name