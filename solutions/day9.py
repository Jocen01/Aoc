import math


f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\9\input")
visited = [[0,0]]
H = [0,0]
T = [0,0]
MOD = 10**9

def moveNext(T,H,rope,idx):
    if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
        #print("no movement",T,steps,di,i)
        a = 3
    elif H[0] - T[0] == 0 and abs(H[1] - T[1]) > 1:
        if H[1] - T[1] > 0:
            T = [T[0],T[1]+1]
        else:
            T = [T[0],T[1]-1]
    elif H[1] - T[1] == 0 and abs(H[0] - T[0]) > 1:
        if H[0] - T[0] > 0:
            T = [T[0]+1,T[1]]
        else:
            T = [T[0]-1,T[1]]
    elif abs(H[1] - T[1]) == 1 and abs(H[0] - T[0]) == 1:
        a = 3
    elif abs(H[1] - T[1]) > 1 and abs(H[0] - T[0]) == 1:
        T = [T[0]+(H[0] - T[0]),T[1]]
        if H[1] - T[1] > 0:
            T = [T[0],T[1]+1]
        else:
            T = [T[0],T[1]-1]
    elif abs(H[1] - T[1]) == 1 and abs(H[0] - T[0]) > 1:
        T = [T[0],T[1]+(H[1] - T[1])]
        if H[0] - T[0] > 0:
            T = [T[0]+1,T[1]]
        else:
            T = [T[0]-1,T[1]]
    elif abs(H[1] - T[1]) > 1 and abs(H[0] - T[0]) > 1:
        if H[1] - T[1] > 0:
            T = [T[0],T[1]+1]
        else:
            T = [T[0],T[1]-1]
        if H[0] - T[0] > 0:
            T = [T[0]+1,T[1]]
        else:
            T = [T[0]-1,T[1]]
    else:
        print(rope,T,H,idx)
    return T

rope = [[0,0] for _ in range(10)]
for idx,line in enumerate(f.read().strip().split("\n")):
    di, steps = line.split()
    steps = int(steps)
    if idx == 6 or idx == 7 or idx == 8:
        print(rope,line)
    for i in range(steps):
        H = rope[0]
        if di == "R":
            H = [H[0]+1,H[1]]
        if di == "L":
            H = [H[0]-1,H[1]]
        if di == "U":
            H = [H[0],H[1]+1]
        if di == "D":
            H = [H[0],H[1]-1]
        rope[0] = H
        for i in range(9):
            rope[i+1] = moveNext(rope[i+1],rope[i],rope,idx)


        visited.append(rope[-1])
S = set()
for i in visited:
    S.add(i[0]+i[1]*100000)

print(len(visited),len(S))
