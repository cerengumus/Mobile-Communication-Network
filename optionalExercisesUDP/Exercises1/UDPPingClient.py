import time
from socket import *
seq = 1
minimum_rtt = 0
maximum_rtt = 0
average_rtt = 0
packets_dropped = 0.0
total_packets = 0.0
recieve_host = '127.0.0.1'
recieve_port = 1024


remote_host = '127.0.0.1'
remote_port = 12000
number_pings = 10
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.settimeout(1.0)
serverSocket.bind((recieve_host, recieve_port))
print("UDP PING CLIENT")
def get_time():
  return int(round(time.time() * 1000))

def wait_for_response():
  global packets_dropped
  while True:
    try:
      message, address = serverSocket.recvfrom(remote_port)
      return message
    except Exception as e:
      packets_dropped = packets_dropped + 1
      return 'ERROR 522 ' + str(get_time()) + ' TIMEOUT'

def send_message(message,wait=False):
   serverSocket.sendto(message, (remote_host, remote_port))
   if wait == False:
     return
   else:
     return wait_for_response()

while seq <= number_pings:
  message = 'PING ' + str(seq) + ' ' + str(get_time())
  print("message:",message)
  recieved = send_message(message.encode('utf-8'), True)
  print("received:",recieved)
  recieved_size = len(recieved)
  if type(recieved) == bytes:
    recv = recieved.decode('utf-8')
  else:
    recv = recieved
  recieved_array = recv.split(' ')
  print(recieved_array)
  recieved_type = recieved_array[0].upper()
  recieved_seq = int(recieved_array[1])
  recieved_time = int(recieved_array[2])
  rtt = get_time() - recieved_time
  if rtt > 1000:
    continue
  if recieved_type == 'PING':
    print (str(recieved_size) + " bytes recieved from " + remote_host + ':' + str(remote_port) + ': seq=' + str(recieved_seq) + ' rtt=' + str(rtt))
    average_rtt = average_rtt + rtt
    if rtt < minimum_rtt or minimum_rtt == 0:
      minimum_rtt = rtt
    if rtt > maximum_rtt or maximum_rtt == 0:
      maximum_rtt = rtt
    seq = seq + 1
  elif recieved_type == 'ERROR':
    recieved_message = recieved_array[3]
    print (recieved)
  else:
    last = recieved
  total_packets = total_packets + 1
print("total packets",total_packets)
print("packets dropped:",packets_dropped)
print ("RTT: minimum=" + str(minimum_rtt) + " maximum=" + str(maximum_rtt) + " average=" + str(average_rtt/10))
print ("Packet Loss: " + str(packets_dropped/total_packets*100) + "%")
