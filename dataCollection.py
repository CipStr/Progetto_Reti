# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:03:01 2021

@author: User
"""
import random
from datetime import datetime

#Utilizza valori pseudo-randomici per il campionamento dei dati e ritorna una lista con i valori calcolati
def collectData():
    date = datetime.now().strftime("%H:%M:%S")
    celsius = random.gauss(20,8)
    hum = random.gauss(50,15)
    dataList = [date, celsius, hum]
    return dataList

#Genera una stringa formattata nel seguente modo("IP-DataCampionamento-Temperatura-Umidità")
def generateDatagram(lista, host_ip):
    data = host_ip
    for elements in lista:
        data = data + '-' + str(elements)
    return data