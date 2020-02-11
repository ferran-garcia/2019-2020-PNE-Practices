from pathlib import Path

file_name = "RNU6_269P.txt"
file_lines = Path(file_name).read_text()
first_line = file_lines.split("\n")
print("First line of the RNU6_269P.txt file: \n", first_line[0])



