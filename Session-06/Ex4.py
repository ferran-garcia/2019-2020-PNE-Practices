import termcolor


class Seq:
    """"A class for representing sequence objects"""

    def __init__(self, strbases):

        for e in strbases:
            if e not in ["A", "C", "T", "G"]:
                print("ERROR!!")
                self.strbases = "ERROR"
                return
        print("New sequence created!")
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    pass


class Gene(Seq):
    pass


def print_seqs_col(seq_list, colour):
    for e in range(len(seq_list)):
        termcolor.cprint(f"Sequence {e} : (Length: {seq_list[e].len()} ) {seq_list[e]}", colour)


def generate_seqs(pattern, number):
    seq_lists = []
    for e in range(1, number + 1):
        bases = e * pattern
        bases = Seq(bases)
        seq_lists.append(bases)
    return (seq_lists)


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs_col((seq_list1), 'blue')

print()
termcolor.cprint("List 2:", 'green')
print_seqs_col(seq_list2, 'green')
