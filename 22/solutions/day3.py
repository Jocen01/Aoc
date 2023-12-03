f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\3\input")
low = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
tot = 0
i = 0
temp = []
for line in f.read().strip().split():
    if len(temp) < 3:
        temp.append(set([c for c in line]))
    else:
        print(i)
        i += 1
        #print(temp)
        c = temp[0].intersection(temp[1])
        c = c.intersection(temp[2])
        for ch in c:
            #print(c,i,low.index(ch) + 1)
            tot += low.index(ch) + 1
        temp = []
        temp.append(set([c for c in line]))
c = temp[0].intersection(temp[1])
c = c.intersection(temp[2])
for ch in c:
    #print(c,i,low.index(ch) + 1)
    tot += low.index(ch) + 1
print(tot)
    