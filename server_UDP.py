# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:27:57 2021

@author: User
"""
import socket as sk

# Creiamo il socket
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# associamo il socket alla porta
rilevazioni = {}
server_address = ('localhost', 10000) 
print ('\n\r starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print('\n\r waiting to receive message...')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print (data.decode('utf8'))
    rilevazioni[data.decode('utf8').split()[0]] = data.decode('utf8')[data.decode('utf8').index(" ")+1:]
    print(rilevazioni)
    if data:
        data1='ACK'
        sent = sock.sendto(data1.encode(), address)
        print ('sent %s bytes back to %s' % (sent, address))


