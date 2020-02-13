from seq0 import *

bases = ["A", "C", "T", "G"]
list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P" ]
txt = ".txt"
FOLDER = "../Session-04/"
list_of_num = []

for e in list_of_genes:
    val = 0
    base = ''
    for i, t in seq_count(seq_read_fasta(FOLDER+e+txt)).items():
        while t > val:
            val = t
            base = i
    print("Gene ", e, " : Most frequent base: ", base)
