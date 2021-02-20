import time
from socket import *
clientSock = socket(AF_INET, SOCK_DGRAM)
clientSock.settimeout(1.0)
msg = 'ping'
addr = ("localhost", 12000)
for i in range(1,11):
    start = time.time()
    clientSock.sendto(msg.encode(), addr)
    try:
        response, server = clientSock.recvfrom(1024)
        end = time.time()
        RTT = end - start

        print('#%d'%i)
        print('Response :%s'%response)
        print('RTT:%fsec'%RTT)
    except timeout:
        print('#%d'%i)
        print('Request timed out')
