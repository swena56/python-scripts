#streaming
#create a streaming socket
import socket


#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 80
# - the normal http port
s.connect(("www.google.com", 80))

print "Streaming socket"


from inspect import getmembers
from pprint import pprint
#pprint(getmembers(s))