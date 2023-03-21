from socket import *
from datetime import datetime
from time import sleep, time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print('W0463123')
print('Dawson Davis')



# THE MODIFIED SENTENCE IS THE OUTPUT FROM THE CLIENT SENDING IT THE SENTENCE

sentence = 'HELO'
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
commandFromServer = clientSocket.recv(1024)
print('From Server: ', commandFromServer)

sentence = 'REQTIME'
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
commandFromServer = clientSocket.recv(1024)
print('From Server: ', commandFromServer)

sentence = 'REQDATE'
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
commandFromServer = clientSocket.recv(1024)
print('From Server: ', commandFromServer)

sentence = 'ECHO'
echoText = 'this is echo text'
clientSocket.send(sentence.encode())
clientSocket.send(echoText.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
commandFromServer = clientSocket.recv(1024)
print('From Server: ', commandFromServer)

sentence = 'REQIP'
clientSocket.send(sentence.encode())
clientIp = clientSocket.recv(1024)
print('From Server: ', clientIp.decode())
commandFromServer = clientSocket.recv(1024)
print('From Server: ', commandFromServer)

sentence = 'BYE'
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
