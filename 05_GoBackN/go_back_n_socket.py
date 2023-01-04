import socket
from threading import Thread
import random
from math import ceil
from lossy_udp_socket import lossy_udp_socket


class go_back_n_socket():
  
  def __init__(self, localPort, remotePort, remoteAddress, PLR=0.1, segmentSize=1000, windowSize=10, debugFlag=False):
    self.localPort = localPort
    self.remotePort = remotePort
    self.remoteAddress = remoteAddress
    self.sock = lossy_udp_socket(self, localPort, (remoteAddress, remotePort), PLR)
    self.segmentSize = segmentSize
    self.windowSize = windowSize
    self.debugFlag = debugFlag

  def send(self, msg):
    # Get the length of the message
    msgLen = len(msg)
    print('SOCK DEBUG | Message length: ', msgLen) if self.debugFlag else None
    
    # Get the number of segments
    numSegments = ceil(msgLen / self.segmentSize)
    print('SOCK DEBUG | Number of segments: ', numSegments) if self.debugFlag else None
    
    # Store the message in a list of segments
    msgSegments = []
    for i in range(numSegments):
      msgSegments.append(msg[i * self.segmentSize : (i + 1) * self.segmentSize])
      print('SOCK DEBUG | Message segments: ', msgSegments) if self.debugFlag else None
    
    # Send the message segments
    for i in range(numSegments):
      print('SOCK DEBUG | Sending segment: ', msgSegments[i]) if self.debugFlag else None
      self.sock.send(msgSegments[i].encode('utf-8'))
  
    
  def receive(self, packet):
    msg = packet.decode('utf-8')
    print('SOCK DEBUG | Received message: ', msg) if self.debugFlag else None
    return msg
