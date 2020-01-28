import socket 
import select 
import sys 
#Declaring a TCP socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#checking arguments  
if len(sys.argv) != 3: 
    print "Correct usage: script, IP address, port number"
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 

#connrcting server
server.connect((IP_address, Port)) 


#starting chat  
while True: 
  
    
   
            message = server.recv(2048) 
            print message 
            message = "Client1 > "+ sys.stdin.readline() 
            server.send(message) 
server.close() 
