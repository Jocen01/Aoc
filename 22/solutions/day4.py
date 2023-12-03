f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\4\input")
tot = 0
for line in f.read().strip().split("\n"):
    e1,e2 = [[int(i) for i in e.split("-")] for e in line.split(",")]
    if (e1[0] <= e2[0] <= e1[1] ) or (e2[0] <= e1[0]  <= e2[1]) or (e1[0] <= e2[1] <= e1[1] ) or (e2[0] <= e1[1]  <= e2[1]):
        tot += 1
print(tot)

