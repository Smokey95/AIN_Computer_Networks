import socket
import time
from threading import Thread

Server_IP = '141.37.168.26'
Server_PORT = 50000
MESSAGE = 'Hello, World!'


def scan_port(port):
    print('Sending message', MESSAGE, 'to UDP server with IP ', Server_IP, ' on Port=', Server_PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.settimeout(10)
    sock.sendto(MESSAGE.encode('utf-8'), (Server_IP, Server_PORT))
    try:
        data, addr = sock.recvfrom(1024)
        print('received message: '+data.decode('utf-8')+' from ', addr)
    except socket.timeout:
        print('Socket timed out at',time.asctime())
    sock.close()

if __name__ == '__main__':
    for i in range(1, 50):
        t=Thread(target=scan_port, args=(i,))
