from btpeer import *
"""
BTPeer
    addhandler
    addpeer
    https://git-scm.com/download/win
    http://twistedmatrix.com/Releases/Twisted/15.5/Twisted-15.5.0.tar.bz2
    http://www.rarlab.com/rar/winrar-x64-531.exe
    https://twistedmatrix.com/trac/
    https://github.com/pyca/pyopenssl
    https://pypi.python.org/packages/2.7/z/zope.interface/zope.interface-4.1.3.win32-py2.7.exe#md5=e0a5bbc762126157b63d0233e26cc751
    https://pypi.python.org/packages/2.7/p/pypiwin32/pypiwin32-219.win32-py2.7.exe#md5=bb89d94a26197a467b27f9de2b24a344
"""

def routing_function():
	print "running function"

peerid = "0"
host = "'104.236.51.232'"
serverHost = ""
port = "62"
maxconnections = "5"

#create socket for localmachine
print "\nCreate local server"
a = BTPeer(maxconnections,port,peerid,host); print vars(a)

print "\nServerIP: " + a.serverhost



print "\nCreate server socket"
server = a.makeserversocket(a.serverport);


running = True; print "\nRunning main loop"
while running == True:       
        list = a.getpeerids
        print vars(list)
        print BTPeer.checklivepeers(a)
        #print "\nStart mainLoop: " + a.mainloop()
        input = raw_input("Press <y> to quit.")
        if input is "y": break

server.close()
