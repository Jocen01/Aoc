from collections import defaultdict as dd

f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\17\input")
gas = ""
for idx,line in enumerate(f.read().strip().split("\n")):
    gas = line

high = 0
gasPos = 0
gasLen = len(gas)
#print(gasLen)

def dot():
    return "."

tower = dd(dot)
for i in range(1000000):
    tower[(0,i)] = "|"
    tower[(8,i)] = "|"
    tower[(i,0)] = "-"

def push(pos, blocktype):
    global tower
    global gasPos
    global gas
    p = pos if gas[gasPos] == ">" else (pos[0]-2,pos[1])
    #print(gas[gasPos],gasPos)
    gasPos += 1
    gasPos = gasPos%gasLen
    if blocktype == 0:
        if tower[(p[0]+1,p[1])] == "." and tower[(p[0]+2,p[1])] == "." and tower[(p[0]+3,p[1])] == "." and tower[(p[0]+4,p[1])] == ".":
            return (p[0]+1,p[1])
        return pos
    elif blocktype == 1:
        if tower[(p[0]+1,p[1])] == "." and tower[(p[0]+1,p[1]+1)] == "." and tower[(p[0]+2,p[1]+1)] == "." and tower[(p[0],p[1]+1)] == "." and tower[(p[0]+1,p[1]+2)] == ".":
            return (p[0]+1,p[1])
        return pos
    elif blocktype == 2:
        if tower[(p[0]+1,p[1])] == "." and tower[(p[0]+2,p[1])] == "." and tower[(p[0]+3,p[1])] == "." and tower[(p[0]+3,p[1]+1)] == "." and tower[(p[0]+3,p[1]+2)] == ".":
            return (p[0]+1,p[1])
        return pos
    elif blocktype == 3:
        if tower[(p[0]+1,p[1])] == "." and tower[(p[0]+1,p[1]+1)] == "." and tower[(p[0]+1,p[1]+2)] == "." and tower[(p[0]+1,p[1]+3)] == ".":
            return (p[0]+1,p[1])
        return pos
    elif blocktype == 4:
        if tower[(p[0]+1,p[1])] == "." and tower[(p[0]+2,p[1])] == "." and tower[(p[0]+1,p[1]+1)] == "." and tower[(p[0]+2,p[1]+1)] == ".":
            return (p[0]+1,p[1])
        return pos
    else:
        print("fel")

def down(pos, blocktype):
    global tower
    p = pos
    if blocktype == 0:
        return tower[(p[0],p[1]-1)] == "." and tower[(p[0]+1,p[1]-1)] == "." and tower[(p[0]+2,p[1]-1)] == "." and tower[(p[0]+3,p[1]-1)] == "."

    elif blocktype == 1:
        return tower[(p[0],p[1]-1)] == "." and tower[(p[0],p[1])] == "." and tower[(p[0]+1,p[1])] == "." and tower[(p[0]-1,p[1])] == "." and tower[(p[0],p[1]+1)] == "."

    elif blocktype == 2:
        return tower[(p[0],p[1]-1)] == "." and tower[(p[0]+1,p[1]-1)] == "." and tower[(p[0]+2,p[1]-1)] == "." and tower[(p[0]+2,p[1])] == "." and tower[(p[0]+2,p[1]+1)] == "."

    elif blocktype == 3:
        return tower[(p[0],p[1]-1)] == "." and tower[(p[0],p[1])] == "." and tower[(p[0],p[1]+1)] == "." and tower[(p[0],p[1]+2)] == "."

    elif blocktype == 4:
        return tower[(p[0],p[1]-1)] == "." and tower[(p[0]+1,p[1]-1)] == "." and tower[(p[0],p[1])] == "." and tower[(p[0]+1,p[1])] == "."

    else:
        print("fel")

def setBlock(pos, blocktype):
    global tower
    global high
    #print("set",pos,blocktype)
    p = pos 
    if blocktype == 0:
        tower[(p[0],p[1])] = "#"
        tower[(p[0]+1,p[1])] = "#"
        tower[(p[0]+2,p[1])] = "#"
        tower[(p[0]+3,p[1])] = "#"
        high = max(high,p[1])
        #print(tower[(p[0],p[1])])

    elif blocktype == 1:
        tower[(p[0],p[1])] = "#"
        tower[(p[0],p[1]+1)] = "#"
        tower[(p[0]+1,p[1]+1)] = "#"
        tower[(p[0]-1,p[1]+1)] = "#"
        tower[(p[0],p[1]+2)] = "#"
        high = max(high,p[1]+2)

    elif blocktype == 2:
        tower[(p[0],p[1])] = "#"
        tower[(p[0]+1,p[1])] = "#"
        tower[(p[0]+2,p[1])] = "#"
        tower[(p[0]+2,p[1]+1)] = "#"
        tower[(p[0]+2,p[1]+2)] = "#"
        high = max(high,p[1]+2)

    elif blocktype == 3:
        tower[(p[0],p[1])] = "#"
        tower[(p[0],p[1]+1)] = "#"
        tower[(p[0],p[1]+2)] = "#"
        tower[(p[0],p[1]+3)] = "#"
        high = max(high,p[1]+3)

    elif blocktype == 4:
        tower[(p[0],p[1])] = "#"
        tower[(p[0]+1,p[1])] = "#"
        tower[(p[0],p[1]+1)] = "#"
        tower[(p[0]+1,p[1]+1)] = "#"
        high = max(high,p[1]+1)

    else:
        print("fel")

    #for y in range(15):
    #    for x in range(9):
    #        print(tower[(x,y)],end="")
    #    print()


def play(start,blocktype):
    pos = start
    while True:
        pos = push(pos, blocktype)
        #print(pos,gasPos)
        if down(pos,blocktype):
            pos = (pos[0],pos[1]-1)
        else:
            setBlock(pos,blocktype)
            break
        #print(pos)

states = {}

def encode(height):
    global tower
    code = 0
    for i in range(height-20,height):
        for j in range(1,8):
            if tower[(j,i)] == ".":
                code = code 
            else:
                code = code * 2 + 1
            code = code % 10**16 +61
    return code

found = False
br = -1
adHigh = 0
for i in range(5000):
    #print(i)
    start = (3,high + 4) if i % 5 != 1 else (4, high + 4)
    play(start,i%5)
    if encode(high) == encode(high+200):
        print("FEL")
    S = (  (gasPos % gasLen) , (i%5),encode(high))#
    if S in states and not found:
        #print(i,S)
        #print(i,states[S])
        #for y in range(states[S][0]-5,states[S][0]+5)[::-1]:
        #    for x in range(9):
        #        print(tower[(x,y)],end="")
        #    print()
        #print(S)
        #for y in range(high-5,high+5)[::-1]:
        #    for x in range(9):
        #        print(tower[(x,y)],end="")
        #    print()
        found = True
        dH = high - states[S][0]
        di = i - states[S][1]
        br = i + ((1000000000000-i+di-1)%di) 
        #print("BR",br,i,di)
        #print(dH,di,br,states[S][1],((1000000000000-states[S][1])%di), 999999999985%50,1000000000000-states[S][1],di,high)
        #print(high,(1000000000000-i+di-1)%di,(1000000000000-i+di)//di)
        
        
    else:
        states[S] = (high,i)
        if i == 405:
            print(S)
    if i == 405:
        print(S,i,high)
        for y in range(high-5,high+5)[::-1]:
            for x in range(9):
                print(tower[(x,y)],end="")
            print()
        print()

    if i == br:
        adHigh = dH * ((1000000000000-i-1)//di)
        #print(high,adHigh,(1000000000000-high)//di,(1000000000000-high)/di)
        break

   
    
#print(high + adHigh,(1555113636385 -(high + adHigh))/  (high + adHigh),"hgfd")
#print(high + adHigh)


#for y in range(400,410)[::-1]:
#    for x in range(9):
#        print(tower[(x,y)],end="")
#    print()
#print()
#for y in range(2170,2180)[::-1]:
#    for x in range(9):
#        print(tower[(x,y)],end="")
#    print()

print("\n")
print(1555113636385 - high - adHigh ,(1555113636385 - high - adHigh) /1555113636385)
print(high+ adHigh)