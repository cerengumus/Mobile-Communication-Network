import sys
import socket
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

buffer_size = 1024
print("server host : " + server_host)
print("server port : " + server_port)
print("filename : " + filename)

host_port = "%s:%s" %(server_host, server_port)
print("host_port : " + host_port)
mesg = bytes(filename, 'utf-8')

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((server_host,int(server_port)))
sock.send(mesg)
data = sock.recv(buffer_size)
sock.close()
print("data : ",data.decode("utf-8") )