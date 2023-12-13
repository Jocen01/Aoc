f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\13\input")
inp = [line.split() for line in f.read().split("\n\n")]
tot = 0
for MAP in inp:

    for row in range(1,len(MAP)):
        diffs = 0
        for i in range(row):
            
            if row+i < len(MAP) and MAP[row-1-i] != MAP[row+i]:
                for c1,c2 in zip(MAP[row-1-i], MAP[row+i]):
                    if c1 != c2: diffs += 1
                
        if diffs == 1: tot += 100*row
    
    MAP = ["".join([MAP[i][j] for i in range(len(MAP))]) for j in range(len(MAP[0]))]

    for row in range(1,len(MAP)):
        diffs = 0
        for i in range(row):
            
            if row+i < len(MAP) and MAP[row-1-i] != MAP[row+i]:
                for c1,c2 in zip(MAP[row-1-i], MAP[row+i]):
                    if c1 != c2: diffs += 1
                
        if diffs == 1: tot += row
print(tot)