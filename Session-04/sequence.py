from pathlib import Path

file_name = "ADA.txt"
file_lines = Path(file_name).read_text()
genes = file_lines.split("\n")
genes = genes[2:]
list_to_str = ''
for e in genes:
    list_to_str += e

print("The total number of bases in the ADA.txt file is: ", len(list_to_str))

