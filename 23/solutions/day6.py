from collections import defaultdict as dd
f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\6\input")

inp = [[int(i) for i in line.split() if i != ""] for line in f.read().split("\n")]
tot1= 1
for i,j in zip(inp[0],inp[1]):
    tot = 0
    for i1 in range(i):
        if (i-i1)*i1 > j:
            tot += 1
    tot1 *= tot
print(tot1)