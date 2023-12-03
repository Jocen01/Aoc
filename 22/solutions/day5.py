f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\5\input.txt")
i = 0
cargo = [["D","T","R","B","J","L","W","G"],["S","W","C"],["R","Z","T","M"],["D","T","C","H","S","P","V"],["G","P","T","L","D","Z"],["F","B","R","Z","J","Q","C","D"],["S","B","D","J","M","F","T","R"],["L","H","R","B","T","V","M"],["Q","P","D","S","V"]]
for line in f.read().strip().split("\n"):
    if i < 10:
        i += 1
        continue
    _,a,_,b,_,c = line.split()
    for _ in range(int(a)):
        cargo[int(c)-1] = cargo[int(c)-1] + cargo[int(b)-1][-1:]
        cargo[int(b)-1] = cargo[int(b)-1][:-1]
for line in cargo:
    print(line[-1],end="")

