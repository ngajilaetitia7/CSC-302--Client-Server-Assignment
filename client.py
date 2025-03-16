import socket

# Define server address and port
HOST = '127.0.0.1'  # Must match the server's address
PORT = 12345        # Must match the server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive data from the server
message = client_socket.recv(1024).decode()
print(f"Server says: {message}")

# Close the connection
client_socket.close()
