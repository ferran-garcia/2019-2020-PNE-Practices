import socket
import termcolor

IP = "212.128.253.129"
PORT = 9005
number_connect = 0
list_ip = []
# -- Step 1: Create a socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind socket to server's IP adress and port
ls.bind((IP, PORT))

# -- Step 3: Convert into a listening socket
ls.listen()

print("El server ta ativo")

while number_connect < 5:

    # -- Wait for client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        number_connect += 1
        print("CONNECTION: {}. From the IP: {}".format(number_connect, client_ip_port))
        list_ip.append(client_ip_port)
        print("A client has connected to the server!")
    except KeyboardInterrupt:
        print("A tomar por culo")
        ls.close
        exit()

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    msg_color = termcolor.colored(msg, 'green')

    # -- Print the received message
    print(f"Received Message: {msg_color}")

    response = (f"{msg}\n")
    cs.send(response.encode())


    # -- Close the socket


    cs.close()

print("The following clients have connected to the server")
for e in range(len(list_ip)):
    print(f"Client {e}: {list_ip[e]}")