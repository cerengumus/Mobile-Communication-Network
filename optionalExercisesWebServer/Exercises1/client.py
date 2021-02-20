from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('127.0.0.1', 80))
serverSocket.listen(5)

while True:
    # Establish connection

    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()

    try:

        message = connectionSocket.recv(1024)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)
        connectionSocket.send('HTTP/1.1 200 OK \r\n\r\n'.encode('utf-8'))

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        connectionSocket.close()

    except IOError:
        connectionSocket.send('404 File Not Found'.encode('utf-8'))
        connectionSocket.close()

serverSocket.close()