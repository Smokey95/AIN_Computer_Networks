#impl of a python server that can calculate with the operators +,-,*,/ and ^ (power)
from socket import *
from threading import Thread
from struct import unpack, pack
import time

server_port = 12000


class server_socket(Thread):
    def __init__(self, server_port):
        Thread.__init__(self)
        self.server_port = server_port
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('localhost', server_port))
        self.serverSocket.listen(1)
        self.calculation_params = None
        self.result = 0
        print("The server is ready to receive")

    def run(self):
        while True:
            connectionSocket, addr = self.serverSocket.accept()

            format = connectionSocket.recv(1024)
            print('Server received format: ', format.decode('utf-8'))
            connectionSocket.send('ok'.encode('utf-8'))

            calc_string = connectionSocket.recv(1024)
            #unpack input with recived format
            unpacked = unpack(format.decode('utf-8'), calc_string)
            self.calculation_params = list(unpacked)
            print('Server received calculation: ', unpacked)
            print('Server calculating...')

            #calculation
            self.calculate_result()


            #send result in format <id><result>
            packed_result = pack('if', int(self.calculation_params[0]), self.result)
            connectionSocket.send(packed_result)

            connectionSocket.close()
            break

    def calculate_result(self):
        id = self.calculation_params[0]
        operation = self.calculation_params[1].decode('utf-8')
        count = self.calculation_params[2]
        num_arr = self.calculation_params[3:]

        if operation == 'add':
            for n in num_arr:
                self.result += n
            
        elif operation == 'sub':
            for n in num_arr:
                self.result -= n

        elif operation == 'mul':
            self.result = 1
            for n in num_arr:
                self.result *= n

        elif operation == 'div':
            self.result = num_arr[0]
            for n in num_arr[1:]:
                self.result /= n