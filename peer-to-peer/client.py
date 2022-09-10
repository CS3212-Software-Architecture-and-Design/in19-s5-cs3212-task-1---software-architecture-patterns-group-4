from nis import match
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

    def startProtocol(self):
        self.transport.write("ready".encode('utf_8'), self.id)

    def messageClients(self):
        print("Select option 1 or 2 to send message")
        while True:
            print("Select option 1 or 2 to send message")
            time.sleep(0.5)
            print("1 - message to peer clients")
            print("2 - message to new client")
            try:
                option = int(input("Enter your option: "))
                if (option not in (1, 2)):
                    print("Invalid input")
                elif option == 1:
                    if not self.clientList:
                        print("No peers")
                    else:
                        print("Select a host from\n",
                              ' '.join(self.clientList))
                        self.addressToSendMsg = input(
                            "host:"), int(input("port:"))
                        self.send_message()

                elif option == 2:
                    self.addressToSendMsg = input("host:"), int(input("port:"))
                    self.send_message()
                    if(self.addressToSendMsg not in self.clientList):
                        self.clientList.append(self.addressToSendMsg)
                        time.sleep(0.5)

            except:
                print("Exception")
                time.sleep(1)

    def datagramReceived(self, datagram, senderAddress):
        datagram = datagram.decode('utf-8')
        if(datagram == "ready"):
            reactor.callInThread(self.messageClients)
        else:
            print("\nMessage received....")
            print("From", senderAddress, "::", datagram, "\n")
            if(senderAddress not in self.clientList):
                self.clientList.append(senderAddress)
            time.sleep(0.5)

    def send_message(self):
        message = input(":::")
        self.transport.write(message.encode('utf-8'), self.addressToSendMsg)
        print(":::Message sent:::")
        time.sleep(1)
        return


if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client(port))
    reactor.run()
