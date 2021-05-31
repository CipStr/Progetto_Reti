import socket as sk
import sys 

#Funzione che prende in input il messaggio in entrata 
#e lo divide secondo il carattere "%" per restituire una lista di elementi
def splitMessage(message):
    formattedMessage = message.split('%')
    return formattedMessage

#Creazione del socket di tipo TCP, IPv4
serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server_address=('localhost',8080)
serverSocket.bind(server_address)
bufferSize = 1024
serverSocket.listen(1)
print ('The Cloud is running on port:',8080)

while True:

    print ('Online, waiting for data')
    connectionSocket, addr = serverSocket.accept()
    print(connectionSocket,addr)

    try:
        print("Size of transmission buffer: %d" %bufferSize)
        message = connectionSocket.recv(bufferSize)
        #Il messaggio decodificato viene passato alla funzione per l'opportuna formattazione
        message = splitMessage(message.decode('utf8'))
        print("Received data from: %s \n" %message[0])
        for i in range(1, len(message)):
            print("Device %s : %s" %(i, message[i]))
        connectionSocket.send("Received".encode())
        connectionSocket.close()
    except Exception as message:
        print (Exception,":",message)
        print ("Connection Failed\r\n")
        sys.exit(0)

