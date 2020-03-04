from Client0 import Client

IP = "212.128.253.129"
PORT = 8080
c = Client(IP, PORT)
talk = 'Message'

for e in range(5):
    talk += str(e)
    c.debug_talk(talk)
    talk = "Message"
