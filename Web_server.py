
from socket import *

portNum=6789
serverSocket = socket(AF_INET, SOCK_STREAM)


serverSocket.bind(('', portNum))
print ("socket binded to %s" %(portNum))
serverSocket.listen(1)
print ("socket is listening")
print ('the web server is up on port:', portNum)


while True:

	print ('Ready to serve...')

	# Set up a new connection from the client
	connectionSocket, addr =serverSocket.accept()

	try:

		message =connectionSocket.recv(1024)

		filename = message.split()[1]

		f = open(filename[1:])

		outputdata =f.read()
		print (outputdata)

		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except IOError:

		connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())

		connectionSocket.close()

serverSocket.close()
