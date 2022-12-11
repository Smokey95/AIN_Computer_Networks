#smpt client without smtplib
from socket import *
from base64 import *

# Choose the htwg asmtp server as mailserver and connect the client socket to it
mailserver = ("asmtp.htwg-konstanz.de", 587)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Checking if connection try has worked
recv = clientSocket.recv(1024)
print("Message after connection request:\n\t" + str(recv.decode("utf-8")) + "\n")
if recv[0:3] != b'220':
    print('220 reply not received from server.')

#sending HELO command
helo_cmd2 = b64encode('hans\r\n'.encode('utf-8'))
helo_cmd = 'HELO lb\r\n'.encode()
clientSocket.send(helo_cmd) 
recv_of_helo = clientSocket.recv(1024)
print("\nMessage after sending HELO command:\n\t" + str(recv_of_helo.decode("utf-8")) + "\n")

#sending username and pw
username = 'rnetin'
password = 'Ueben8fuer8RN'
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print("\nMessage after sending username and pw:\n\t" + str(recv_auth.decode("utf-8")) + "\n")

#sending MAIL FROM command
mail_from = 'MAIL FROM:<rnetin@htwg-konstanz.de>\r\n'.encode()
clientSocket.send(mail_from)
recv_mail = clientSocket.recv(1024)
print("\nMessage after sending MAIL FROM command:\n\t" + str(recv_mail.decode("utf-8")) + "\n")

#sending RCPT TO command
rcpt_to = 'RCPT TO:<larsbuerger1@gmail.com>\r\n'.encode()
clientSocket.send(rcpt_to)
recv_rcpt = clientSocket.recv(1024)
print("\nMessage after sending RCPT TO command:\n\t" + str(recv_rcpt.decode("utf-8")) + "\n")

#sending DATA command
data = 'DATA\r\n'.encode()
clientSocket.send(data)
recv_data = clientSocket.recv(1024)
print("\nMessage after sending DATA command:\n\t" + str(recv_data.decode("utf-8")) + "\n")

#sending message data
msg = 'Subject: Testmail\r\n.\r\n'.encode()
clientSocket.send(msg)
recv_msg = clientSocket.recv(1024)
print("\nMessage after sending message data:\n\t" + str(recv_msg.decode("utf-8")) + "\n")

#sending QUIT command
quit = 'QUIT\r\n'.encode()
clientSocket.send(quit)
recv_quit = clientSocket.recv(1024)
print("\nMessage after sending QUIT command:\n\t" + str(recv_quit.decode("utf-8")) + "\n")
