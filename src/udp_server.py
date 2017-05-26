"""
Creates an UDP echo server, that listens to a port and returns the message to the sender
"""
import socket
import time

#ip address and port to listen
ip = "127.0.0.1"
port = 5000

# create a datagram socket and listen to the port
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))

while True:
	data, addr = sock.recvfrom(1024)
	datastr = str(data)
	#print out the message, addr is a tuple: (ip,port)
	print("received: " +datastr + " from: "+ addr[0] + ":" + str(addr[1]))

	sock.sendto(data,addr)