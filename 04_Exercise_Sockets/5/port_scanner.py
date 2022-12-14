import socket
from threading import Thread
import time

Server_IP = '141.37.168.26'
MESSAGE = 'hello'

def scan_port(port):
    
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.settimeout(10)
    
    try:
        print('Connecting to TCP server with IP ', Server_IP, ' on Port ', port)
        #tcp_client.connect((Server_IP, port))
        result = tcp_client.connect_ex((Server_IP, port))
        
        if result == 0:
            print('Connection established at',time.asctime(), 'on port', port)
        elif result == 10061:
            print('Connection refused [WinEr: 10061] at',time.asctime() , 'on port', port)
        elif result == 10060:
            print('Connection timed out at',time.asctime(), "on port", port)
        elif result == 10051:
            print('Network is unreachable at',time.asctime(), "on port", port)
        else:
            print('Unknown error at',time.asctime(), "on port", port)
        
    except socket.timeout:
        print("Connection timed out at",time.asctime(), "on port", port)
    except ConnectionRefusedError:
        print('Connection refused [WinEr: 10061] at',time.asctime() , 'on port', port)
    except socket.error:
        print('Socket error at',time.asctime(), 'on port', port)
    finally:
        tcp_client.close()

if __name__ == '__main__':
     for i in range(1, 51):
         t=Thread(target=scan_port, args=(i,))
         t.start()
    #scan_port(7)

