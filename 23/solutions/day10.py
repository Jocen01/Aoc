f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\10\input")
MAP = [line for line in f.read().split("\n")]

pos = []
starts = []
s = (0,0)
for idx,i in enumerate(MAP):
    for jdx, j in enumerate(i):
        if j == "S":
            s = (idx,jdx)
            starts.append((idx,jdx+1))
            starts.append((idx,jdx-1))
            starts.append((idx+1,jdx))
            starts.append((idx-1,jdx))

def nextPos(pos,c,upLeft=True):
    if upLeft:
        if c == ".": return (-1,-1)
        if c == "|": return (pos[0]+1,pos[1])
        if c == "-": return (pos[0],pos[1]+1)
        if c == "L": return (pos[0],pos[1]+1)
        if c == "J": return (pos[0],pos[1]-1)
        if c == "7": return (pos[0]+1,pos[1])
        if c == "F": return (pos[0]+1,pos[1])
    else:
        if c == ".": return (-1,-1)
        if c == "|": return (pos[0]-1,pos[1])
        if c == "-": return (pos[0],pos[1]-1)
        if c == "L": return (pos[0]-1,pos[1])
        if c == "J": return (pos[0]-1,pos[1])
        if c == "7": return (pos[0],pos[1]-1)
        if c == "F": return (pos[0],pos[1]+1)
    return (-1,-1)


def dir(path, pos):
    if path[-1][1] - path[-2][1] == 1 and MAP[pos[0]][pos[1]] == "J": return False
    if path[-1][1] - path[-2][1] == 1: return True
    if path[-1][0] - path[-2][0] == -1 : return False
    if path[-1][1] - path[-2][1] == -1 and MAP[pos[0]][pos[1]] != "F": return False
    if path[-1][1] - path[-2][1] == -1 and MAP[pos[0]][pos[1]] == "F": return True
    if path[-1][0] - path[-2][0] == 1: return True
    
    
    if path[-1][0] - path[-2][0] == -1: return False

def dir2(path,pos):
    if path[-1][0] - path[-2][0] == 1: return (pos[0],pos[1]-1)
    if path[-1][0] - path[-2][0] == -1: return (pos[0],pos[1]+1)
    if path[-1][1] - path[-2][1] == -1: return (pos[0]-1,pos[1])
    if path[-1][1] - path[-2][1] == 1: return (pos[0]+1,pos[1])
for st in starts:
    visited =set()
    path = [s,st]
    pos = [st]
    right = []
    for p in pos:
        
        right.append(dir2(path,p))
        right.append(dir2(path,path[-2]))
        n = nextPos(path[-1],MAP[p[0]][p[1]],dir(path,p))
        if n == (-1,-1): break
        if n in visited: break
        visited.add(n)
        path.append(n)
        pos.append(n)
        if MAP[n[0]][n[1]] == "S": break
    if MAP[path[-1][0]][path[-1][1]] == "S": break
pos = []
visited =set()
for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        pos.append((i,j))
path = set(path)
tot = 0
right = [r for r in right if r not in path]
right = set(right)
for p in right:
    if p in visited or p in path: continue
    pos = [p]
    for p2 in pos:
        if (p2 in visited) or (p2 in path): continue
        tot += 1
        visited.add(p2)
        for dx,dy in [(1,1),(1,0),(1,-1),(0,1),(0,0),(0,-1),(-1,1),(-1,0),(-1,-1)]:
            if (p2[0]+dx,p2[1]+dy) not in visited and (p2[0]+dx,p2[1]+dy) not in path:
                pos.append((p2[0]+dx,p2[1]+dy))


print(tot)