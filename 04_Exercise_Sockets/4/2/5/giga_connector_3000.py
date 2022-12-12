#tcp client

from socket import *
from threading import Thread
from struct import unpack, pack

class TcpClient(Thread):
    def __init__(self, server_port):
        Thread.__init__(self)
        self.server_port = server_port
        self.message = 'ECHO from TCP'

    def run(self):
        
        tcp_client = socket(AF_INET, SOCK_STREAM)
        tcp_client.connect(('localhost', self.server_port))

        #sending host format
        tcp_client.send(self.message.encode('utf-8'))
        check = tcp_client.recv(1024)
        print('From Server:', check.decode('utf-8'))

        tcp_client.close()