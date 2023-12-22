f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\21\input")
inp = [line for line in f.read().split("\n")]
size = 3#26501365//131
inp2 = [line*(1+2*size) for line in inp]
inp2 = inp2*(1+2*size)
inp = inp2

pos = []
for r,l in enumerate(inp):
    for c,i in enumerate(l):
        if inp[r][c] == "S":
            pos.append((r,c))
pos = [pos[((1+2*size)**2)//2]]
print(pos)
for _ in range(65+131*size):
    pos1=set()
    for r,c in pos:
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            if inp[r+dr][c+dc] != "#":
                pos1.add((r+dr,c+dc))
    pos = pos1
k=0
for idx,r in enumerate(inp):
    for jdx,c in enumerate(r):
        if c != "#" and (idx+jdx)%2 ==1:
            k += 1
print("k",k)
axis = 26501365//2*4
full = 7407 # 7409
full_inverted = 7474 # 7479
tri = 3742
nbr_tri = size+1
outer_tri = 3792#full-tri
#print(len(pos))
#print(len([1 for r,c in pos1 if ((131 > r or r >= 131*2)  and (131 > c or c >= 131*2))]))

nbr_outer_tri = size
nbr_outer_full = 3*(size-1)+2 if size != 0 else 0

l = [0,0]
for i in range(size):
    if i == 0:
        l[0]+=1
    else:
        l[i%2]+=4*i
if size%2 == 0:
    nbr_fulls,nbr_inverted_full = l
else:
    nbr_inverted_full, nbr_fulls = l
nbr_fulls += nbr_outer_full
#nbr_fulls = sum([i for i in range((size*2)+1)])#size*2*(size*2+1)//2 #
print(nbr_fulls,nbr_inverted_full,nbr_tri,nbr_outer_tri)
tot = full*nbr_fulls+full_inverted*nbr_inverted_full+tri*nbr_tri+outer_tri*nbr_outer_tri
print(tot)

assert tot == len(pos)
#full 0,2,6
#full_invert 0,1,4,










"""
tri = len([1 for r,c in pos1 if (131 <= r < 131*2  and 131 <= c < 131*2)])/2
print(tri) 
pr = "\n".join(["".join([inp[r][c] if (r,c) not in pos1 else "O" for c,i in enumerate(l)]) for r,l in enumerate(inp)])
with open("./test.txt","w") as file:
    print(pr,file=file) 
i = 65+131
tot =  tri*2+full
j = 1
while i != 26501365:
    tot += j*4*full
    j+=1
    tot += tri
    i+=131
print(tot)




print((26501365//131+1)*tri+(4*sum([i for i in range((26501365//131))]))*full)

print(len(pos1)*202300+81850175401*full)

#nbr full = 81850984601,81850175401
#nbr tri = 202301


606428706556351
612158218834421
1218586168380430
1218586168376688
2612814711712953748

"""