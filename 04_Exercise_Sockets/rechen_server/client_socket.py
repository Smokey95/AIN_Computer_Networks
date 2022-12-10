from socket import *
from threading import Thread
from struct import unpack, pack

class client_socket(Thread):
    def __init__(self, server_port):
        Thread.__init__(self)
        self.server_port = server_port

    def run(self):
        inp = input('Enter calculation: ')

        #parse inp string
        cutted = inp[1:-1]
        splitted_inp = cutted.split('><')

        #variables
        id          = int(splitted_inp[0])
        operation   = splitted_inp[1]
        count       = int(splitted_inp[2])
        num_arr     = list(map(int, splitted_inp[3:]))

        format = 'i' + str(len(operation)) + 'si' + str(count) + 'i'
        packed_operation = pack(format, id, operation.encode(), count, *num_arr)

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(('localhost', self.server_port))

        #sending host format
        clientSocket.send(format.encode('utf-8'))
        check = clientSocket.recv(1024)
        print('From Server: ', check.decode('utf-8'))

        #sending calculation
        operation = inp.encode('utf-8')
        clientSocket.send(packed_operation)
        calculation = clientSocket.recv(1024)

        #unpack result
        unpacked = unpack('if', calculation)
        print(f'From Server: ID: {unpacked[0]} Result: {unpacked[1]}')

        clientSocket.close()