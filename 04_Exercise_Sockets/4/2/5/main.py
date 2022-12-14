from hybrid_server import HybridServer
from mega_connector_3000 import UdpClient
from giga_connector_3000 import TcpClient

if __name__ == '__main__':
    server = HybridServer(50000)
    server.start()

    udp_client = UdpClient(50000)
    udp_client.start()

    tcp_client = TcpClient(50000)
    tcp_client.start()