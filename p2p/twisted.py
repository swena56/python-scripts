#twisted
#https://pypi.python.org/packages/source/t/twisted-dev-tools/twisted-dev-tools-0.0.2.tar.gz
from twisted.internet.protocol import Protocol

class Echo(Protocol):

    def dataReceived(self, data):
        self.transport.write(data)
