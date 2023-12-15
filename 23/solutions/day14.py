f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\14\input")
inp = [[c for c in line] for line in f.read().split("\n")]
F = True
DP = {}
round = 1000000000
while round != 0:
    for rot in range(4):
        F = True
        while F:
            F = False
            for idx, row in enumerate(inp):
                for jdx, c in enumerate(row):
                    if inp[idx][jdx] == "O" and idx != 0 and inp[idx-1][jdx] == ".":
                        inp[idx][jdx] = "."
                        inp[idx-1][jdx] = "O"
                        F = True
        pr = [[inp[row][col] for col in range(len(inp[0])) ] for row in range(len(inp))]

        inp = [[inp[row][col] for row in range(len(inp))[::-1] ] for col in range(len(inp[0]))]

        for _ in range(rot):
            pr = [[pr[row][col] for row in range(len(pr)) ] for col in range(len(pr[0]))[::-1]]
        #print("\n")
        #print("\n".join(["".join(row) for row in pr]))
    #exit()
    #print("\n")
    #print("\n".join(["".join(row) for row in inp]))
    round -= 1
    hash="".join(["i".join(row) for row in inp])
    if hash in DP:
        r = DP[hash]
        print(r,round)
        if round + (round-r) > 0:
            round = (round)%(r-round)
            print(round)
    tot = 0
    for idx,row in enumerate(inp[::-1]):
        for c in row:
            if c == "O":
                tot += 1+idx
    DP[hash] = round
    
print(tot)

