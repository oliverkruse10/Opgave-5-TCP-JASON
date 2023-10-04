from socket import *
import threading
import random
import json

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

def handleCommunication(connectionSocket, addr):
    print(f'User {addr} has connected')
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print(f'Received: {sentence}')

        try:
            sentence = json.loads(sentence)

            operation = sentence['operation']
            value1 = int(sentence['value1'])
            value2 = int(sentence['value2'])
    
            if operation == 'Add':
                result = value1 + value2
            elif operation == 'Subtract':
                result = value2 - value1
            elif operation == 'Random':
                result = random.randint(value1, value2)
            else:
                result = "Invalid operation"

        except (ValueError, KeyError, json.JSONDecodeError):
            result = "Invalid values"

        print(result)
        
        result = str(result)
        connectionSocket.send(result.encode())

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleCommunication, args=(connectionSocket, addr)).start()