import socket
import time

Server_IP = '127.0.0.1'
Server_PORT = 50000
MESSAGE = 'Hello, World!'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
print('Connecting to TCP server with IP ', Server_IP, ' on Port ', Server_PORT)
sock.connect((Server_IP, Server_PORT))
print('Sending message', MESSAGE)
sock.send(MESSAGE.encode('utf-8'))
try:
    msg=sock.recv(1024).decode('utf-8')
    print('Message received; ', msg)
except socket.timeout:
    print('Socket timed out at',time.asctime())
sock.close()


