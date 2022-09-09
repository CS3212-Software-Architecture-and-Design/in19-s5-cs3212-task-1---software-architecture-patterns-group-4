from twisted.internet.protocol import DatagramProtocol

class Client(DatagramProtocol):

    def __init__(self, host, port):
        
        
        self.id= host,port
