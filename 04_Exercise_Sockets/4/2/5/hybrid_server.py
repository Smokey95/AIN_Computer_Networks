#impl of a python server that can calculate with the operators +,-,*,/ and ^ (power)
from socket import *
from threading import Thread
from struct import unpack, pack
import time


class HybridServer(Thread):
    def __init__(self, server_port):
        Thread.__init__(self)
        self.server_port = server_port
        self.tdp_socket = socket(AF_INET, SOCK_STREAM)
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.tdp_socket.bind(('localhost', self.server_port))
        self.udp_socket.bind(('localhost', self.server_port))
        self.tdp_socket.listen(1)
        self.calculation_params = None
        self.result = 0
        print("The server is ready to receive")


    def run_udp(self):      
        while True:
            message, clientAddress = self.udp_socket.recvfrom(2048)
            print('Server received format: ', message.decode('utf-8'))
            self.udp_socket.sendto('ok'.encode('utf-8'), clientAddress)

            break


    def run_tcp(self):
        while True:
            connectionSocket, addr = self.tdp_socket.accept()
            msg = connectionSocket.recv(1024)
            print('Server received format: ', msg.decode('utf-8'))
            
            connectionSocket.send('ok'.encode('utf-8'))
            connectionSocket.close()
            
            #terminate on keyboard interrupt
            break


    def run(self):
        #create two threads that run the run_tcp and run_udp methods
        print('Starting udp thread')
        udp_thread = Thread(target=self.run_udp)
        udp_thread.start()

        print('Starting tcp thread')
        tcp_thread = Thread(target=self.run_tcp)
        tcp_thread.start()

        udp_thread.join()
        tcp_thread.join()
    
    
    