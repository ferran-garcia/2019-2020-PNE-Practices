from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.253.129"
PORT = 8099
FOLDER = "../Session-04/"
txt = ".txt"
gene = "U5"
file_name = FOLDER + gene + txt
s0 = Seq('')
s0 = str(s0.read_fasta(file_name))
c = Client(IP, PORT)
c.debug_talk(f"Sending {gene} to the server")
c.debug_talk(s0)