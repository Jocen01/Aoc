f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\15\input")
inp = [line for line in f.read().split(",")]
tot = 0
boxes = [[] for _ in range(256)]
for line in inp:
    if "=" in line:
        line, p = line.split("=")
    else:
        line = line[:-1]
        p=-1
    h = 0
    for c in line:
        h+= ord(c)
        h*=17
        h%=256
    if p == -1:
        boxes[h] = [hs for hs in boxes[h] if hs[0] != line]
    else:
        if len([l[0] for l in boxes[h] if l[0] == line]) == 0:
            boxes[h].append((line,p))
        else:
            k = []
            for hs in boxes[h]:
                if hs[0] == line:
                    k.append((line,p))
                else:
                    k.append(hs)
            boxes[h] = k
tot = 0

for idx,b in enumerate(boxes):
    for j,l in enumerate(b):
        #print((idx+1),(j+1),int(l[1]))
        tot += (idx+1)*(j+1)*int(l[1])

print(tot)