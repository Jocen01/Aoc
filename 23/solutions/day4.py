from collections import defaultdict as dd
f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\4\input")

inp =  [[j.split() for j in i.split(": ")[1].split(" | ")] for i in f.read().split("\n")]
print(inp)
tot = 0
po = dd(lambda : 1)
for idx,(c1,c2) in enumerate(inp):
    p = 0
    for c in c1:
        if c in c2:
            p+=1
    for i in range(idx+1,idx+1+p):
        po[i] += po[idx]
    tot += po[idx]
    
print(tot)
