f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\12\input")
inp = [line.split() for line in f.read().split("\n")]
intervalls = [[int(i) for i in l[1].split(",")] for l in inp]
tot = 0
stack = []
dp = {}
def posibilities(line: str, inter):
    global dp
    ha = line + " ".join(map(str,inter))
    if ha in dp:
        return dp[ha]
    if (len(line) == 0 and len(inter)>= 1) or (sum(inter) + len(inter)-1 > len(line)): return 0
    if len(inter) == 0:
        if line.count("#") == 0:
            return 1
        return 0
    if len(line) == inter[0] and line.count(".") == 0: return 1
    tot =0
    for i in range(len(line)):
        if line[i] == ".": continue
        if len(line[i:]) >= inter[0] and line[i:inter[0]+i].count(".") == 0 and (len(line) == inter[0]+i or line[inter[0]+i] != "#"):
            tot += posibilities(line=line[i+inter[0]+1:],inter=inter[1:])
        if i + inter[0] == len(line) or line[i] == "#":break
    dp[ha] = tot
    return tot
for idx,(line, l) in enumerate(inp):
    inter = [int(i) for i in l.split(",")]
    tot += posibilities("?".join([line for _ in range(5)]), inter*5)
    dp = {}
print(tot)





# ?#???????????? 1,1,2,3


# guessed 5733