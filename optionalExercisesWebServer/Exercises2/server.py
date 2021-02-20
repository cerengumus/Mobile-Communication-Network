from socket import *
import datetime

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6791
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	print ("addr:\n", addr)
	message = connectionSocket.recv(1024)
	if not message:
		break
	f = open(message)
	outputdata = f.read()
	print("data :",outputdata)
	output = bytes(outputdata, 'utf-8')
	connectionSocket.send(output)


connectionSocket.close()