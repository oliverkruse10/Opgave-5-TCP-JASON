from socket import *
import json

serverName = "192.168.1.159"
serverPort = 12005
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))



operation = input('Input message:')
value1 = input('Input value1:')
value2 = input('Input value2:')
myMessage = {"operation": operation, "value1": value1, "value2": value2}
message_json = json.dumps(myMessage)  
clientSocket.send(message_json.encode()) 
#clientSocket.close()
