import socket
from threading import Thread
import random

from lossy_udp_socket import lossy_udp_socket

class go_back_n_socket():
  
  def __init__(self, localPort, remotePort, remoteAddress):
    self.localPort = localPort
    self.remotePort = remotePort
    self.remoteAddress = remoteAddress
    self.sock = lossy_udp_socket(self, localPort, (remoteAddress, remotePort), 1)

  def send(self, msg):
    print('[Socket] Sending message: ', msg)
    self.sock.send(msg.encode('utf-8'))
    
  def receive(self, packet):
    msg = packet.decode('utf-8')
    print('[Socket] Received message: ', msg)
    return msg
