f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\24\input")

MAP = []
storms = []

for idx, line in enumerate(f.read().strip().split("\n")):
    MAP.append([])
    for idx2, c in enumerate(line):
        MAP[idx].append(c)
        if c == "^":
            storms.append((idx,idx2,0))
        if c == ">":
            storms.append((idx,idx2,1))
        if c == "v":
            storms.append((idx,idx2,2))
        if c == "<":
            storms.append((idx,idx2,3))

def stormsMove(storms):
    global MAP
    nextStorm = []
    for s in storms:
        if s[2] == 0:
            if s[0] == 1:
                nextStorm.append((len(MAP)-2,s[1],0))
            else:
                nextStorm.append((s[0]-1,s[1],0))
        if s[2] == 1:
            if s[1] == len(MAP[0])-2:
                nextStorm.append((s[0],1,1))
            else:
                nextStorm.append((s[0],s[1]+1,1))
        if s[2] == 2:
            if s[0] == len(MAP)-2:
                nextStorm.append((1,s[1],2))
            else:
                nextStorm.append((s[0]+1,s[1],2))
        if s[2] == 3:
            if s[1] == 1:
                nextStorm.append((s[0],len(MAP[0])-2,3))
            else:
                nextStorm.append((s[0],s[1]-1,3))
    posOfStorms = set()
    for s in nextStorm:
        posOfStorms.add((s[0],s[1]))
    return nextStorm, posOfStorms

def bfs2(grid, r, c, storms, fr, fc):
    R = len(grid)
    C = len(grid[0])
    q = [(r, c)]
    #dist = {(r, c): 0}
    i = 1
    stormsPos = set()
    while q:
        storms, stormsPos = stormsMove(storms)
        q2 = set()
        for r, c in q:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),(r,c)]:
                if 0 <= nr < R and 0 <= nc < C:
                    tup = nr, nc
                    if grid[nr][nc] != '#' and tup not in stormsPos:
                        #dist[tup] = dist[r, c] + 1
                        if tup == (fr,fc):
                            print(tup)
                            return i, storms
                        q2.add(tup)
        q = list(q2)
        i += 1
        if i %10 == 0:
            print(i)
    return i, storms

i, storms = bfs2(MAP, 0, 1, storms, len(MAP)-1, len(MAP[0])- 2)
i2, storms = bfs2(MAP, len(MAP)-1, len(MAP[0])- 2, storms, 0, 1)
i3, storms = bfs2(MAP, 0, 1, storms, len(MAP)-1, len(MAP[0])- 2)
print(i+i2+i3)

