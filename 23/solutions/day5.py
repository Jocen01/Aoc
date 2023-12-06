from collections import defaultdict as dd
f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\5\input")

inp = [line for line in f.read().split("\n\n")]

seeds = [int(i) for i in inp[0].split(": ")[1].split()]
ny = []
s1 = -1
for s in seeds:
    if s1 == -1:
        s1 = s
    else:
        ny.append((s1,s1+s))
        s1 = -1
mapings = ny

NK = []
ranges = []
for lines in inp[1:]:
    ln = lines.split("\n")
    n,k = ln[0].split()[0].split("-to-")
    NK.append((n,k))
    ranges.append([])
    l = []
    for line in ln[1:]:
        ranges[-1].append([int(i) for i in line.split()])
        l.append(([int(i) for i in line.split()][1],[int(i) for i in line.split()][2]-1))


    ranges[-1]
tot = 10**10


for rng in ranges:
    
    maped = set()
    for t,f,r in rng:
        l = len(mapings)
        for i in range(l):
            start, end = mapings[i]
            if end <= f or start >= f+r or i in maped: continue
            if start < f and end >= f+r:
                mapings[i] = (start,f)
                mapings.append((t,t+r))
                maped.add(len(mapings)-1)
                if f+r != end:
                    mapings.append((f+r,end))
            elif start < f and end < f+r:
                mapings[i] = (start,f)
                mapings.append((t,end-f+t))
                maped.add(len(mapings)-1)
            elif start >= f and end >= f+r:
                mapings[i] = (start-f+t,t+r)
                maped.add(i)
                if f+r != end:
                    mapings.append((f+r,end))
            elif start >= f and end < f+r:
                mapings[i] = (start-f+t,end-f+t)
                maped.add(i)
            else:
                print("impossible",start,end,f,r,t,start >= f, end >= f+r)






for s,t in mapings:
    tot = min(tot,s)
print(tot)


