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
    
    def __init__(self,socket):
        Thread.__init__(self)
        #print needs a socket as a parameter if number of parameters is 2
        self.socket = socket

    def run(self):
        print "listening socket on...localhost"
        while listen == True:
            (conn, (ip,port)) = socket.accept()
            newthread = ClientThread(ip,port)
            newthread.start()
            threads.append(newthread)

    def stop():
        listen = False
    

#--------------------------


def makeserversocket(port, backlog=5 ):
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
	s.bind( ( '104.236.51.232', port ) )
	s.listen( backlog )
	return s

def connect():
        print "connecting"
        conn = BTPeerConnection(0,serverHost,62)
        return

#global variables
threads = []
print "\nInitializating..."
serverHost = '104.236.51.232'; print "server host: "+serverHost
peer_me = BTPeer(5,62,5,serverHost)
socket = peer_me.makeserversocket(62)

listen = Listen(socket)
listen.start()
running = True

#main loop
while running == True:
        #os.system('cls')       
        print "\n\n------------------Menu-------------------"
        print "Listening socket: "
        print "-----------------------------------------"
        print "1)Connect"
        print "X)Show Peer List"
        print "X)"
        print "9)Quit"
        print "\n"
        input = raw_input("selection:")
        if input is "1":
                connect()
        if input is "9":
                running = False


for t in threads:
    t.join()
