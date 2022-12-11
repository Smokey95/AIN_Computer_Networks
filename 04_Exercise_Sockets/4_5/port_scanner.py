import socket
from threading import Thread
import time

Server_IP = '141.37.168.26'
Server_PORT = 500000
MESSAGE = 'hello'

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(100)
    print('Connecting to TCP server with IP ', Server_IP, ' on Port ', port)
    sock.connect((Server_IP, port))
    print('Sending message', MESSAGE)
    sock.send(MESSAGE.encode('utf-8'))
    try:
        msg=sock.recv(1024).decode('utf-8')
        print('Message received; ', msg)
    except socket.timeout:
        print('Socket timed out at',time.asctime())
    sock.close()

if __name__ == '__main__':
    # for i in range(1, 50):
    #     t=Thread(target=scan_port, args=(i,))
    #     t.start()
    scan_port(7)

