This project is designed to calculate the Round-Trip Time and handle cases such as packet loss and timeouts,

#Project components:
UDP_server.py:  listens for messages on port, processes them by converting the text to uppercase, and sends the message back to the client.
UDP_client.py: sends "ping" requests to the server, calculates the RTT, and handles timeouts and potential packet loss.
test_UDP_client.py: contains unit tests, including successful ping responses, handling packet loss, and managing timeout scenarios.

#Run the project
##Dependencies:
You need to install packages like socket, time, unittest, 

##Usage:
###Run the server
Run UDP_server.py. The server binds to 127.0.0.1 at port 12000
###Start the client
Run UDP_client.py in your ide
###Use the program
1. Enter a number to ping to UDP server
2. Enter 999 to exit program
 
