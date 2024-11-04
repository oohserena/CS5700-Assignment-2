import socket
import time  # Import time library
while True:
    print("\nChose one option:")
    print("  ")
    print("1. Enter a number to ping to UDP server")
    print("2. Enter 999 to exit program")
    print(" \n")

    option = input("Enter you option: ")
    if option == 999:
        break
    print("      ")
    print("Starting the program")
    print("    \n")

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket for the client
    server_address = ('127.0.0.1', 12000)  # Set IP Address and Port Number of Socket
    mysocket.settimeout(2) # Sets a timeout value 2 seconds

    try:  # Infinite loop to continuously send messages to the server
        for i in range(0, 10):
            start = time.time()  # Start time send message to server
            message = 'Ping ' + str(i) + " " + time.ctime(start)
            try:
                sent = mysocket.sendto(message.encode("utf-8"), server_address)
                print("Sent " + message)
                data, server = mysocket.recvfrom(4096)  # Maximum data received 4096 bytes
                print("Received " + str(data))
                end = time.time();
                elapsed = end - start
                print("RTT: " + str(elapsed * 1000) + " Milliseconds\n")
            except socket.timeout:
                print("#" + str(i) + " Requested Time out\n")
    finally:
        print("Finish ping, closing socket")
        mysocket.close()
