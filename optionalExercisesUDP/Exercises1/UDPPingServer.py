import random
from socket import *
import time
recieve_host = '127.0.0.1'
recieve_port = 12000
remote_host = '127.0.0.1'
remote_port = 1024

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((recieve_host, recieve_port))

simulate_packet_loss = True
sleep_for_rand_response_times = True

def get_time():
  return int(round(time.time() * 1000))

def send_message(message,wait=False):
   serverSocket.sendto(message, (remote_host, remote_port))
   if wait == False:
     return
   else:
     return wait()

while True:
  message, address = serverSocket.recvfrom(remote_port)
  message = message.upper()
  print ('Recieve: ' , message)
  if sleep_for_rand_response_times:
    min_sleep = 0.2
    max_sleep = 1.0
    time.sleep(random.uniform(min_sleep, max_sleep))
    if simulate_packet_loss:
      if random.randint(0, 10) < 2:
        continue
  elif simulate_packet_loss:
    if random.randint(0, 10) < 4:
      continue
  serverSocket.sendto(message, address)
  print ('Send: ' , message)
