class Seq:
    """"A class for representing sequence objects"""
    def __init__(self, strbases):
        if strbases == '':
            print("NULL Seq created!")
            self.strbases = "NULL"
        else:
            for e in strbases:
                if e not in ["A", "C", "T", "G"]:
                    print("INVALID seq")
                    self.strbases = "ERROR"
                    return
            print("New sequence created!")
            self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        for e in self.strbases:
            if e not in ["A", "C", "T", "G"]:
                return 0
        return len(self.strbases)

    def count_base(self, base):
        count_base = 0
        if self.strbases == '':
            return 0
        else:
            for e in self.strbases:
                if e not in ["A", "C", "T", "G"]:
                    return 0
                else:
                    if e in base:
                        count_base += 1
            return count_base

    def count(self):
        count_A = 0
        count_C = 0
        count_T = 0
        count_G = 0
        counter_list = []
        bases = ["A", "C", "T", "G"]
        if self.strbases == '':
            counter_list.append(count_A)
            counter_list.append(count_C)
            counter_list.append(count_T)
            counter_list.append(count_G)
            dict1 = dict(zip(bases, counter_list))
            return dict1
        else:
            for e in self.strbases:
                if e not in bases:
                    return dict1
                else:
                    if e in bases[0]:
                        count_A += 1
                    elif e in bases[1]:
                        count_C += 1
                    elif e in bases[2]:
                        count_T += 1
                    elif e in bases[3]:
                        count_G += 1
            counter_list.append(count_A)
            counter_list.append(count_C)
            counter_list.append(count_T)
            counter_list.append(count_G)
            dict2 = dict(zip(bases, counter_list))
            return dict2

                    





    pass