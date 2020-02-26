import socket
import termcolor
###La IP va cambiando dependiendo del terminal desde el que se ejecute
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)

    def ping(self):
        print("Ok!")

    def __str__(self):
        return(f"Connection to SERVER at {self.ip}, PORT: {self.port}")

    def talk(self, msg):
        response = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response += s.recv(2048).decode("utf-8")
        s.close()
        return(response)

    def debug_talk(self, msg):
        message = str(msg)
        response = self.talk(msg)
        print("To server:")
        termcolor.cprint(message, 'blue')
        print("From server: ")
        termcolor.cprint(response, 'green')

