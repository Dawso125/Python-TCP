from socket import *
from datetime import datetime
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('W0463123')
print('Dawson Davis')

print('The server is ready to receive')


while True:
    connectionSocket, addr = serverSocket.accept()
    print('got a connection from ', addr)
    while True:
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        
        if sentence != None:
            if sentence == 'HELO':
                print("GOT HELO")
                connectionSocket.send("Hi, pleased to meet you.".encode())
                connectionSocket.send(capitalizedSentence.encode())
                

            if sentence == 'REQTIME':
                print("Got REQTIME")
                now = datetime.now()
                currentTime = now.strftime("%H:%M:%S")
                connectionSocket.send(currentTime.encode())
                connectionSocket.send(capitalizedSentence.encode())
                
            if sentence == 'REQDATE':
                print('GOT REQDATE')
                currentDate = datetime.utcnow()
                currentDate = currentDate.strftime('%Y-%m-%d')
                connectionSocket.send(currentDate.encode())
                connectionSocket.send(capitalizedSentence.encode())
                

            if sentence == 'ECHO':
                print('GOT ECHO')
                echoText = connectionSocket.recv(1024).decode()
                connectionSocket.send(echoText.encode())
                connectionSocket.send(capitalizedSentence.encode())
                

            if sentence == 'REQIP':
                print('GOT REQIP')
                clientIp = addr[0]
                connectionSocket.send(clientIp.encode())
                connectionSocket.send(capitalizedSentence.encode())
                
            if sentence == 'BYE':
                print('GOT BYE')
                seeYa = 'See Ya Later!'
                connectionSocket.send(seeYa.encode())
                connectionSocket.send(capitalizedSentence.encode())
                exit()