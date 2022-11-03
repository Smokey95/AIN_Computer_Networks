from asyncio.windows_events import INFINITE
from threading import Thread, Event

import time

class Utility:
  
  debug_factor    = 1                          # decrement wait time for debugging
  station_timeout = 50000                             # timeout for station to wait for customer
  
  allStations = []                                # list of all stations for ending simulation
  endStationEv = Event()                          # event to notify all stations to end simulation
  endSimulationEv = Event()                       # event to end simulation
  
  simulation_start_time = 0                       # time when simulation started
  simulation_end_time = 0                         # time when simulation ended
  
  def __init__(self):
    pass
  
  def setSimulationStartTime(self):
    self.simulation_start_time = time.time_ns()
    
  def setSimulationEndTime(self):
    self.simulation_end_time = time.time_ns()
    
  def getSimulationDuration(self):
    return self.simulation_end_time - self.simulation_start_time
