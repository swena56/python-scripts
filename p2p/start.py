#using btpeer.py

import btpeer

btp = btpeer()
   
def printme( str ):
   "This prints a passed string into this function"
   print str
   return
   

   

print "\nusing btpeer.py to construct a p2p network"
print "import btpeer.py"
print "This computer stats: "
ip = "127.0.0.1"

print "clients List"
#print the client list 

#there are different distance measurements 
#distance(a,b) = a xor b
#choord guid distance


#routing table