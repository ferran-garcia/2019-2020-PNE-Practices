from seq0 import *

list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P" ]
txt = ".txt"
FOLDER = "../Session-04/"

for e in list_of_genes:
    print("Gen", e, "--->  Length: ", seq_len(seq_read_fasta(FOLDER+e+txt)))