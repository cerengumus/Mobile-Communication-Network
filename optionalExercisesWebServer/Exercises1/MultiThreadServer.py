from socket import *
import datetime
import threading


class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024)
                if not message:
                    break
                print("message: \n", message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                print("outputdata:", outputdata)
                now = datetime.datetime.now()


                first_header = "HTTP/1.1 200 OK"
                header_info = {
                    # "Date": now.strftime("%Y-%m-%d %H:%M"),
                    "Content-Length": len(outputdata),
                    "Keep-Alive": "timeout=%d,max=%d" % (10, 100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }

                following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
                print("following_header:", following_header)
                connectionSocket.send((first_header + "\r\n"+ following_header + "\r\n\r\n").encode('utf-8'))
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode('utf-8'))
            except IOError:
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))


if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Fill in start
    serverPort = 80
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    threads = []
    # Fill in end
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print("addr:\n", addr)
        # Fill in start
        # Fill in end
        client_thread = ClientThread(connectionSocket, addr)
        client_thread.start()
        client_thread.setDaemon(True)
        threads.append(client_thread)


    serverSocket.close()