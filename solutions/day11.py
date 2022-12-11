f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\11\input")

class monkey:
    def __init__(self,line1,line2,line3,line4,line5) -> None:
        self.items = [int(x.strip(",")) for x in line1.split()[2:]]
        self.func = line2
        
        self.test = int(line3.split()[-1])
        self.ifTrue = int(line4.split()[-1])
        self.ifFalse = int(line5.split()[-1])
        self.thrown = 0

    def get(self,n):
        self.items.append(n)

    def hasItems(self):
        return len(self.items) != 0

    def handleItem(self):
        self.items[0] = self.func(self.items[0])%(19*7*17*13*11*2*5*3)
        
        if self.items[0]%self.test == 0:
            return self.ifTrue
        return self.ifFalse
    
    def give(self):
        p = self.items[0]
        self.items.pop(0)
        self.thrown += 1
        return p


lamb = [lambda x: x*13,lambda x: x*x,lambda x: x + 6, lambda x: x+2,lambda x: x+3,lambda x: x+4,lambda x: x+8,lambda x: x*7]
#lamb = [lambda x: x*19,lambda x: x+6,lambda x: x*x,lambda x: x+3,]
monkeys = []
for idx,line in enumerate(f.read().strip().split("\n\n")):
    lines = line.split("\n")
    lines.pop(0)
    monkeys.append(monkey(lines[0],lamb[idx],lines[2],lines[3],lines[4]))
b = [m.thrown for m in monkeys]
S = set()
for i in range(10000):
    for monk in monkeys:
        while monk.hasItems():
            monkeys[monk.handleItem()].get(monk.give())
a = [m.thrown for m in monkeys]
a.sort()
print(a[-1]*a[-2])

    