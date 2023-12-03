MAP = [[" " for _ in range(150)] for _ in range(200)]
inst = ""
f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\22\input")
print(len(MAP[0]))
start = (0,0)
count = 0
for idx,line in enumerate(f.read().split("\n")):
    if idx < 200:
        for i , c in enumerate(line):
            if start == (0,0) and c != " ":
                start = (idx,i)
            MAP[idx][i] = c
            #if c != " ":
                #count += 1
                #MAP[idx][i] = "."
    if idx == 201:
        inst = line
d = 1
#MAP[start[0]][start[1]] = "+"
#MAP[185][14] = "#"
inst = inst.replace("R", " R ")
inst = inst.replace("L", " L ")
print(start)
#inst = "R 50 L " + "200 R 1 L " * 100

def nextPos(dir, pos):
    global MAP
    if dir == 0:
        if pos[0] == 0:
            pos = (len(MAP),pos[1])
        if MAP[pos[0]-1][pos[1]] == " ":
            return nextPos(dir,(pos[0]-1,pos[1]))
        return (pos[0]-1,pos[1])
    if dir == 1:
        if pos[1] == len(MAP[0])-1:
            pos = (pos[0],-1)
        if MAP[pos[0]][pos[1]+1] == " ":
            return nextPos(dir, (pos[0],pos[1]+1))
        return (pos[0],pos[1]+1)
    if dir == 2:
        if pos[0] == len(MAP)-1:
            pos = (-1,pos[1])
        if MAP[pos[0]+1][pos[1]] == " ":
            return nextPos(dir,(pos[0]+1,pos[1]))
        return (pos[0]+1,pos[1])
    if pos[1] == 0:
        pos = (pos[0],len(MAP[0]))
    if MAP[pos[0]][pos[1]-1] == " ":
        return nextPos(dir,(pos[0],pos[1]-1))
    return (pos[0],pos[1]-1)


def nextPosQube(dir,pos):
    if pos[0] == 100 and 0 <= pos[1] < 50 and dir == 0:
        return (50+pos[1],50) , 1
    if 50 <= pos[0] < 100 and pos[1] == 50 and dir == 3:
        return (100, pos[0] - 50), 2

    if 100 <= pos[0] < 150 and pos[1] == 0 and dir == 3:
        return (149 - pos[0],50), 1
    if 0 <= pos[0] < 50 and pos[1] == 50 and dir == 3:
        return (149-pos[0],0), 1

    if 150 <= pos[0] < 200 and pos[1] == 0 and dir == 3:
        return (0,pos[0]-100), 2
    if pos[0] == 0 and 50 <= pos[1] < 100 and dir == 0:
        return (pos[1] + 100, 0) , 1

    if pos[0] == 199 and 0 <= pos[1] < 50 and dir == 2:
        return (0,100 + pos[1]) , 2
    if pos[0] == 0 and 100 <= pos[1] < 150 and dir == 0:
        return (199,pos[1] - 100), 0

    if 150 <= pos[0] < 200 and pos[1] == 49 and dir == 1:
        return (149,pos[0] -100), 0
    if pos[0] == 149 and 50 <= pos[1] < 100 and dir == 2:
        return (100 + pos[1],49), 3

    if pos[0] == 49 and 100 <= pos[1] < 150 and dir == 2:
        return (pos[1] - 50 ,99), 3
    if 50 <= pos[0] < 100 and pos[1] == 99 and dir == 1:
        return (49,pos[0] + 50), 0

    if 0 <= pos[0] < 50 and pos[1] == 149 and dir == 1:
        return (149 - pos[0],99),3
    if 100 <= pos[0] < 150 and pos[1] == 99 and dir == 1:
        return (149 - pos[0], 149),3

    return nextPos(dir,pos), dir

#print(len(inst.split()))

for i in range(len(MAP)):
    for j in range(len(MAP[0])):
        if MAP[i][j] != " ":
            for di in [0,1,2,3]:
                pos = (i,j)
                nPos, di2 = nextPosQube(di,pos)
                assert pos == nextPosQube((di2+2)%4,nPos)[0]
                #print(i,j)
#assert nextPosQube(0,(100,0)) == ((50,50),1)
#exit()
for i,c in enumerate(inst.split()):
    #print(c)
    #if i == 3000000:
    #    break
    if c == "R":
        d = (d + 1)% 4
    elif c == "L":
        d = (d + 3) % 4
    else:
        for _ in range(int(c)):
            next, dn = nextPosQube(d,start)
            #print(next,d)
            assert not (next[0] < 100 and next[1] < 50)
            assert not (next[0] >= 50 and next[1] >= 100)
            assert not (next[0] >= 150 and next[1] >= 50)
            if MAP[next[0]][next[1]] == "#":
                break
            d = dn
            start = next
            if d == 0:
                MAP[start[0]][start[1]] = "^"
            if d == 1:
                MAP[start[0]][start[1]] = ">"
            if d == 2:
                MAP[start[0]][start[1]] = "v"
            if d == 3:
                MAP[start[0]][start[1]] = "<"
#MAP[start[0]][start[1]] = "F"
print((start[0]+1)*1000+(start[1]+1)*4+(d-1)%4,start)
c2 = 0
#for l in MAP:
#    print("".join(l))
#    for c in l:
#        if c == "#":
#            c2 += 1
#print(count,c2)
print([nextPosQube(i,(49,149)) for i in range(4)])

