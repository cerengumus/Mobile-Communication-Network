
from socket import *
import time
import random

recieve_host = '127.0.0.1'
recieve_port = 12000
remote_host = '127.0.0.1'
remote_port = 1024

seq = 0
recieved_time = 0
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((recieve_host, recieve_port))

simulate_packet_loss = True
sleep_for_rand_response_times = True
print("ready to server...")

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
  res = get_time() - recieved_time
  print (res)
  if recieved_time !=0 and get_time() - recieved_time > 5000:
    print ('timeout')
    seq = 0
    recieved_time = 0
  message = message.upper()
  print("message:" ,message)
  recieved_size = len(message)
  if type(message) == bytes:
    message = message.decode('utf-8')
  recieved_array = message.split(' ')
  recieved_type = recieved_array[0].upper()
  recieved_seq = int(recieved_array[1])
  recieved_time = int(recieved_array[2])
  if recieved_seq != seq+1:
    if seq != 0:
      for i in range(seq, recieved_seq):
        print ('Dropped Packet:' + str(i))
    if seq == 0:
      print ('Client connect.')
    seq = recieved_seq
  print ('Recieve: ' + message)
  minimum_sleep = 0.2
  maximum_sleep = 1.0
  if sleep_for_rand_response_times:
    time.sleep(random.uniform(minimum_sleep, maximum_sleep))
    if simulate_packet_loss:
      if random.randint(0, 10) < 2:
        print ('Dropped')
        continue
  elif simulate_packet_loss:
    if random.randint(0, 10) < 4:
      continue
  serverSocket.sendto(message.encode('utf-8'), address)
  print ('Send: ' + message)
