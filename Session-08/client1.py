import socket

IP = "212.128.253.128"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))



# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("JAVIER THE BIONIC"))

# Closing the socket
s.close()