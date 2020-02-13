from seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
print("DNA file: ", FILENAME)
print("The first 20 bases are: \n", seq_read_fasta(FOLDER+FILENAME)[:20])

dict = {5: 600, 6: 71, 7: 54, 8: 77, 9: 58, 10: 40, 11: 41, 12: 57, 13: 66, 14: 49, 15: 64, 16: 43, 17: 24, 18: 36,
        19: 55, 20: 36, 21: 57, 22: 26, 23: 84}

clave_mayor = max(dict.keys())

print("Clave con mayor valor: %d y su valor %d" % (clave_mayor, dict.get(clave_mayor)))