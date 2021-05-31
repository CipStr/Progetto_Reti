# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:16:25 2021

@author: User
"""
import socket
import dataCollection as dc
import time

#Assegnamento di un particolare indirizzo di Classe C al device
host_ip = '192.168.1.1'
#Creazione del socket di tipo UDP, IPv4
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
bufferSize = 4096

while True:
    #Attesa di qualche secondo prima di inviare i dati. Simula l'invio giornaliero richiesto dalla consegna
    time.sleep(10)
    try:
        #Apertura(ed eventuale creazione) di un file per salvare i dati campionati dal dispositivo
        file = open("Device_1.txt", "w+")
        file.write(dc.generateDatagram(dc.collectData(), host_ip))
        file.seek(0)
        #Teniamo traccia dell'orario al momento di invio del messaggio
        now = time.time()
        sent = socket.sendto(file.read().encode(), server_address)
        file.close()
        print("Size of transmission buffer: %d" %bufferSize)
        data, server = socket.recvfrom(bufferSize)
        print('received message "%s"' % data.decode('utf8'))
        #Calcolo del tempo impiegato per la trasmissione
        print("Transmission took %g seconds" %(time.time() - now))
    except Exception as info :
        print(info)