f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\11\input")
inp = [line for line in f.read().split("\n")]
rows = []
for idx,line in enumerate(inp):
    if line.count("#") == 0:
        rows.append(idx)
inp = ["".join([inp[i][j] for i in range(len(inp))]) for j in range(len(inp[0]))]
cols = []
for idx,line in enumerate(inp):
    if line.count("#") == 0:
        cols.append(idx)

pos = []
for idx,line in enumerate(inp):
    for jdx,c in enumerate(line):
        if c == "#":
            pos.append((idx,jdx))
tot = 0
print(pos)
for idx,(x1,y1) in enumerate(pos):
    for x2,y2 in pos[idx+1:]:
        tot += abs(x1-x2) + abs(y1-y2)
        tot += sum([1 for i in rows if min(y1,y2) < i < max(y1,y2)])*999999 + sum([1 for i in cols if min(x1,x2) < i < max(x1,x2)])*999999
print(tot)