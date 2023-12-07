from collections import defaultdict as dd
f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\7\input")

class card:
    def __init__(self, s) -> None:
        self.hand, self.bits = s.split()
        self.bits = int(self.bits)
        self.count = dd(lambda: 0)
        self.J = 0
        for c in self.hand:
            if c == "J":
                self.J += 1
            else:
                self.count[c] += 1
        m = 0
        if self.count.values():
            m = max(self.count.values())
        
        for k in self.count.keys():
            if self.count[k] == m:
                self.count[k] += self.J
                break
        if m == 0 and self.J == 5:
            self.count["J"] = 5
        self.scor = self.score()


    def score(self):
        vals = self.count.values()
        if 5 in vals:
            return 8
        elif 4 in vals:
            return 7
        elif 3 in vals and 2 in vals:
            return 6
        elif 3 in vals:
            return 5
        elif 2 in vals:
            a = list(vals).count(2)
            if a == 2:
                return 4
            return 3
        else: 
            return 2

    def __lt__(self, other):
        if self.scor == other.scor:
            for i in range(5):
                if self.card_to_val(self.hand[i]) == other.card_to_val(other.hand[i]):
                    continue
                else:
                    return self.card_to_val(self.hand[i]) < other.card_to_val(other.hand[i])
        return self.scor < other.scor

    def card_to_val(self, a):
        if a == "A":
            return 15
        if a == "K":
            return 14
        if a == "Q":
            return 13
        if a == "J":
            return 0
        if a == "T":
            return 11
        return int(a)
    
    
inp = [card(line) for line in f.read().split("\n")]
inp.sort()
tot = 0
for idx,c in enumerate(inp):
    tot += (idx+1)*c.bits
print(tot)