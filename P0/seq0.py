from pathlib import Path

def seq_ping():
    print("OK!")

def seq_read_fasta(filename):
    file_lines = Path(filename).read_text()
    body = file_lines.split("\n")
    body = body[1:]
    final_str = ''.join(body)
    return(final_str)

def seq_len(seq):
    return(len(seq))

def seq_count_base(seq, base):
    counter = 0
    for e in seq:
        if e in base:
            counter += 1
    return counter

def seq_count(seq):
    bases = ["A", "C", "T", "G"]
    times = []
    for e in bases:
        times.append(seq_count_base(seq, e))
    dict_fin = dict(zip(bases, times))
    return(dict_fin)

def seq_reverse(seq):
    rev_seq = ''
    for e in seq[::-1]:
        rev_seq += e
    return(rev_seq)

def seq_complement(seq):
    bases = ["A", "C", "T", "G"]
    bases_comp = ["T", "G", "A", "C"]
    comp_seq = ""
    dict_comp = dict(zip(bases, bases_comp))
    for e in seq:
        for i,t in dict_comp.items():
            if e == i:
                comp_seq += t
    return(comp_seq)








