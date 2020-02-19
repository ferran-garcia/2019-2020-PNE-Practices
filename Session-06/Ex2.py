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

def print_seqs(seq_list):
    for e in range(len(seq_list)):
        print("Sequence", e, ": (Length:",  seq_list[e].len(), ")",  seq_list[e])


print_seqs([Seq("ACT"), Seq("GATA"), Seq("CAGATA")])

