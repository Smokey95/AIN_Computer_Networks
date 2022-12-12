#udp client

from socket import *
from threading import Thread
from struct import unpack, pack

class UdpClient(Thread):
    def __init__(self, server_port):
        Thread.__init__(self)
        self.server_port = server_port
        self.message = 'ECHO from UDP'

    def run(self):

        client_socket = socket(AF_INET, SOCK_DGRAM)
        client_socket.connect(('localhost', self.server_port))

        #sending message to server
        print(f'Sending message from UDP')
        client_socket.sendto(self.message.encode('utf-8'), ('localhost', self.server_port))

        #receiving answer from server
        recv = client_socket.recv(2048)
        print(f'From Server: {recv.decode()}')

        client_socket.close()