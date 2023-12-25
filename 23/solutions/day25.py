f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\25\input")
inp = [line for line in f.read().split("\n")]
from collections import defaultdict as dd
from itertools import combinations

from collections import defaultdict
class Dinitz:
    def __init__(self, sz, INF=10**10):
        self.G = [defaultdict(int) for _ in range(sz)]
        self.sz = sz
        self.INF = INF

    def add_edge(self, i, j, w):
        self.G[i][j] += w
        self.G[j][i] += w

    def bfs(self, s, t):
        level = [0]*self.sz
        q = [s]
        level[s] = 1
        while q:
            q2 = []
            for u in q:
                for v, w in self.G[u].items():
                    if w and level[v] == 0:
                        level[v] = level[u] + 1
                        q2.append(v)
            q = q2
        self.level = level
        return level[t] != 0

    def dfs(self, s, t, FLOW):
        if s in self.V: return 0
        if s == t: return FLOW
        self.V.add(s)
        L = self.level[s]
        for u, w in self.G[s].items():
            if u in self.dead: continue
            if w and L+1==self.level[u]:
                F = self.dfs(u, t, min(FLOW, w))
                if F:
                    self.G[s][u] -= F
                    self.G[u][s] += F
                    return F
        self.dead.add(s)
        return 0
    

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.dead = set()
            while True:
                self.V = set()    
                pushed = self.dfs(s, t, self.INF)
                if not pushed: break
                flow += pushed
        return flow

names = set()

wores = set()

rem  = [("hfx","pzl"),("bvb","cmg"), ("nvd","jqt")]

neigh = dd(lambda: set())

for line in inp:
    fr, to = line.split(": ")
    
    names.add(fr)
    for i in to.split():
        neigh[fr].add(i)
        neigh[i].add(fr)
        wores.add((fr,i))
        wores.add((fr,i))
        names.add(i)
k = len(names)
names = list(names)

together = [{names[0]},set()]
for idx,i in enumerate(names):
    for jdx,j in enumerate(names[idx+1:]):
        FLOW = Dinitz(k)
    

        for f,t in wores:
            FLOW.add_edge(names.index(f),names.index(t),1)
        f = FLOW.max_flow(idx,idx+1+jdx)
        print(i,j,f)
        if f > 3:
            together[0].add(j)
        else:
            together[1].add(j)

    break
print(len(together[0]),len(together[1]))
exit()
best = 0
start = inp[0].split(": ")[0]
print(len(wores))
for idx,l in enumerate(combinations(wores,3)):
    if idx %1000 == 0: print(idx)
    pos = [start]
    visited = set([start])
    for p in pos:
        for ne in neigh[p]:
            if ne not in visited and ((p,ne) not in l and (ne,p) not in l):
                pos.append(ne)
                visited.add(ne)
    if len(visited) != k and len(visited) != 3:
        print(len(visited),k-len(visited),len(visited)*k-len(visited))
    #print(visited)
    #break


