f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\17\input")
inp = [[int(i) for i in line] for line in f.read().split()]

def next_pos(p,d,steps,heat):
    if d == 1 and p[1]+1 < len(inp[0]): return (p[0],p[1]+1,d,steps,heat+inp[p[0]][p[1]+1])
    if d == 2 and p[0]+1 < len(inp): return (p[0]+1,p[1],d,steps,heat+inp[p[0]+1][p[1]])
    if d == 3 and p[1]-1 >= 0: return (p[0],p[1]-1,d,steps,heat+inp[p[0]][p[1]-1])
    if d == 0 and p[0]-1 >= 0: return (p[0]-1,p[1],d,steps,heat+inp[p[0]-1][p[1]])
    return (-1,-1)
visited = set()
pos = [(0,0,1,10,0)]
DP = [[[[10**10 for _ in range(4)] for _ in range(10)] for _ in i] for i in inp]
parent = [[[(0,0,0) for _ in range(3)] for _ in i] for i in inp]
for p in pos:
    for d in range(4):
        if d == (p[2]+2)%4:continue
        if d == p[2] and p[3] == 0: continue
        if d != p[2] and p[3] > 6: continue
        steps = p[3]-1 if p[2] == d else 9
        ne = next_pos(p,d,steps,p[-1])
        if ne[0] != -1 and ne not in visited:
            if DP[ne[0]][ne[1]][ne[3]][ne[2]] > ne[-1]:
                DP[ne[0]][ne[1]][ne[3]][ne[2]] = ne[-1]
                #parent[ne[0]][ne[1]][ne[3]] = (p[0],p[1],p[3])
                pos.append(ne)
                visited.add(ne)

best = 10**10
be = 0
for r,c,_,b,h in visited:
    if r == len(inp)-1 and c == len(inp[-1])-1 and h < best and b < 7: 
        best = h
        be = b
print(best)
#t= 0
#pr = [(-1,-1,be)]
#for p in pr:
#    print(p)
#    pr.append(parent[p[0]][p[1]][p[2]])
#    t += inp[p[0]][p[1]]
#    inp[p[0]][p[1]] = "#"
#    if p[0] == 0 and p[1] == 0:break
#print("\n".join(["".join(map(str,l)) for l in inp]))
#print(t)
