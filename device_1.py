# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:16:25 2021

@author: User
"""
import socket
import dataCollection as dc
import time

host_ip = '192.168.1.1'
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
bufferSize = 4096

while True:
    time.sleep(10)
    try:
        now = time.time()
        file = open("Device_1.txt", "w+")
        file.write(dc.generateDatagram(dc.collectData(), host_ip))
        file.seek(0)
        sent = socket.sendto(file.read().encode(), server_address)
        file.close()
        print("Size of transmission buffer: %d" %bufferSize)
        data, server = socket.recvfrom(bufferSize)
        print('received message "%s"' % data.decode('utf8'))
        print("Transmission took %g seconds" %(time.time() - now))
    except Exception as info :
        print(info)