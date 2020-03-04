from Client0 import Client

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
t = ""
print("*Testing PING...")
print(c.talk("PING"))
print("*Testing GET...")
print(c.talk("GET 0"))
print(c.talk("GET 1"))
print(c.talk("GET 2"))
print(c.talk("GET 3"))
print(c.talk("GET 4"))