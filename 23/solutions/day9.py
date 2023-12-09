f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\9\input")
inp = [[int(i) for i in line.split()] for line in f.read().split("\n")]
tot = 0
for l in inp:
    last = [l[0]]
    while l.count(0) != len(l):
        l2 = [l[i+1]-l[i] for i in range(len(l)-1)]
        last.append(l2[0])
        l=l2
    j = 0
    for i in last[::-1]:
        j= i - j
    tot += j
print(tot)
    