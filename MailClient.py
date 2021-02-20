import socket
import ssl
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

mailserver =  'smtp.gmail.com'
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((mailserver, 587))
recv = clientSocket.recv(1024)
print (recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')

command ='HELO Alice\r\n'
heloCommand = command.encode()
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print (recv1)

if recv1[:3] != '250':
    print ('250 reply not received from server.')



command = 'STARTTLS\r\n'.encode()
clientSocket.send(command)
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print ('220 reply not received from server')

#Encrypt the socket
clientSocket = ssl.wrap_socket(clientSocket)


email = (base64.b64encode('cerengumus0932@gmail.com'.encode())+ ('\r\n').encode())
password= (base64.b64encode('44761210476'.encode())+ ('\r\n').encode())

clientSocket.send('AUTH LOGIN \r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '334':
    print ('334 reply not received from server')

clientSocket.send(email)
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '334':
    print ('334 reply not received from server')

clientSocket.send(password)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '235':
    print ('235 reply not received from server')

clientSocket.send("MAIL FROM: <cerengumus0932@gmail.com>\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
if recv2[:3] != '250':
    print ('250 reply not received from server.')

clientSocket.send("RCPT TO: <cerengumus0932@gmail.com>\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
print (recv2)


clientSocket.send("DATA\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
print (recv2)

clientSocket.send(("Subject: SMTP Email Test! \r\n").encode())
clientSocket.send(("To: cerengumus0932@gmail.com \r\n").encode())
clientSocket.send(msg.encode())

clientSocket.send(endmsg.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

clientSocket.send("QUIT\r\n".encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

clientSocket.close()

print('Mail sent and connection closed')
