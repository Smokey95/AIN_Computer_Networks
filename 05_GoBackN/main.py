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
parser.add_argument('-L', '--lossRate', type=float, default=0.1, help='Loss Rate')
parser.add_argument('-N', '--segmentSize', type=int, default=1000, help='Segment Size')
parser.add_argument('-W', '--windowSize', type=int, default=10, help='Window Size')

parser.add_argument('-d', '--debug', action='store_true', default=False, help='Debug Mode')
parser.add_argument('-s', '--suppress', action='store_true', default=False, help='Suppress Mode')
parser.add_argument('-t', '--timeout', type=int, default=1000, help='Timeout')

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
  serverSocket = go_back_n_socket(args.serverPort , 
                                  args.clientPort, 
                                  '127.0.0.1', 
                                  PLR=args.lossRate,
                                  timeout=args.timeout,
                                  segmentSize=args.segmentSize,
                                  windowSize=args.windowSize,
                                  debugFlag=args.debug,
                                  suppressFlag=args.suppress)
  
  # Create a client socket
  # Local Port:     12001
  # Remote Port:    12000
  # Remote Address: localhost
  clientSocket = go_back_n_socket(args.clientPort, 
                                  args.serverPort, 
                                  args.clientAddress,
                                  PLR=args.lossRate,
                                  segmentSize=args.segmentSize,
                                  windowSize=args.windowSize, 
                                  timeout=args.timeout,
                                  debugFlag=args.debug,
                                  suppressFlag=args.suppress)
  
  # Send msg to server
  with open('testdata.txt', 'r') as f:
    msg = f.read(257500)
  clientSocket.send(msg)
  
  print("MAIN INFO  | Resend count SERVER: " + str(serverSocket.resendCounter))
  print("MAIN INFO  | Resend count CLIENT: " + str(clientSocket.resendCounter))
  print("MAIN INFO  | Time for sending: " + str(clientSocket.timer - clientSocket.startTimer))

  # Wait for server to receive msg
  sleep(5)
  
  # Terminate sockets
  print('MAIN INFO  | Terminating sockets')
  serverSocket.lossy_udp_sock.stop()
  clientSocket.lossy_udp_sock.stop()