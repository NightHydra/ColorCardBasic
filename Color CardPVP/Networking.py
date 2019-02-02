from socket import *

class sending():
    def __init__(self, ip):
        # Opens the socket(connection)
        self.host = ip
        self.port = 13000
        self.addr = (self.host, self.port)
        self.UDPSock = socket(AF_INET, SOCK_DGRAM)
        
        

    def send(self, data):
        # Sends parameter data to other user
        self.UDPSock.sendto(data.encode(), self.addr)
    def const_send(self, data):
        # Sends parameter data to other user
        global stop
        while stop == False:
            self.UDPSock.sendto(data.encode(), self.addr)

    def close():
        #Closes the socket
        self.UDPSock.close()
        os._exit()

class recieving():
    def __init__(self):
        # Opens your socket the recieving data
        self.host = ""
        self.port = 13000
        self.buf = 320
        self.addr = (self.host, self.port)

        self.UDPSock = socket(AF_INET, SOCK_DGRAM)
        self.UDPSock.bind(self.addr)
        
    def recieve(self, select, attack, player, other, active):
        # Function to recieve data and call function

        
        recieved = "None"
        while True:
            while len(recieved) != 2:
                (data,addr) = self.UDPSock.recvfrom(self.buf)
                
                
                recieved = data.decode()
                recieved = recieved.split()
            
            
            return recieved
            

    def connect(self):
        # Function to recieve data and call function
        recieved = None

        while recieved == None:
            (data,addr) = self.UDPSock.recvfrom(self.buf)
            recieved = data.decode()
            return(recieved)
        
        
    def exit(self):
        # Closes Socket
        self.UDPSock.close()
        os._exit()

#Sender = sending("10.20.12.65")
#Sender = sending("10.20.12.209")
#Sender = sending("10.20.12.208")


Sender = sending("192.168.40.5")
Recieve = recieving()
