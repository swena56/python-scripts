import socket
import urllib

print "<<CLIENT>>\n\n"
print ">>connecting to server...\n"

print ">>Attempting to connect to Server..."
s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
CONNECT = 0
while CONNECT == 0:
    try:
        s.connect ( ( '127.0.0.1', 8642 ) )  
    except socket.error, msg:
        continue
    CONNECT = 1
    
print "\n>>Connected to server\n"
  
while (1):
    data=raw_input(">> ")
    if not data:
        break
    else:
        if(s.send(data)):
            retdata=s.recv(1000)                  
            if (retdata != "Client exit" ):
                print ">>Server: ",retdata,"\n"
            else:
                print ">>Closing connection"
                s.close()
                print ">>Connection terminated"
                exit(1);
    
s.close()
