from threading import Thread, Event

import time

class utility:
  
  debug_factor    = 1000                          # decrement wait time for debugging
  station_timeout = 5                             # timeout for station to wait for customer
  
  allStations = []                                # list of all stations for ending simulation
  endStationEv = Event()                          # event to notify all stations to end simulation
  endSimulationEv = Event()                       # event to end simulation
  
