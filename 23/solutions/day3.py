f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\3\input")

map = [line for line in f.read().split("\n")]
nums = []
cords = []
n = ""
for i,line in enumerate(map):
    for j,c in enumerate(line):
        if c.isdigit():
            if not n:
                cords.append([])
            cords[-1].append((i,j))
            n += c
        elif n:
            nums.append(int(n))
            n=""
tot = 0
gears = {}
for i in range(len(cords)):
    added = False
    for x,y in cords[i]:
        for dx,dy in [(1,1),(1,0),(1,-1),(0,1),(0,0),(0,-1),(-1,1),(-1,0),(-1,-1)]:
            if 0 <= x+dx < len(map) and 0 <= y+dy < len(map[x+dx]):
                if map[x+dx][y+dy] == "*":
                    if (x+dx,y+dy) in gears:
                        gears[(x+dx,y+dy)].add(i)
                    else:
                        gears[(x+dx,y+dy)] = {i}
for l in gears.values():
    l = list(l)
    if len(l) == 2:
        tot += nums[l[0]] * nums[l[1]]           
print(tot)
