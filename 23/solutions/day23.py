f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\23\input")
inp = [line for line in f.read().split("\n")]
from heapq import heappop, heappush, heapify



nodes = [(0,0),(len(inp)-1,len(inp[0])-2)]
for r in range(1,len(inp)-1):
    for c in range(1,len(inp[0])-1):
        if inp[r][c] != "#":
            cnt = 0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if inp[r+dx][c+dy] != "#":
                    cnt += 1
            if cnt > 2:
                nodes.append((r,c))
nodess = {n:idx for idx,n in enumerate(nodes)}
neigh = [[] for _ in nodes]
for idx,node in enumerate(nodes):
    pos = [node]
    tot = 1
    visited = set([node])
    while pos:
        pos1 = []
        for p in pos:
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if p[0]+dx >= len(inp) or p[0]+dx < 0 or (p[0]+dx,p[1]+dy) in visited: continue
                if (p[0]+dx,p[1]+dy) in nodess:
                    neigh[idx].append((nodess[(p[0]+dx,p[1]+dy)],tot))
                elif inp[p[0]+dx][p[1]+dy] != "#":
                    pos1.append((p[0]+dx,p[1]+dy))
                    visited.add((p[0]+dx,p[1]+dy))
        pos = pos1
        tot += 1
print(nodes)
print(neigh)
pos = []
heapify(pos)
heappush(pos,(0,0,{}))   #pos = [(0,0,{})]#node,dist,visited nodes
tot = 0
best = 0
parents = [[{} for _ in l] for l in inp]

while pos:
    p = heappop(pos)
    path = [a for a in p[2]]
    if len(p[2]) == 4:
        print(p[2])
    if p[1] == 1: 
        if p[0] < best:
            print(p[0],path,len(path))
        best = min(p[0],best)
        continue
    for ne in neigh[p[1]]:
        if ne[0] not in path:
            pos.append((p[0]-ne[1],ne[0], path+[ne[0]]))

#inp = [[c for c in line] for line in inp]
#for r,c in visited.keys():
#    inp[r][c] = "0"

#print("\n".join(["".join(line) for line in inp]))
print(best)