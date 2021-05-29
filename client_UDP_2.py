# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:19:55 2021

@author: User
"""

import socket
from datetime import datetime

def dati():

    lista = ['192.168.1.2', datetime.now().strftime("%H:%M:%S"), 32, 10]
    return lista

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

try:
    
    file = open("Prova_iot.txt", "w+")
    lista = dati()
    file.write(str(dati()))
    file.seek(0)
    sent = socket.sendto(file.read().encode(), server_address)
    file.close()
    data, server = socket.recvfrom(4096)
    print ('received message "%s"' % data.decode('utf8'))
except Exception as info :
    print(info)
finally:
    socket.close()