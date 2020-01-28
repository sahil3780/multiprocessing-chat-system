import socket 
import select 
import sys 

  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print "Correct usage: script, IP address, port number"
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 
  
while True: 
  
            message = server.recv(2048) 
            print message 
        else: 
            message = "Client2 >"+sys.stdin.readline() 
            server.send(message) 
            
server.close() 
