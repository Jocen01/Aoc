f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\23\input")


class Elf:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.nextDir = [0,1,2,3]

    def whantToMove(self, outherElfs):
        byItSelf = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (self.pos[0]+i,self.pos[1]+j) in outherElfs:
                    byItSelf += 1
        if byItSelf == 1:
            d = self.nextDir.pop(0)
            self.nextDir.append(d)
            return self.pos, 0
        for d in self.nextDir:
            f = False
            if d == 0:
                for p in [(self.pos[0]-1,self.pos[1]), (self.pos[0]-1,self.pos[1]+1), (self.pos[0]-1,self.pos[1]-1)]:
                    if p in outherElfs:
                        f = True
            if d == 1:
                for p  in [(self.pos[0]+1,self.pos[1]), (self.pos[0]+1,self.pos[1]+1), (self.pos[0]+1,self.pos[1]-1)]:
                    if p in outherElfs:
                        f = True
            if d == 2:
                for p in [(self.pos[0],self.pos[1]-1), (self.pos[0]-1,self.pos[1]-1), (self.pos[0]+1,self.pos[1]-1)]:
                    if p in outherElfs:
                        f = True
            if d == 3:
                for p in [(self.pos[0],self.pos[1]+1), (self.pos[0]-1,self.pos[1]+1), (self.pos[0]+1,self.pos[1]+1)]:
                    if p in outherElfs:
                        f = True
            if not f:
                
                #print(self.nextDir)
                if d == 0:
                    d = self.nextDir.pop(0)
                    self.nextDir.append(d)
                    return (self.pos[0]-1,self.pos[1]), 1
                if d == 1:
                    d = self.nextDir.pop(0)
                    self.nextDir.append(d)
                    return (self.pos[0]+1,self.pos[1]), 1
                if d == 2:
                    d = self.nextDir.pop(0)
                    self.nextDir.append(d)
                    return (self.pos[0],self.pos[1]-1), 1
                if d == 3:
                    d = self.nextDir.pop(0)
                    self.nextDir.append(d)
                    return (self.pos[0],self.pos[1]+1), 1
        d = self.nextDir.pop(0)
        self.nextDir.append(d)
        return self.pos, 0
    
    def move(self, pos):
        
        self.pos = pos



elfs = []

allPos = set()
for idx, line in enumerate(f.read().strip().split("\n")):
    for idx2, c in enumerate(line):
        if c == "#":
            elfs.append(Elf((idx,idx2)))
            allPos.add((idx,idx2))
            #print(idx,idx2)
#tot = 0
#for r in range(74):
#    for c in range(74):
#        if (r, c) not in allPos:
#            tot += 1
#print(tot)

for i in range(1000000):
    #print(i)
    moves = {}
    atPos = set()
    for e in elfs:
        atPos.add(e.pos)
    totalMoves = 0
    for e in elfs:
        newPos, moved = e.whantToMove(atPos)
        #print(moved,e.pos,newPos)
        if newPos in moves:
            moves[newPos].append((e,moved))
        else:
            moves[newPos] = [(e,moved)]
        totalMoves += moved
    
    for p in list(moves.keys()):
        if len(moves[p]) == 1 and moves[p][0][1] == 1:
            moves[p][0][0].move(p)
    if totalMoves == 0:
        print(i)
        break
      
#allPos = set()
#allPos.add(elfs[0].pos)
##print(elfs[0].pos)
#maxR, maxC = elfs[0].pos
#minR, minC = maxR, maxC
#for e in elfs[1:]:
#    #print(e.pos)
#    allPos.add(e.pos)
#    maxR = max(maxR, e.pos[0])
#    minR = min(minR, e.pos[0])
#    maxC = max(maxC, e.pos[1])
#    minC = min(minC, e.pos[1])
#tot = 0
#for r in range(12):
#    for c in range(14):
#        if (r, c) not in allPos:
#            print(".",end="")
#        else:
#            print("#",end="")
#    print()
#print("\n")
#print(tot,minR, maxR, minC, maxC)