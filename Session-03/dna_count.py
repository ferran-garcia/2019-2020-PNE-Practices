def dna_counter(chain):
    count_A = 0
    count_C = 0
    count_T = 0
    count_G = 0
    count_tot = 0
    count_non = 0
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
        else:
            count_non += 1
            count_tot += 1
    print("Total length: ", count_tot)
    print("A: ", count_A)
    print("C: ", count_C)
    print("T: ", count_T)
    print("G: ", count_G)
    print("The nº of non correct bases is: ", count_non)

dna_counter("CATGTAGACTAGW")