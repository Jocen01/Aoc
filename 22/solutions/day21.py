blueprints = {}
f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\21\input")
res = {}

class Monkey:
    def __init__(self, name, left, op, right) -> None:
        self.op = op
        self.left = left
        self.right = right
        self.name = name
    
    def eval(self, dict):
        global res
        if self.name == "humn":
            res[self.name] = self.left #"NA"
            return self.left #"NA"
        if self.right == 0:
            res[self.name] = self.left
            return self.left
        else:
            resLeft = dict[self.left].eval(dict)
            resRight = dict[self.right].eval(dict)
            if resLeft == "NA" or resRight == "NA":
                res[self.name] = "NA"
                return "NA"
            match self.op:
                case "+":
                    res[self.name] = resLeft + resRight
                    return resLeft + resRight
                case "-":
                    res[self.name] = resLeft - resRight
                    return resLeft - resRight
                case "*":
                    res[self.name] = resLeft * resRight
                    return resLeft * resRight
                case "/":
                    res[self.name] = resLeft / resRight
                    return resLeft / resRight


    def print(self, res, monkeys):
        if self.name == "humn":
            print("humn",end="")
        elif res[self.name] == "NA":
            monkeys[self.left].print(res,monkeys)
            if self.name == "root":
                print("=", end="")
            else:
                print(self.op,end="")
            monkeys[self.right].print(res,monkeys)
        else:
            print(res[self.name],end="")

    


monkeys = {}

for idx,line in enumerate(f.read().strip().split("\n")):
    M , op = line.split(": ")
    op = op.split()
    monkeys[M] = Monkey(M,*op) if len(op) == 3 else Monkey(M,int(op[0]), "+", 0)

print(monkeys["root"].eval(monkeys))
print(monkeys[monkeys["root"].right].eval(monkeys),monkeys[monkeys["root"].left].eval(monkeys))
lo = -100000000000000
hi = 1000000000000000
while hi -1 > lo:
    mid = (hi + lo)//2
    monkeys["humn"].left = mid
    r = monkeys[monkeys["root"].right].eval(monkeys)-monkeys[monkeys["root"].left].eval(monkeys)
    if 0 < r:
        hi = mid
    else:
        lo = mid
    print(hi,lo,r)