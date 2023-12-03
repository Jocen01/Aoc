from collections import defaultdict as dd
f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\2\input")
inp = f.read().split("\n")
games = []
for idx,line in enumerate(inp):
    l = line.split(": ")
    l2 = l[1].split(", ")
    games.append(dd(lambda : 0))
    for i in l2:
        n,c = i.split()
        games[-1][c] = max(int(n),games[-1][c])
tot = 0
for idx,g in enumerate(games):
    tot +=  g["red"] * g["green"] * g["blue"]
    




print(tot)