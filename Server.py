# This code is about creating a listener on a specific port.
# It is expected that you have basic knowledge about ip and port
import socket     # to create the socket to listen to incoming connection 
import sys        # To execute command on the host system
host=""
port=8080
# AF_INET is for address family ipv4, to use ipv6 change it with AF_INET6
# SOCK_STREAM is to create TCP socket and SOCK_DGRAM is to create UDP socket
sock_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def connectSocket():
    # Combining socket, port, and ip to listen to connection
    print ("# Binding to port }:-) "+str(port))
    sock_s.bind((host, port))
    # How many connections u want to accept, as default i am setting it to 1
    sock_s.listen(1)
    # Accept functions returns socket and address of incomming conection
    sock_c, addr=sock_s.accept()
    print ("\n #Connection established with }:-) "+addr[0]+":"+str(addr[1]))
    talkClient(sock_c)
    # It is wise to close your connection.... you are not the only evil }:-)
    sock_c.close()
    sock_s.close()

def talkClient(conn):
  print ("\n# Enter your commands after each reply u get }:-) \n")
  # Keep alive connection till u want to exit
  while True:
    msg=input(">")
    if (msg=="quit"):
      return
    # To check if somehing is being sent or not
    if (len(msg)>0):
      conn.send(str.encode(msg)
    # How many bytes u want to receive... here it is 1024
    rply=str.decode(conn.recv(1024),"utf 8")
    print ("\n"+rply, end="")
   

def main():
  connectSocket()

main() 
