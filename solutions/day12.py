f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\12\input")
G = f.read().strip().split("\n")
def bfs2(grid, S):
    R = len(grid)
    C = len(grid[0])
    q = []
    dist = {}
    for r,c in S:
        q.append((r, c))
        dist[(r, c)] =  0
    while q:
        q2 = []
        for r, c in q:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    dif = grid[nr][nc] - grid[r][c]
                    tup = nr, nc
                    #try:
                    #    if grid[nr][nc] >= 21 and grid[r][c] >19:
                    #        print(grid[nr][nc],nr,nc)
                    #    if grid[r][c] >15:
                    #        print(grid[r][c],nr,nc)
                    #except:
                    #    print(nr,nc)
                    #    pass

                    
                    
                    if dif <= 1 and tup not in dist:
                        dist[tup] = dist[r, c] + 1
                        q2.append(tup)
        q = q2
    return dist
#SE=  "SSSSSSSSSSSSSSSSSSSSSSSSSEabcdefghijklmnopqrstuvwxyz"
alf = "SabcdefghijklmnopqrstuvwxyzE"
      #"abcdefghijklmnopqrstuvwxyz"
for idx,line in enumerate(G):
    for idx2, c in enumerate(line):
        if c not in alf:
            print(c)
#print(G)
graf = [[alf.index(c) for c in line] for line in G]
#print(graf)
S = []
E = 0
f.close()
f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\12\input")
for idx,line in enumerate(f.read().strip().split("\n")):
    for idx2, c in enumerate(line):
        if c == "a":
            S.append([idx,idx2])
        elif c == "E":
            E = [idx,idx2]
#print(graf)
[(E[0],E[1])]
#print(len(graf))
#for l in graf:
#    print(len(l))
dist = bfs2(graf,S)
print(dist[(E[0],E[1])])