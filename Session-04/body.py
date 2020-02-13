from pathlib import Path

file_name = "U5.txt"
file_lines = Path(file_name).read_text()
body = file_lines.split("\n")
body = body[1:]
final_str = ''
for e in body:
    final_str += e
    final_str += "\n"
print("Body of the U5.txt file:\n", final_str)


