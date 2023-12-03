f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\1\input")

elfs = f.read().split("\n\n")
MAX = 0
tot = []
for elf in elfs:
    temp = 0
    for i in elf.split("\n"):
        temp += int(i)
    tot.append(temp)
tot.sort()
print(sum(tot[-3:]))

