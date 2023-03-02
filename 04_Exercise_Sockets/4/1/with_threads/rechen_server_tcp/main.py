from client_socket import client_socket
from server_socket import server_socket



if __name__ == '__main__':
    port = 12000

    server = server_socket(port)
    server.start()
    client = client_socket(port)
    client.start()

    server.join()
    client.join()