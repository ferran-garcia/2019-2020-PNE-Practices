from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.253.129"
PORT = 8099
c = Client(IP, PORT)
print("Sending a message to the server...")
response = c.talk("Testing !!!")
print(f"Response: {response}")
