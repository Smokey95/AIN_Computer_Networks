import socket
from threading import Thread
import random
from math import ceil
from lossy_udp_socket import lossy_udp_socket
import time


class go_back_n_socket():

  currOffset = 0
  goBackNOffsetMasterImpl300VarName = 0
  currPackage = 0
  expectedPackage = 0
  resendCounter = 0
  

  def __init__(self, localPort, remotePort, remoteAddress, PLR=0.1, segmentSize=1000, windowSize=10, debugFlag=False, suppressFlag=False, timeout=1000):
    self.localPort = localPort
    self.remotePort = remotePort
    self.remoteAddress = remoteAddress
    self.lossy_udp_sock = lossy_udp_socket(self, localPort, (remoteAddress, remotePort), PLR)
    self.segmentSize = segmentSize
    self.windowSize = windowSize
    self.debugFlag = debugFlag
    self.suppressFlag = suppressFlag
    self.headerSize = 8
    self.timeout = timeout / 1000
    self.timer = time.time()
    self.startTimer = time.time()
    
    

  def send(self, msg):
    
    # Get the length of the message
    msgLen = len(msg)
    print('SOCK DEBUG | Message length: ', msgLen) if self.debugFlag else None
    
    # Get the number of segments
    numSegments = ceil(msgLen / (self.segmentSize - self.headerSize))
    print('SOCK DEBUG | Number of segments: ', numSegments) if self.debugFlag else None

    # Store the message in a list of segments
    msgSegments = []
    for i in range(0, numSegments):
      # segment[8 Byte ID | 992 Byte Data]
      # segment[00000009Hello World! This is a comment...]
      msgSegments.append(str(i).zfill(self.headerSize) + msg[i * (self.segmentSize - self.headerSize) : (i + 1) * (self.segmentSize - self.headerSize)])
      print('SOCK DEBUG | Message segments: ', msgSegments) if (self.debugFlag and not self.suppressFlag) else None

    # Send the message segments
    while(go_back_n_socket.currPackage < numSegments):

      if(time.time() - self.timer > self.timeout):
        print('SOCK DEBUG | ERROR: Timeout Go-Back-N!!!') if self.debugFlag else None
        go_back_n_socket.resendCounter += 1
        go_back_n_socket.currOffset = go_back_n_socket.currPackage - go_back_n_socket.expectedPackage
        go_back_n_socket.currPackage = go_back_n_socket.expectedPackage
        
        #go back n
      
      if(go_back_n_socket.currOffset < self.windowSize):
          if(self.debugFlag and not self.suppressFlag):
            print('SOCK DEBUG | Sending segment with ID | DATA: [' + self.getMsgID(msgSegments[go_back_n_socket.currPackage]) + ' | ' + msgSegments[self.currPackage] + ']')
          elif(self.debugFlag and self.suppressFlag):
            print('SOCK DEBUG | Sending segment with ID: [' + self.getMsgID(msgSegments[go_back_n_socket.currPackage]) + ']')
          
          self.lossy_udp_sock.send(msgSegments[go_back_n_socket.currPackage].encode('utf-8'))
          self.timer = time.time()
          go_back_n_socket.currOffset += 1
          go_back_n_socket.currPackage += 1
          print('SOCK DEBUG | Current Offset: ', go_back_n_socket.currOffset) if self.debugFlag else None
          
            
  def receive(self, packet):
    msg = packet.decode('utf-8')
    if(self.debugFlag and not self.suppressFlag):
      print('SOCK DEBUG | Received segment with ID | DATA: [' + self.getMsgID(msg) + ' | ' + msg + ']')
    elif(self.debugFlag and self.suppressFlag):
      print('SOCK DEBUG | Received segment with ID: [' + self.getMsgID(msg) + ']')
      
    currentID = int(self.getMsgID(msg))
    if(self.debugFlag):
      print('SOCK DEBUG | Current ID: ', currentID)
      print('SOCK DEBUG | Expected ID: ', go_back_n_socket.expectedPackage)
      print('SOCK DEBUG | Current Offset: ', go_back_n_socket.currOffset)
    
    if(currentID == go_back_n_socket.expectedPackage):
      go_back_n_socket.expectedPackage += 1
      go_back_n_socket.currOffset -= 1
    
    go_back_n_socket.goBackNOffsetMasterImpl300VarName = go_back_n_socket.currOffset

    return msg
  
  def getMsgID(self, msg):
    return msg[0 : self.headerSize]


