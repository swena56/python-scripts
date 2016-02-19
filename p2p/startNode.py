import socket
from threading import Thread
from SocketServer import ThreadingMixIn
from btpeer import *
 
class Server(Thread):
 
    def __init__(self,socket):
        Thread.__init__(self)
        (conn, (ip,port)) = socket.accept()
        self.conn = conn
        self.ip = ip
        self.port = port
        print "[+] New thread started for "+ ip+ ":"+port

    def send(self):
        print "sending message"
        self.conn.send("Message")
        
    def run(self):
        print "start"
        while True:
            data = self.conn.recv(2048)
            if not data: break
            print "received data:", data
            self.conn.send(data)  # echo

class Client(Thread):
 
    def __init__(self,socket,ip,port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port
        print "[+] New thread started for "+ ip+ ":"+str(port)
        
    def run(self):
        host = self.socket.gethostname()
        self.socket.connect((host,port))
        self.socket.recv(1024)
        self.socket.close()
       
        
class Connect(Thread):
      
    threads = []
    peers = []
    TCP_IP = ''
    TCP_PORT = 62
    peerid = 0
    def __init__(self,TCP_IP = '0.0.0.0'):
        Thread.__init__(self)
        self.TCP_IP = TCP_IP
        self.btpeer = BTPeer(5,self.TCP_PORT,None,self.TCP_IP)
        print "\nWaiting for incoming connections from "+self.TCP_IP+"\n"
 
    def run(self):
        BUFFER_SIZE = 20  # Normally 1024, but we want fast response
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind((self.TCP_IP, self.TCP_PORT))
        tcpsock.listen(10)
        self.tcpsock = tcpsock       
        if self.TCP_IP is '0.0.0.0':
            newthread = Server(self.tcpsock)
            newthread.start()
            self.threads.append(newthread)
        else:
            newthread = Client(self.tcpsock,self.TCP_IP, self.TCP_PORT)
            self.threads.append(newthread)
        

    def getConnectionLable(self):
        return self.TCP_IP + " on port " + str(self.TCP_PORT)
    
    def showPeers(self):
        self.btpeer

    def addPeer(self):
        self.btpeer
        
    def showSockets(self):
        for t in self.threads:
            t.join()

    def connect(self):
        input = raw_input("connect to what ip: ")
        print "establishing a connection to "+input
        print vars(self.btpeer)
        
            
thr = Connect()
thr.start()
peers = []
running = True
while running == True:
    print "\n------------------Menu-------------------"
    print "Listening socket: " + thr.getConnectionLable()
    print "Peers List:\n"
    for t in peers:
        print t.join()
    print "-----------------------------------------"
    print "1)Connect"
    print "2)Show Peer List"
    print "3)Add Peer"
    print "4)Add Router"
    print "5)Show Sockets"
    print "9)Quit"
    print "\n"
    input = raw_input("selection:")
    if input is "1":
            print "examples: 104.236.51.232"
            input = raw_input("connect to what ip: ")
            print "establishing a connection to "+input
            if input is "":
                input = "104.236.51.232"
            #check to make sure it is a valid ip
            newPeer = Connect('104.236.51.232')
            newPeer.start()
            peers.append(newPeer)           
    if input is "2":
            thr.showPeers()
    if input is "3":
            thr.addPeer()
    if input is "4":
            thr.addRouter()
    if input is "5":
            thr.showSockets()
    if input is "9":
            running = False
            #close all sockets

