"""
Script, that sends a message via UDP
"""
import socket
import time 

#server IP and Port
ip = "127.0.0.1"
port = 5000
msg = "hello world"

#create a datagram socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send message
sock.sendto(bytes(msg,"utf-8"),(ip,port))
print("send: "+msg)

#receive response
response, addr = sock.recvfrom(1024)
print("received echo: " + str(response))

sock.close()