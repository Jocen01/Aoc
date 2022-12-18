f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\15\input")

from collections import defaultdict

def edgepoints(x,y,delta):
    p = []
    delta += 0
    for i in range(delta+1):
        p.append((x-i,y+i-delta -1))
        p.append((x-i,y-i+delta +1))
        p.append((x+i,y+i-delta -1))
        p.append((x+i,y-i+delta +1))
    return p


def outside(sx,sy,bx,by,delta):
    dx = abs(sx-bx)
    dy = abs(sy-by)
    return dx+dy>delta and 0 <= sx <= 4000000 and 0 <= sy <= 4000000


def value():
    return "."

graf = defaultdict(value)
dists = []
po = []
for idx,line in enumerate(f.read().strip().split("\n")):
    w = line.split()
    sx = int(w[2].strip(",").split("=")[1])
    sy = int(w[3].strip(":").split("=")[1])
    bx = int(w[8].strip(",").split("=")[1])
    by = int(w[9].split("=")[1])
    graf[(sx,sy)] = "S"
    graf[(bx,by)] = "B"
    dists.append([sx,sy,abs(sx-bx)+abs(sy-by)])
    po.append((sx,sy))
    #print(edgepoints(*[sx,sy,abs(sx-bx)+abs(sy-by)]))
    #graf = bfs2(graf,sx,sy,max(4000000,sx,bx),max(4000000,sy,by),min(0,sx,sy),min(0,sy,by))
    #print(sx,sy,bx,by,abs(sx-bx)+abs(sy-by))
pr = (0,0)
for p1 in dists:
    print("PO")
    for edge in edgepoints(*p1):
        br = True
        for p2 in dists:
            if not outside(*edge,*p2):
                br = False
                break
        if br:
            print(edge)
            print(edge[0]*4000000+edge[1])
#print(po)
#for p in dists:
#    if not outside(14,11,*p):
#        print(p)
#print(tot)


#level = 2000000
#for idx,line in enumerate(f.read().strip().split("\n")):
#    w = line.split()
#    sx = int(w[2].strip(",").split("=")[1])
#    sy = int(w[3].strip(":").split("=")[1])
#    bx = int(w[8].strip(",").split("=")[1])
#    by = int(w[9].split("=")[1])
#    dx = abs(sx-bx)
#    dy = abs(sy-by)
#    distToLine = abs(level-sy)
#    graf[bx,by] = "B"
#    graf[sx,sy] = "S"
#
#    for x in range(sx-(dx+dy-distToLine),sx+(dx+dy-distToLine)+1):
#        #print(x,sx,sy,"-",bx,by,"-",dx+dy,(dx+dy-distToLine))
#        if graf[x,level] == ".":
#            #print("#")
#            graf[x,level] = "#"
#tot = 0
#for x in list(graf.keys()):
#    
#    if x[1] == level and graf[x] == "#":
#        #print(x)
#        tot += 1
#print(graf[105942,2000000])
#print(tot)