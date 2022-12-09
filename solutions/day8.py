f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\8\input")

def bfs2(grid,start):
    R = len(grid)
    C = len(grid[0])
    q = start
    dist = set([cell[0] + cell[1]*len(grid)for cell in start])
    #print(dist)
    tot = len(dist)
    visited = set()
    for i in dist:
        visited.add(i)
    while q:
        q2 = []
        for r, c in q:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    tup = nr, nc
                    if grid[nr][nc] > grid[r][c] and tup not in dist:
                        dist.add(nr+nc*len(graph))
                        q2.append(tup)
                        if nr+nc*len(graph) not in visited:
                            visited.add(nr+nc*len(graph))
                            tot += 1
        q = q2
    return tot

graph = [[int(c) for c in line] for line in f.read().strip().split("\n")]
#edges =[ [(i,j) for i in range(len(graph[0]))] for j in range(len(graph[0]))]
edges = []

for j in range(99):
    edges.append((0,j))
    edges.append((98,j))
    edges.append((j,0))
    edges.append((j,98))
edg2 = edges.copy()

res = bfs2(graph,list(set(edges)))
print(len(graph[0]),len(graph))
print(res)

print(len(list(set(edges))),"fghjk")
j = 0
for i in range(0,99):
    while graph[i][j] < graph[i][j+1]:
        edges.append((i,j+1))
        j += 1
j = 98
for i in range(0,99):
    while graph[i][j] < graph[i][j-1]:
        edges.append((i,j-1))
        j -= 1
j = 0
for i in range(0,99):
    while graph[j][i] < graph[j+1][i]:
        edges.append((j+1,i))
        j += 1
j = 98
for i in range(0,99):
    while graph[j][i] < graph[j-1][i]:
        edges.append((j-1,i))
        j -= 1
print(len(list(set(edges))))
print(len(edg2))

trees = set()
R,C = len(graph),len(graph[0])
for r in range(R):
    mx = -1
    for c in range(C):
        if graph[r][c] > mx:
            trees.add((r,c))
            mx =  graph[r][c]
    mx = -1
    for c in range(C)[::-1]:
        if graph[r][c] > mx:
            trees.add((r,c))
            mx =  graph[r][c]
for c in range(C):
    mx = -1
    for r in range(R):
        if graph[r][c] > mx:
            trees.add((r,c))
            mx =  graph[r][c]
    mx = -1
    for r in range(R)[::-1]:
        if graph[r][c] > mx:
            trees.add((r,c))
            mx =  graph[r][c]


def get(R,C,graph):
    H = graph[R][C]
    print(H)
    tot = 1
    sight= 1
    c = C
    for r in range(0,R)[::-1]:
        print(r,c,graph[r][c])
        assert(0 <= r <99 and 0 <= c <99)
        if graph[r][c] < H:
            sight += 1
        else:
            break
    print(sight,tot)
    tot = tot * sight
    sight = 0
    for r in range(R+1,99):
        print(r,c,graph[r][c])
        assert(0 <= r <99 and 0 <= c <99)
        if graph[r][c] < H:
            sight += 1
        else:
            break
    print(sight,tot)
    tot *= sight
    sight= 0
    r = R
    for c in range(0,c)[::-1]:
        print(r,c,graph[r][c])
        assert(0 <= r <99 and 0 <= c <99)
        if graph[r][c] < H:
            sight += 1
        else:
            break
    print(sight,tot)
    tot *= sight
    sight= 0
    for c in range(C+1,99):
        print(r,c,graph[r][c])
        assert(0 <= r <99 and 0 <= c <99)
        if graph[r][c] < H:
            sight += 1
        else:
            break
    print(sight,tot)
    tot *= sight
    return tot

ma = 0
print(get(86,48,graph))
#for r in range(0,99):
#    for c in range(1,99):
#
#        if get(r,c,graph) > ma:
#            ma = get(r,c,graph)
#            print(r,c,get(r,c,graph))
print(ma)