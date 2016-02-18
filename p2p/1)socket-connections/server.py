#from socket import *               # Import socket module
import socket

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 6000               # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
# # Get local machine name
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection
