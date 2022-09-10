from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint
import time


class Client(DatagramProtocol):

    def __init__(self, port):
        host = "127.0.0.1"
        self.id = host, port
        self.addressToSendMsg = None
        self.clientList = []
        print('my address:', self.id, " Ready to send and recieve")
        time.sleep(1)
        

    def send_message(self):
        message = input(":::")
        self.transport.write(message.encode('utf-8'), self.addressToSendMsg)
        print(":::Message sent:::")
        return

if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client(port))
    reactor.run()
