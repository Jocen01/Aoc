f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\18\input")

points = []
cubes = set()
X,Y,Z = 0,0,0

for idx,line in enumerate(f.read().strip().split("\n")):
    x,y,z= map(int,line.split(","))
    X = max(x,X)
    Y = max(y,Y)
    Z = max(z,Z)
    points.append([x,y,z])
    cubes.add((x+1,y+1,z+1))

sides = 0
for x,y,z in points:
    for dx,dy,dz in [[x+1,y,z],[x-1,y,z],[x,y+1,z],[x,y-1,z],[x,y,z+1],[x,y,z-1]]:
        if (dx,dy,dz) not in cubes:
            sides += 1
print(sides,X,Y,Z)

def bfs2(r, c, h, cubes):
    sides = 0
    q = [(r, c, h)]
    dist = {(r, c, h): 0}
    while q:
        q2 = []
        for r, c, h in q:
            for nr, nc, nh in [(r - 1, c, h), (r + 1, c, h), (r, c - 1, h), (r, c + 1, h),(r, c ,h - 1), (r, c ,h + 1)]:
                if 0 <= nr < 23 and 0 <= nc < 23 and 0 <= nh < 23:
                    tup = nr, nc, nh
                    if (nr, nc, nh) not in cubes and tup not in dist:
                        dist[tup] = dist[r, c, h] + 1
                        q2.append(tup)
                    if (nr, nc, nh) in cubes:
                        sides += 1
        q = q2
    return sides

print(bfs2(0,0,0,cubes))