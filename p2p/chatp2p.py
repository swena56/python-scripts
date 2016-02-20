import socket
import urllib #needed for other features which i didn't include here for brievity

s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.bind ( ( '', 8642 ) )

s.listen ( 1 )
while True:
   channel, details = s.accept()
   while(1):
       data= channel.recv ( 100 )
       command=data.split(" ")
       if not data:
           break
       else:
           if command[0] == "/terminate":
               channel.send("Client exit")
               channel.close()
               s.close()
               exit(1);
           elif command[0] == "/quit":
               channel.send("Client exit")
           elif command[0] == "/get-peers":
               channel.send("peer-list")
           elif command[0] == "/quit":
               channel.send("Client exit")
           else:
               print data
               str="received: "+data
               channel.send(str)
   channel.close()
