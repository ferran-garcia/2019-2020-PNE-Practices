from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.253.129"
PORT = 8080
c = Client(IP, PORT)
c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")