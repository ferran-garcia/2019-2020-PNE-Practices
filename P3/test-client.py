from Client0 import Client
IP = "127.0.0.1"
PORT = 8088
c = Client(IP, PORT)
list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print(f"Connection to SERVER at {IP}, PORT: {PORT}")
print("*Testing PING...")
print(c.talk("PING"))
print("*Testing GET...")
print("GET 0: ", c.talk("GET 0"))
print("GET 1: ", c.talk('GET 1'))
print("GET 2: ", c.talk('GET 2'))
print("GET 3: ", c.talk('GET 3'))
print("GET 4: ", c.talk('GET 4'))
print("*Testing INFO...")
print(c.talk("INFO ATCCGTA"))
print("*Testing COMP...")
print(c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"))
print("*Testing REV...")
print(c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"))
print("*Testing GENE...")
print("GENE: U5")
print(c.talk("GENE U5"))
print("GENE: ADA")
print(c.talk("GENE ADA"))
print("GENE: FRAT1")
print(c.talk("GENE FRAT1"))
print("GENE: FXN")
print(c.talk("GENE FXN"))
print("GENE: RNU_269P")
print(c.talk("GENE RNU_269P"))


