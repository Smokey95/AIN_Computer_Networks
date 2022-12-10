#impl of a python server that can calculate with the operators +,-,*,/ and ^ (power)
from socket import *
from threading import Thread

server_port = 12000


class server_socket(Thread):
    def __init__(self, server_port):
        Thread.__init__(self)
        self.server_port = server_port
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('', server_port))
        self.serverSocket.listen(1)
        print("The server is ready to receive")

    def run(self):
        while True:
            connectionSocket, addr = self.serverSocket.accept()

            sentence = connectionSocket.recv(1024)
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence)

            connectionSocket.close()
