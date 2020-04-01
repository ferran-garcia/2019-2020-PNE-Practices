from Client0 import Client
list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P" ]
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)

t = ""
print("*Testing PING...")
print(c.talk("PING"))
print("*Testing GET...")
print("*Testing INFO...")
print(c.talk("INFO ATCCGTA"))
print("*Testing COMP...")
print(c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"))
print("*Testing REV...")
print(c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"))
print("*Testing GENE...")
for e in list_of_genes:
    print(c.talk("GENE "+ e))



