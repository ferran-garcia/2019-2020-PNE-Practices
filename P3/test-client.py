from Client0 import Client
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)

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
for e in list_of_genes:
    print(f"GENE: {e}")
    print(c.talk("GENE "+ e))


