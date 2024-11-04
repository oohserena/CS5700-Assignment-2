import unittest
from unittest.mock import patch, MagicMock
import socket
import time

class TestUDPPingClient(unittest.TestCase):
    
    @patch('socket.socket')
    def test_successful_ping(self, mock_socket):
        
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.recvfrom.return_value = (b'PING 0 Mon Nov  3 12:00:00 2024', ('127.0.0.1', 12000))

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('127.0.0.1', 12000)

        print("\n[Test Successful Ping] Sending message to server...")
        message = 'Ping 0 ' + time.ctime(time.time())
        client_socket.sendto(message.encode('utf-8'), server_address)

        data, server = client_socket.recvfrom(4096)
        print(f"[Test Successful Ping] Received data: {data.decode('utf-8')}")
        self.assertEqual(data.decode('utf-8'), "PING 0 Mon Nov  3 12:00:00 2024")

    @patch('socket.socket')
    def test_packet_loss_simulation(self, mock_socket):

        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.recvfrom.side_effect = [socket.timeout] * 5 + [(b'PING 0 Mon Nov  3 12:00:00 2024', ('127.0.0.1', 12000))]

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(2) 
        server_address = ('127.0.0.1', 12000)

        timeouts = 0
        successful_response = False
        for i in range(6):
            try:
                print(f"[Test Packet Loss] Attempt {i+1}: Sending message to server...")
                message = 'Ping ' + str(i) + " " + time.ctime(time.time())
                client_socket.sendto(message.encode('utf-8'), server_address)
                data, server = client_socket.recvfrom(4096)
                print(f"[Test Packet Loss] Received data: {data.decode('utf-8')}")
                successful_response = True
                break
            except socket.timeout:
                print(f"[Test Packet Loss] Attempt {i+1}: Timeout occurred.")
                timeouts += 1

        print(f"[Test Packet Loss] Total timeouts: {timeouts}")
        self.assertEqual(timeouts, 5)
        self.assertTrue(successful_response)

    @patch('socket.socket')
    def test_timeout_handling(self, mock_socket):
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.recvfrom.side_effect = socket.timeout

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(2)  # Set 2-second timeout
        server_address = ('127.0.0.1', 12000)

        print("\n[Test Timeout Handling] Sending message to server and expecting timeout...")
        with self.assertRaises(socket.timeout):
            message = 'Ping 0 ' + time.ctime(time.time())
            client_socket.sendto(message.encode('utf-8'), server_address)
            client_socket.recvfrom(4096)
        print("[Test Timeout Handling] Timeout confirmed.")

    @patch('socket.socket')
    def test_server_always_responds(self, mock_socket):
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.recvfrom.return_value = (b'PING 0 Mon Nov  3 12:00:00 2024', ('127.0.0.1', 12000))

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(2)  
        server_address = ('127.0.0.1', 12000)

        for i in range(10):
            message = 'Ping ' + str(i) + " " + time.ctime(time.time())
            print(f"\n[Test Server Always Responds] Sending Ping {i} to server...")
            client_socket.sendto(message.encode('utf-8'), server_address)
            data, server = client_socket.recvfrom(4096)
            print(f"[Test Server Always Responds] Received data: {data.decode('utf-8')}")
            self.assertEqual(data.decode('utf-8'), 'PING 0 Mon Nov  3 12:00:00 2024')

if __name__ == '__main__':
    unittest.main()
