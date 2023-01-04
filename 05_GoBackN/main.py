# -------------------------------------------------------------------------------------------------- Imports
import socket
from threading import Thread
import random
from time import sleep

from go_back_n_socket import go_back_n_socket

import argparse

# -------------------------------------------------------------------------------------------------- Argument Parser
parser = argparse.ArgumentParser(description='Go-Back-N Socket', add_help=True)
parser.add_argument('-S', '--serverPort', type=int, default=12000, help='Server Port')
parser.add_argument('-C', '--clientPort', type=int, default=12001, help='Remote Port')
parser.add_argument('-A' ,'--clientAddress', type=str, default='127.0.0.96', help='Remote Client Address')
parser.add_argument('-L', '--lossRate', type=float, default=0.0, help='Loss Rate')

parser.add_argument('-d', '--debug', action='store_true', default=False, help='Debug Mode')


# -------------------------------------------------------------------------------------------------- Main
if __name__ == '__main__':
  
  args = parser.parse_args()
  
  print('MAIN INFO  | Starting main.py')
  sleep(0.1)
  
  # Create a server socket
  # Server Port:    12000
  # Remote Port:    12001
  # Remote Address: localhost
  # Server should be listening after creation (see lossy_udp_socket.py Thread initialization)
  serverSocket = go_back_n_socket(args.serverPort , args.clientPort, '127.0.0.1', debugFlag=args.debug)
  
  # Create a client socket
  # Local Port:     12001
  # Remote Port:    12000
  # Remote Address: localhost
  clientSocket = go_back_n_socket(args.clientPort, args.serverPort, args.clientAddress, debugFlag=args.debug)
  
  # Send msg to server
  with open('testdata.txt', 'r') as f:
    msg = f.read()
  clientSocket.send(msg)
  
  # Wait for server to receive msg
  sleep(1)
  
  # Terminate sockets
  print('MAIN INFO  | Terminating sockets')
  serverSocket.sock.stop()
  clientSocket.sock.stop()