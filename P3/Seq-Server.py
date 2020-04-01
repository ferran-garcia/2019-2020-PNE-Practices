import socket
import termcolor
from Seq1 import Seq

list_genes = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
bases = ["A", "C", "T", "G"]
folder = "../Session-04/"
ext = ".txt"
IP = "127.0.0.1"
PORT = 8080
# -- Step 1: Create a socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind socket to server's IP adress and port
ls.bind((IP, PORT))

# -- Step 3: Convert into a listening socket
ls.listen()

print("El server ta ativo")

while True:

    # -- Wait for client to connect

    try:
        (cs, client_ip_port) = ls.accept()


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
    comps = msg.split(" ")
    if len(comps) >= 2:
        comp1 = comps[0]
        comp2 = comps[1]
    else:
        comp1 = msg
    if comp1 == "PING":
        termcolor.cprint("PING command!", 'green')
        print("OK!")
        response = "OK!\n"
    if comp1 == "GET":
        for e in range(len(list_genes)):
            if e == int(comp2):
                termcolor.cprint("GET", 'green')
                response = list_genes[e] + "\n"
                print(list_genes[e])
    if comp1 == "INFO":
        seq0 = Seq(comp2)
        response = ""
        termcolor.cprint("INFO", 'green')
        print(f"Sequence: {comp2}")
        response += f"Sequence: {comp2}" + "\n"
        print(f"Total length: {seq0.len()}")
        response += f"Total length: {seq0.len()}" + "\n"
        for e in bases:
            print(f"{e} : {seq0.count_base(e)} ({round(seq0.count_base(e)*(100/seq0.len()), 2)}%)")
            response += f"{e} : {seq0.count_base(e)} ({round(seq0.count_base(e)*(100/seq0.len()), 2)}%)" + "\n"
    if comp1 == "COMP":
        response = ''
        response += f"COMP {comp2}" + "\n"
        seq0 = Seq(comp2)
        termcolor.cprint("COMP", 'green')
        print(seq0.complement())
        response += seq0.complement() + "\n"
    if comp1 == "REV":
        response = ""
        response += f"REV {comp2}" + "\n"
        seq0 = Seq(comp2)
        termcolor.cprint("REV", 'green')
        print(seq0.reverse())
        response += seq0.reverse() + "\n"
    if comp1 == "GENE":
        response += f"GENE {comp2}" + "\n"
        seq0 = Seq("")
        seq0 = str(seq0.read_fasta(folder+comp2+ext))
        termcolor.cprint("GENE", 'green')
        print(seq0)
        response += seq0 + "\n"


    cs.send(response.encode())


    # -- Close the socket


    cs.close()