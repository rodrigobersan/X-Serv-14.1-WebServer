#!/usr/bin/python
import socket
import random

MyPort=1234
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', MyPort))

mySocket.listen(5)

while True:
	print '	Waiting for connections'
	(recvSocket, address) = mySocket.accept()
	print '	HTTP request recived:'
	request = recvSocket.recv(1024)
	print request


	slots = request.split('\n')
	IP = slots[1].split(':')[1]
	Puerto = slots[1].split(':')[-1]

	NextExt = str(random.randint(0,100000))
	NextURL = "http://localhost:" + str(MyPort) + "/" + NextExt
	Msg = "Hola. Eres la IP" + IP + " de este puerto " + Puerto

	recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + "<html><body>" + Msg + "</body></html>" + "\r\n")
	recvSocket.close()
