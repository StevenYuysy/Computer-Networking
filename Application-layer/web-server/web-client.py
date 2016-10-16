from socket import *

# Create socket
serverName = 'localhost'
serverPort = 6789
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect((serverName, serverPort))
filename = input('The file you want to get: ')
# send HTTP request message
message = 'GET /%s HTTP/1.1\r\n \r\n' % filename
clientSocket.send(message.encode())

# explain HTTP resonse message
responseTotal = ''
while 1:
    response = clientSocket.recv(1024)
    if response:
        responseTotal += response.decode()
    else:
        break

print(responseTotal)

clientSocket.close()
