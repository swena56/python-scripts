import socket
import threading
import SocketServer
from btpeer import *

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    
    def checkDatabase(self):       
        return

    def addPeer(self):
        return
    
    def handle(self):
        data = self.request.recv(1024)
        print data
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    conn = BTPeerConnection(2,ip,port,sock, True)
    print vars(conn)
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "0.0.0.0", 5669

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    #    client(ip, port, "Hello World 1")
    #    client(ip, port, "Hello World 2")
    #    client(ip, port, "Hello World 3")

    
    a = BTPeer(5,5670,None,'swena56.ddns.net')
    b = BTPeer(5,5670,None,'docker.me')
  
    
    #define peers
    running = True

    #main loop
    while running == True:
	#os.system('cls')       
        print "\n\n------------------Menu-------------------"
        print "Listening socket: "
        print "-----------------------------------------"
        print "1)Connect to hose"
        print "2)Show Peer List"
        print "X)"
        print "9)Quit"
        print "\n"
        input = raw_input("selection:")
        if input is "1":
                connectTo = raw_input("connect what host: ")
                if True:
                    client(connectTo,port,"message")
        if input is "2":
                print server.getMessages()
        if input is "9":
                running = False

    server.shutdown()
    server.server_close()

