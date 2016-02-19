import os
from btpeer import *
from threading import Thread
from SocketServer import ThreadingMixIn

class Template:

    def __init__(self, dict):
        self.dict = dict

    def __str__(self):
        return "Hello %(name)s. Hello %(name|upper)s!" % self

    def __getitem__(self, key):
        l = key.split("|")
        if len(l) == 1:
            return self.dict[key]
        else:
            return getattr(self, l[1])(self.dict[l[0]])

    def upper(self, s):
        return s.upper()


#print Template({"name": "Guido"})

class ClientThread(Thread):
 
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New thread started for "+ip+":"+str(port)
 
 
    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print "received data:", data
            conn.send(data)  # echo

class Listen(Thread):

    listen = True
    threads = []
    def __init__(self,socket):
        Thread.__init__(self)
        #print needs a socket as a parameter if number of parameters is 2
        self.socket = socket

    def run(self):
        print "listening socket on...localhost"
        while listen == True:
            (conn, (ip,port)) = socket.accept()
            print "[+] New thread started for "+ip+":"+str(port)
            newthread = ClientThread(ip,port)
            newthread.start()
            self.threads.append(newthread)

    def stop():
        listen = False

    def showPeers(self):
        print "\nPeer list"
        print "1)..."
        for t in self.threads:
            t.join()
        return
        
    

#--------------------------

print "\nInitializating..."

def makeclientsocket(addr,port, backlog=5 ):
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
	s.bind( ( addr, port ) )
	s.listen( backlog )
	return s

def connect():
        print "connecting"
        #conn = BTPeerConnection(0,serverHost,62)
        return

#global variables

#I need to do this entirely with sockets first before using btpeer

print "\nInitializating..."
serverHost = '104.236.51.232'
local = '0.0.0.0'
print "server host: "+serverHost


socket = makeclientsocket(62)
listen = Listen(socket)
listen.start()
#peerconn = BTPeerConnection( None, serverHost, 62, socket, debug=False )

running = True

#main loop
while running == True:
        #os.system('cls')       
        print "\n\n------------------Menu-------------------"
        print "Listening socket: "
        print "-----------------------------------------"
        print "1)Connect"
        print "2)Show Peer List"
        print "X)"
        print "9)Quit"
        print "\n"
        input = raw_input("selection:")
        if input is "1":
                connect()
        if input is "2":
                listen.showPeers()
        if input is "9":
                running = False



