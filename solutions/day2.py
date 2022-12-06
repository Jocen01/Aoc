f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\2\input")
tot = 0
MAP = {"A X" : 3, "A Y" : 4, "A Z" : 8, "B X" : 1, "B Y" : 5, "B Z" : 9, "C X" : 2, "C Y": 6,"C Z":7}
for line in f.read().strip().split("\n"):
    tot += MAP[line]
print(tot)
