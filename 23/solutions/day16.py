f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\16\input")
inp = [line for line in f.read().split()]


def next_dir(dir, c):
    if c == ".": return dir
    if c == "-" and (dir == 1 or dir == 3): return [dir]
    if c == "-": return [(dir+1)%4,(dir+3)%4]
    if c == "|" and (dir == 0 or dir == 2): return [dir]
    if c == "|": return [(dir+1)%4,(dir+3)%4]
    if c == "/" and dir == 1: return 0
    if c == "/" and dir == 0: return 1
    if c == "/" and dir == 3: return 2
    if c == "/" and dir == 2: return 3
    if c == "\\" and dir == 1: return 2
    if c == "\\" and dir == 2: return 1
    if c == "\\" and dir == 3: return 0
    if c == "\\" and dir == 0: return 3
best = 0
starts = []
for i in range(len(inp)):
    starts.append((i,0,1))
    starts.append((i,len(inp[0])-1,3))
for i in range(len(inp[0])):
    starts.append((0,i,2))
    starts.append((len(inp)-1,i,0))
for v in starts:
    visited = set([v])
    pos = [v]
    delta = [(-1,0),(0,1),(1,0),(0,-1)]
    for p in pos:
        if 0 > p[0] or p[0] >= len(inp) or 0 > p[1] or p[1] >=  len(inp[0]): continue
        if inp[p[0]][p[1]] == "-" or  inp[p[0]][p[1]] == "|":
            ne = next_dir(p[2], inp[p[0]][p[1]])
        else:
            ne = [next_dir(p[2], inp[p[0]][p[1]])]
        for n_dir in ne:
            if (p[0]+delta[n_dir][0],p[1]+delta[n_dir][1],n_dir) not in visited:
                pos.append((p[0]+delta[n_dir][0],p[1]+delta[n_dir][1],n_dir))
                visited.add((p[0]+delta[n_dir][0],p[1]+delta[n_dir][1],n_dir))
    a = {(i[0],i[1]) for i in visited if not (0 > i[0] or i[0] >= len(inp) or 0 > i[1] or i[1] >=  len(inp[0]))}
    #print(len(a))
    if len(a) > best: best = len(a)
    #inp = [[c for c in i] for i in inp]
    #print("\n".join(["".join(r) for r in inp]))
    #for r,c in a:
    #    inp[r][c] = "#"
    #print("\n".join(["".join(r) for r in inp]))
print(best)