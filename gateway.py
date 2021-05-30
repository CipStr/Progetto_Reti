# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:27:57 2021

@author: User
"""
import socket as sk
import sys
import time

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
surveys = {}
bufferSizeCloud = 1024
bufferSizeDevice = 4096

gateway_ip = '10.10.10.1'

def generateHeader():
    header = gateway_ip
    for element in surveys.keys():
        header = header + '%' + element + '-' + surveys[element]
    return header
        
def sendToCloud(header):
    try:
        clientsocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        clientsocket.connect(('localhost',8080))
        now = time.time()
    except Exception as data:
        print (Exception,":",data)
        print ("Connection Failed\r\n")
        sys.exit(0)
    clientsocket.send(header.encode())
    print("Size of transmission buffer: %d" %bufferSizeCloud)
    response = clientsocket.recv(bufferSizeCloud)
    print (response)
    print("Transmission took %g seconds" %(time.time() - now))
    clientsocket.close()

server_address = ('localhost', 10000) 
print ('\n\r starting up on %s port %s' % server_address)
sock.bind(server_address)
 
while True:
    print('\n\r waiting to receive message...')
    print("Size of transmission buffer: %d" %bufferSizeDevice)
    data, address = sock.recvfrom(bufferSizeDevice)
    print('received %s bytes from %s' % (len(data), address))
    print (data.decode('utf8'))
    surveys[data.decode('utf8').split('-')[0]] = data.decode('utf8')[data.decode('utf8').index("-")+1:]
    print(surveys)
    if data:
        data1='ACK'
        sent = sock.sendto(data1.encode(), address)
        print ('sent %s bytes back to %s' % (sent, address))
    if (len(surveys) % 4) == 0:
        sendToCloud(generateHeader())
        surveys.clear()
         


    