import sqlite3 as lite
import sys

con = None
con = lite.connect('btpeer.db')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Peers(Id INT, ip TEXT, port INT)")
    cur.execute("INSERT INTO Peers VALUES(1,'swena56.ddns.net',5667)")
    cur.execute("CREATE TABLE Routes(Id INT, ip TEXT, port INT)")
    #cur.execute("INSERT INTO Routes VALUES(1,'swena56.ddns.net',5667)")
    
   
