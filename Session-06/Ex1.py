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

s1 = Seq("AACGT")
s2 = Seq("SDSAFGWESARDF")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
