f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\7\input.txt")
di = {}
path = []
ls = False
one = [0,0,0,0,0]
for line in f.read().strip().split("\n"):
    if line == "$ cd /":
        one[0] += 1
        path = ["/"]
    elif line == "$ ls":
        one[1] += 1
        if "/".join(path) in di:
            continue
        di["/".join(path)] = []
        continue
    elif line[0] != "$":
        one[2] += 1
        size , name = line.split()
        di["/".join(path)].append([size,name])
    elif line == "$ cd ..":
        one[3] += 1
        path.pop()
    elif line.split()[1] == "cd":
        one[4] += 1
        path.append(line.split()[2])

def cost(di,name):
    tot = 0
    for size,dir in di[name]:
        if size == "dir":
            tot += cost(di,name+"/"+dir)
        else:
            tot += int(size)
    return tot
res = []
for key in di.keys():
    res.append(cost(di,key))
res.sort()
root = cost(di,"/")
for i in res:
    if 30000000 <= 70000000-root +i:

        print(i)
        break

