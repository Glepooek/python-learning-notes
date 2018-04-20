from twisted.internet.interfaces import IReactorTCP
from twisted.internet.protocol import Protocol, Factory


class SimpleLogger(Protocol):
    def connectionMade(self):
        print('got connection from %s' % self.transport.client)

    def connectionLost(self, reason):
        print('%s disconnected' % self.transport.client)

    def dataReceived(self, data):
        print(data)


factory = Factory()
factory.protocol = SimpleLogger
IReactorTCP.listenTCP(1234, factory)
IReactorTCP.Run()
