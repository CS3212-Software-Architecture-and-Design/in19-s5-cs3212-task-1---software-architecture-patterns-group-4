from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):

    def __init__(self, port):
        host = "127.0.0.1"
        self.id = host, port
        
        self.addressToSendMsg = None
        self.addressLastSent = None
        self.addressLastReceived = None
        
        self.peers = dict()
                
        print("P2P Messanger Started @", self.id)
        print("Ready to send and Recieve \n\n")
    
    #runs when reactor.run() is called
    def startProtocol(self):
        reactor.callInThread(self.mainMenu)
    
    #gets the messsage as text input, and send it to addressToSendMsg
    def send_message(self):
        print("Sending to : ", self.addressToSendMsg)
        message = input(":::")
        self.transport.write(message.encode('utf-8'), self.addressToSendMsg)
        print(":::Message sent:::")
        self.addressLastSent = self.addressToSendMsg
        return
    
    #runs when a message is recieved    
    def datagramReceived(self, datagram, senderAddress):
        datagram = datagram.decode('utf-8')
        
        print("Message received....")
        print("From", senderAddress, "::", datagram)
        self.addNewPeer(senderAddress)
        self.addressLastReceived = senderAddress
        return
        
    def mainMenu(self):
        while True:
            
            print("P2P Messanger - Menu")
            
            print("1 - Message Last Sent Address")
            print("2 - Message Last Recieved Address")
            print("3 - Message a Saved Peer")
            print("4 - Message a New Peer")
            print("...   ----   ...")
            print("0 - Exit P2P Messanger")
            print("\n\n\n")
            
            selection = int(input("Select an option  :  "))
                    
            if (selection == 1):    self.msgLastSentAddr()
                
            elif (selection == 2):  self.msgLastRecAddr()
                
            elif (selection == 3):  self.msgSavedPeer()
                
            elif (selection == 4):  self.msgNewPeer()
                
            elif (selection == 0):  self.exitApp()
                
            else:   print("invalid input")
        
            
    def msgLastSentAddr(self):
        self.addressToSendMsg = self.addressLastSent
        self.send_message()
        
    def msgLastRecAddr(self):
        self.addressToSendMsg = self.addressLastReceived
        self.send_message()
        
    def msgSavedPeer(self):
        self.addressToSendMsg = self.selectPeer()
        self.send_message()
        
    def msgNewPeer(self):
        self.addressToSendMsg = self.getNewPeer()
        self.addNewPeer(self.addressToSendMsg)
        self.send_message()
        
    def exitApp(self):
        reactor.stop()
        exit()
    
    def selectPeer(self):
        print(self.peers)
        selected = int(input("Select a peer: "))
        return self.peers[selected]
    
    def getNewPeer(self):
        peer = input("host:"), int(input("port:"))
        return peer
    
    def addNewPeer(self, peer):
        peerSize = len(self.peers)
        #if not in the list
        self.peers[peerSize] = peer
        return
    
        
   
if __name__ == '__main__':
    port = randint(1000, 5000)
    client = Client(port)
    reactor.listenUDP(port, client)
    reactor.run()