from typing import Dict

from Seq1 import Seq

bases = ["A", "C", "T", "G"]
list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P" ]
txt = ".txt"
FOLDER = "../Session-04/"


for e in list_of_genes:
    s0 = Seq('')
    val = 0
    base = ''
    s0 = s0.read_fasta(FOLDER+e+txt)
    dict1 = s0.count()
    for i, t in dict1.items():
        while t > val:
            val = t
            base = i
    print("Gene ", e, " : Most frequent base: ", base)