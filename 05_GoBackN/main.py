import socket
from threading import Thread
import random
from time import sleep

from go_back_n_socket import go_back_n_socket

if __name__ == '__main__':
  
  print('MAIN INFO | Starting main.py')
  sleep(0.1)
  
  # Create a server socket
  # Server Port:    12000
  # Remote Port:    12001
  # Remote Address: localhost
  # Server should be listening after creation (see lossy_udp_socket.py Thread initialization)
  serverSocket = go_back_n_socket(12000, 12001, '127.0.0.1')
  
  # Create a client socket
  # Local Port:     12001
  # Remote Port:    12000
  # Remote Address: localhost
  clientSocket = go_back_n_socket(12001, 12000, '127.0.0.69')
  
  # Send msg to server
  clientSocket.send('Hello World')
  
  # Wait for server to receive msg
  sleep(1)
  
  # Terminate sockets
  print('MAIN INFO | Terminating sockets')
  serverSocket.sock.stop()
  clientSocket.sock.stop()