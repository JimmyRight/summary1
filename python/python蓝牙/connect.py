#--*--coding=utf-8--*--
#P191
#sudo pip install pybluez
 
import time
from bluetooth import *
def rfcommCon(addr,port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr,port))
        print "[+] RFCOMM port : " +str(port)+' open'
        sock.close()
    except Exception,e:
        print '[-] RFCOMM port :' +str(port)+' closed'
 
for port in range(1,30):
    rfcommCon('50:01:D9:B0:D5:13',port)
    print("connected.  type cp_code")
    while True:
        data = input()
        if len(data) == 0: break
        sock.send(data)
sock.close()