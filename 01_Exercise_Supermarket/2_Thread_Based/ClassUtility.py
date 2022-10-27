from threading import Thread, Event

import time

class utility:
  
  debug_factor    = 1000
  station_timeout = 2
  
  endSimulationEv = Event()
