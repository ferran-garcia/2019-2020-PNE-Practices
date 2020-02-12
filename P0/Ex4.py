from seq0 import *

bases = ["A", "C", "T", "G"]
list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P" ]
txt = ".txt"
FOLDER = "../Session-04/"

for e in list_of_genes:
    print("Gene", e, ":")
    for i in bases:
        print( i, ":", seq_count_base(seq_read_fasta(FOLDER+e+txt), i))
