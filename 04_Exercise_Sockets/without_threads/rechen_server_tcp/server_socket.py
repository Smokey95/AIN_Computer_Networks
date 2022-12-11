#impl of a python server that can calculate with the operators +,-,*,/ and ^ (power)
from socket import *
from threading import Thread
from struct import unpack, pack
import time

server_port = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', server_port))
serverSocket.listen(1)

calculation_params = None

print("The server is ready to receive")

def calculate_result():
    result = 0
    operation = calculation_params[1].decode('utf-8')
    num_arr = calculation_params[3:]
    if operation == 'add':
        for n in num_arr:
            result += n
        
    elif operation == 'sub':
        for n in num_arr:
            result -= n
    elif operation == 'mul':
        result = 1
        for n in num_arr:
            result *= n
    elif operation == 'div':
        result = num_arr[0]
        for n in num_arr[1:]:
            result /= n
    return result


while True:
    connectionSocket, addr = serverSocket.accept()

    format = connectionSocket.recv(1024)
    print('Server received format: ', format.decode('utf-8'))
    connectionSocket.send('ok'.encode('utf-8'))

    calc_string = connectionSocket.recv(1024)
    #unpack input with recived format
    unpacked = unpack(format.decode('utf-8'), calc_string)
    calculation_params = list(unpacked)
    print('Server received calculation: ', unpacked)
    print('Server calculating...')

    #calculation
    result = calculate_result()


    #send result in format <id><result>
    packed_result = pack('if', int(calculation_params[0]), result)
    connectionSocket.send(packed_result)

    connectionSocket.close()
    break

