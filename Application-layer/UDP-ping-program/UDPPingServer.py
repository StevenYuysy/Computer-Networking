import time
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, addr = serverSocket.recvfrom(2048)
    modifiedMessage = time.asctime() + 'pong'
    serverSocket.sendto(modifiedMessage.encode(), addr)
