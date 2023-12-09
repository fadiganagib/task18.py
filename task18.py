import socket
from getpass import getpass
from netmiko import ConnectHandler

username = 'prne'
password = getpass('Enter your password:')

# Create a socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local address of the socket
address = socket.getsockname()
print('local address:', address)
# Create TCP sockets for both routers
router1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Replace the IP addresses with the desired ones
router1_ip = "192.168.56.101"
router2_ip = "192.168.56.130"
router2_port = 80

# Connect router1 to router2
router1_socket.connect((router2_ip, router2_port))

# Send data from router1 to router2
data = "Hello from router1!".encode("utf-8")
router1_socket.sendall(data)

# Receive data from router2 to router1
received_data = router2_socket.recv(1024).decode("utf-8")
print("Received data from router2:", received_data)

# Close connections
router1_socket.close()
router2_socket.close()