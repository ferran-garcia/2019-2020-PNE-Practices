def dna_counter_files(file_name):
    count_A = 0
    count_C = 0
    count_T = 0
    count_G = 0
    count_tot = 0
    f = open(file_name, 'r')
    read_info = f.read()
    chain = read_info.strip("\n")
    f.close()
    for e in chain:
        if e in "A":
            count_A += 1
            count_tot += 1
        elif e in "C":
            count_C += 1
            count_tot += 1
        elif e in "T":
            count_T += 1
            count_tot += 1
        elif e in "G":
            count_G += 1
            count_tot += 1
    print("Total length: ", count_tot)
    print("A: ", count_A)
    print("C: ", count_C)
    print("T: ", count_T)
    print("G: ", count_G)

dna_counter_files('dna.txt')
