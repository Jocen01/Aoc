import math


f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\8\input")
inp = [line for line in f.read().split("\n")]
path = inp[0]
steps = {l.split(" = (")[0]:[i.strip(")").strip() for i in l.split(" = (")[1].split(",")] for l in inp[2:]}

idx = 0
def GCD(a, b):
    if(b == 0): return abs(a)
    return GCD(b, a % b)
pos = [k for k in steps.keys() if k[-1] == "A"]
tot=1
l = len(pos)
idxes = [[] for _ in pos]
while l != len([k for k in pos if k[-1] == "Z"]):
    for i in range(len(pos)):
        if path[idx] == "L":
            pos[i] = steps[pos[i]][0]
            
        else:
            pos[i] = steps[pos[i]][1]
        if pos[i][-1] == "Z":
            idxes[i].append((idx,tot))
    tot += 1
    idx +=1
    idx %= len(path)
    #if len([1 for l in idxes if len({t for i,t in l})>=10]) == l:
    #    print([{t for i,t in l} for l in idxes]) 
    #    break
delta = [l[1][1]-l[0][1] for l in idxes]
pos = [l[0][1] for l in idxes]
d = delta[0]
for i in delta:
    d = GCD(d,i)
d2 = [i//d for i in delta]
tot = 1
for i in d2:
    tot *= i
def match(a,m,b,n):
    A = a
    B = b
    while A != B:
        if A > B: B += math.ceil((A-B)/n)*n
        else: A += math.ceil((B-A)/m)*m
    return (A,m*n//GCD(m,n))

A = delta[0]-1
m = delta[0]
for n in delta[1:]:
    print(A,m)
    A,m = match(A,m,n-1,n)
print(A,m)
exit()
while len(set(pos)) != 1:
    idx = pos.index(min(pos))
    pos[idx] += delta[idx]
print(tot)
7309459565206
7309459565207