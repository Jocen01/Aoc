from collections import defaultdict as dd
from math import lcm
f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\20\input")
inp = [line for line in f.read().split("\n")]
before = ["xc","th","pd","bp"]
#(from, to, value)
name_to_type = dd(lambda: "out")
state = {}
remember = {}
ff = {}
conj = {}
braud = []
conections = dd(lambda: [])
for line in inp:
    fr, to = line.split(" -> ")
    if fr[0] == "%":
        ff[fr[1:]] = to.split(", ")
        state[fr[1:]] = False
        name_to_type[fr[1:]] = "ff"
        for t in to.split(", "):
            conections[t].append(fr[1:])
    elif fr[0] == "&":
        conj[fr[1:]] = to.split(", ")
        remember[fr[1:]] = dd(lambda: 0)
        name_to_type[fr[1:]] = "conj"
        for t in to.split(", "):
            conections[t].append(fr[1:])
    else:
        braud = to.split(", ")
        
        name_to_type[fr] = "broadcaster"
        for t in to.split(", "):
            conections[t].append(fr)

print(name_to_type)
deltas = dd(lambda: [])
high = 0
low = 0
Found = False
DP = set()
for idx in range(50000):
    stat = "".join([("1" if i else "0") for i in state.values()])+"".join(["".join([("1" if i else "0") for i in di.values()]) for di in remember.values()])
    hs = hash(stat)
    if hs in DP: break
    DP.add(hs)
    #print(idx)
    low += 1
    pulses = [("broadcaster",i,0) for i in braud]
    for fr,to,val in pulses:
        #print(fr,to,val)
        if fr in before and val == 1:
            print(fr,idx)
            deltas[fr].append(idx)
        if to == "rx" and val == 0: Found = True
        if val == 0: low +=1
        if val == 1: high +=1
        t = name_to_type[to]
        if t == "ff":
            if val == 0:
                state[to] = not state[to]
                pulse = 1 if state[to] else 0
                for ne in ff[to]:
                    pulses.append((to,ne,pulse))
        if t == "conj":
            remember[to][fr] = val
            #print("len",len(conections[to]),to)
            #for i in remember[to].values():
            #    print(i)
            pulse = 0 if sum([1 for i in remember[to].values() if i == 1]) == len(conections[to]) else 1
            for ne in conj[to]:
                    pulses.append((to,ne,pulse))
    if Found: break

f = []
for l in deltas.values():
    d = 0
    p = []
    for i in l:
        p.append(i-d)
        d = i
    print(p)
    f.append(p[-1])
print(lcm(*f))
        

print(low*high)

