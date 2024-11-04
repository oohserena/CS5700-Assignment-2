import socket  

serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('127.0.0.1', 12000))  
print("Started UDP Server IP Address: 127.0.0.1 and Port: 12000")  
while True:  
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()  
   
    serverSocket.sendto(message, address)  
