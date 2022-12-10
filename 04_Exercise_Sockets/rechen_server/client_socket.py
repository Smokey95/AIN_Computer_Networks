from socket import *
from threading import Thread

class client_socket(Thread):
    def __init__(self, server_port):
        Thread.__init__(self)
        self.server_port = server_port

    def run(self):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(('localhost', self.server_port))
        sentence = 'Input lowercase sentence'.encode('utf-8')
        clientSocket.send(sentence)
        modifiedSentence = clientSocket.recv(1024)

        print('From Server: ', modifiedSentence)
        clientSocket.close()