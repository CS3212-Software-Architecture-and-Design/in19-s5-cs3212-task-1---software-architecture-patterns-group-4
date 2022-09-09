from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):

    def __init__(self, port):
        # if(host == "localhost"):
        #     host = "127.0.0.1"
        host = "127.0.0.1"
        self.id = host,port
        self.address = None
        
        print('my address:', self.id)



if __name__ == '__main__':
    port = randint(1000,5000)
    reactor.listenUDP(port, Client(port))

    reactor.run()