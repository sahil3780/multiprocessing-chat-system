import socket 
import select 
import sys 
from thread import *

#Declaring a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

  
#Giving server ip address 
IP_address = str("0.0.0.0") 
  
#giving server port number
Port = int(250)

server.bind((IP_address, Port)) 
  
#
server.listen(100) 
#listning for hundred clients  
list_of_clients = []

#function for minimal bot
def bot(m):
    if "name" in m and "what" in m:
        text="i'm chatbot"
        return str(text)
    elif "how are you" in m:
        text="im fine How are you?"
        return str(text)
    elif "im fine How are you" in m:
        text="im good"
        return str(text)
    elif "what is this" in m:
        text="this is a multiprocessing chat system";
        return str(text)
    elif "help" in m and "Help" in m:
        text="you can ask FAQ's here"
        return str(text)
    elif "who developed you" in m:
        text="my master sahil sharma"
        return str(text)
    else:
        print "Relpy to the Client:"
        text=sys.stdin.readline()
        return str(text)



#sending and recieving replies from client


  
def clientthread(conn, addr): 
  
     
    conn.send("Welcome to this chatroom!") 
  
    while True: 
            try: 
                message = conn.recv(2048) 

                if message: 
                    print message
                    message_to_send = "Server > " + bot(message)
                    conn.send(message_to_send) 
  
                else: 
                    
                    remove(conn) 
  
            except Exception as e: 
                print e
  
#removing connection
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 


#accepting connections and creating new threads
while True: 
  
    
    conn, addr = server.accept() 
  
    
    list_of_clients.append(conn) 
  
    print addr[0] + " connected"

#starting new thread for a new client
  
    start_new_thread(clientthread,(conn,addr))     
  
conn.close() 
server.close() 
