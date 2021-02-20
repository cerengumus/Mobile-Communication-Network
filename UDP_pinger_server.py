
import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(('', 12000))
print("PING SERVER")
while True:
    rand = random.randint(0, 10)
    print("random number:",rand)
    msg, addr = serverSocket.recvfrom(1024)
    msg = msg.upper()
    if rand < 4:
        continue
    serverSocket.sendto(msg, addr)

serverSocket.close()
