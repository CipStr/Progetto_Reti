# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:16:25 2021

@author: User
"""
import socket
import dataCollection as dc
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
bufferSize = 4096

def checkIp(ip):
    splitted_ip = host_ip.split(".")
    if len(splitted_ip) != 4 or splitted_ip[0]+ splitted_ip[1] + splitted_ip[2] != '1921681':
        print("Not a class C Ip address")
        return False
    else:
        try:
            socket.sendto(("Dev-" + ip).encode("utf-8"), server_address)
            print("Size of transmission buffer: %d" %bufferSize)
            data, server = socket.recvfrom(bufferSize)
            if data.decode("utf-8") == "ACK":
                print('Received ACK from gateway, now using IP: %s' % ip)
                return True
            else:
                print("Something went wrong. Try using a different IP address")
                return False
        except Exception as info :
            print(info)
            return False
            
print("Starting device...")
while True:
    host_ip = ''
    print("Insert IP address for this device: ")
    host_ip = input()
    if checkIp(str(host_ip)):
        break;


while True:
    time.sleep(10)
    try:
        now = time.time()
        file = open("Device" + host_ip.replace(".", "_") + ".txt", "w+")
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