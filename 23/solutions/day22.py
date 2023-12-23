f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\22\input")
inp = [[[int(p) for p in l.split(",")] for l in line.split("~")] for line in f.read().split("\n")]
mx = [0,0,0]
for l1 in inp:
    for l2 in l1:
        mx[0] = max(mx[0],l2[0]+1)
        mx[1] = max(mx[1],l2[1]+1)
        mx[2] = max(mx[2],l2[2]+1)

MAP = [[[-1 for _ in range(mx[2])] for _ in range(mx[1])] for _ in range(mx[0])]
for idx,brick in enumerate(inp):
    (x1,y1,z1),(x2,y2,z2) = brick
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                MAP[x][y][z] = idx
suported_by = [set() for _ in inp]
for x in range(mx[0]):
    for y in range(mx[1]):
        MAP[x][y][0] = -2

falen = True
while falen:
    falen = False
    inp2 = [i for i in inp]
    for idx,((x1,y1,z1),(x2,y2,z2)) in enumerate(inp):
        tot = 0
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if MAP[x][y][z1-1] != -1:
                    tot += 1
        if tot == 0:
            inp2[idx] = [(x1,y1,z1-1),(x2,y2,z2-1)]
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    MAP[x][y][z1-1] = idx
                    MAP[x][y][z2] = -1
            falen=True
    inp = inp2
            

for x in range(mx[0]):
    for y in range(mx[1]):
        for z in range(1,mx[2]):
            if MAP[x][y][z] != MAP[x][y][z-1] and MAP[x][y][z-1] != -1 and MAP[x][y][z] >= 0:
                
                suported_by[MAP[x][y][z]].add(MAP[x][y][z-1])

#for z in range(mx[2]):
#    s = ""
#    for x in range(mx[0]):
#        for y in range(mx[1]):
#            s =s+str(MAP[x][y][z])
#        s = s+"\n"
#    print(s)
#    print()
left = set([i for i in range(len(inp))])
#print(suported_by)
tot = 0
for l in suported_by:
    if len(l) == 1 and list(l)[0] in left:
        left.remove(list(l)[0])
        sup_copy = [set([i for i in l]) for l in suported_by]
        rem = [list(l)[0]]
        for i in rem:
            for idx,l2 in enumerate(sup_copy):
                if i in l2:
                    l2.remove(i)
                    if len(l2) == 0:
                        rem.append(idx)
        #print(len(rem)-1)
        tot += len(rem)-1
print(tot)
        




print(len(left))


