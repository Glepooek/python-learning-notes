import socket
from logger import Logger


class Server(object):
    """
    服务器
    """

    def __init__(self):
        self.server_socket = socket.socket()
        # 获取主机名
        self.host = socket.gethostname()
        self.port = 11010
        self.server_socket.bind((self.host, self.port))
        # 监听，参数为允许排队的连接数
        self.server_socket.listen(5)

    def accept(self):
        try:
            while True:
                client, addr = self.server_socket.accept()
                if client:
                    client.send(bytes('hello', encoding='gb2312'))
                    break
        except Exception as e:
            Logger.debug(e)


class Client(object):
    """
    客户端
    """

    def __init__(self):
        self.client_socket = socket.socket()
        self.host = socket.gethostname()
        self.port = 11010
        self.data = None

    def connect(self):
        self.client_socket.connect((self.host, self.port))

    def receive(self):
        try:
            while True:
                if self.client_socket:
                    self.data = self.client_socket.recv(1024)
                if self.data:
                    return self.data
        except Exception as e:
            Logger.debug(e)


if __name__ == '__main__':
    server = Server()
    client = Client()

    client.connect()
    server.accept()

    print(client.receive())
