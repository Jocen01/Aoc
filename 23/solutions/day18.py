f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\18\input")
inp = [line for line in f.read().split("\n")]
visited = []
MAP = [["." for _ in range(20)]for _ in range(20)]
pos = (1,1)
def next_pos(p,d,s):
    if d == "U": return (p[0]-s,p[1])
    if d == "R": return (p[0],p[1]+s)
    if d == "D": return (p[0]+s,p[1])
    if d == "L": return (p[0],p[1]-s)
def i_c(i):
    if i == "0": return "R"
    if i == "1": return "D"
    if i == "2": return "L"
    if i == "3": return "U"
for line in inp:
    d,s,l = line.split()
    s = int(l[2:-2],16)
    d = i_c(l[-2])
    s = int(s)
    np = next_pos(pos,d,s)
    visited.append(np)
    pos = np
def polygonArea(points):
    if len(points) < 3:
        return 0
    pre = points[-1]
    summ = 0
    omk = 0
    for p in points:
        summ += pre[0]*p[1]-p[0]*pre[1] 
        omk += abs(pre[0]-p[0])+abs(pre[1]-p[1])
        pre = p
    return abs(summ / 2)+omk/2+1

print(int(polygonArea(visited)))