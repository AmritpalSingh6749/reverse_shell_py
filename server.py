#! /usr/bin/python3
# This code is about creating a listener on a specific port.
# It is expected that you have basic knowledge about ip and port
import socket
import sys

port = 8080
# Creating socketm AF_INET=> IPv4, AF_INET6=>IPv6, SOCK_STREAM=>TCP, SOCK_DGRAM=>UDP
sock_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectSocket(host):
	print("# Binding  to port : "+host+" : "+str(port))
	try:
		# Binding Host and port with socket
		sock_s.bind((host,port))
	except:
		print("\n Unable to bind.... check input given :\n Exiting")
		return
	# Listening to max 1 connection, to listen to multiple connections parallel process need to be created using threading 
	sock_s.listen(1)
	# Accepting Socket, Host and Port of remote system
	sock_c, addr = sock_s.accept()
	print("\n # Connected to host:port : "+str(addr[0])+" : "+str(addr[1]))
	msgClient(sock_c)
	sock_c.close()
	sock_s.close()

def msgClient(conn):
	print("\n # Type commands : ")
	while True:
		msg=input("remote_connection >")
		if(msg=="exit"):
			# Commanding the remote system to exit and closing sockets of both sides
			conn.send(msg.encode())
			return
		if(len(msg)>0):
			# Encoding data to bytes
			conn.send(msg.encode())
			# Accepting 1 mb of data
			rply=conn.recv(1048576)
			rply=rply.decode()
			print(rply)
		else:
			print("\n # Type exit to close connection : ")
def usage():
	print("\nsyntax:- ./Server.py 'ip'\n\teg. ./Server.py 127.0.0.1 \nExiting")
	return

def main():
	try:
		host=sys.argv[1]
		connectSocket(host)
	except:
		usage()
main()
