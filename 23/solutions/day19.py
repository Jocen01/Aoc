f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\19\input")
inp = [line for line in f.read().split("\n\n")]
rules = {}

for rule in inp[0].split("\n"):
    name, r = rule.split("{")
    conditions = [c for c in r[:-1].split(",")]
    rules[name] = conditions
letter = ["x","m","a","s"]
accepted = []
stack = [("in",[(1,4000),(1,4000),(1,4000),(1,4000)])]
tot = 0
tot2 = 0
for rule, vars in stack:
    #print(rule,vars)
    if rule == "A":
        
        add = 1
        for i,j in vars:
            add *= (j-i+1)
        tot += add
        continue
    if rule == "R":
        add = 1
        for i,j in vars:
            add *= (j-i+1)
        tot2 += add
        continue
    vars = [i for i in vars]
    for line in rules[rule][:-1]:
        cond,dest = line.split(":")
        ci = int(cond[2:])
        i = letter.index(cond[0])
        new = [i for i in vars]
        if cond[1] == "<":
            if vars[i][1] < ci:
                stack.append((dest,vars))
                break
            if vars[i][0] >= ci:
                continue
            vars[i] = (ci,vars[i][1])
            new[i] = (new[i][0],ci-1)
            stack.append((dest,new))
        if cond[1] == ">":
            if vars[i][1] <= ci:
                continue
            if vars[i][0] > ci:
                
                stack.append((dest,vars))
                break
            
            new[i] = (ci+1,new[i][1])
            vars[i] = (vars[i][0],ci)
            stack.append((dest,new))
    stack.append((rules[rule][-1],vars))
#print(stack)
print(tot)
print(tot + tot2, 4000**4)
assert tot + tot2 == 4000**4
    








"""
def char_to_idx(c):
    if c == "x": return 0
    if c == "m": return 1
    if c == "a": return 2
    if c == "s": return 3
#print(rules)
for line in inp[1].split("\n"):
    vars = [int(i[2:]) for i in line[1:-1].split(",")]
    x,m,a,s = vars
    rule = "in"
    i = 0
    #print(x,m,a,s)
    while i < len(rules[rule]):
        if i +1 == len(rules[rule]):
     
     #       print(rules[rule],i)
            if rules[rule][i] == "A":
                accepted.append((x,m,a,s))
            if rules[rule][i] == "A" or rules[rule][i] == "R":
                break
            rule = rules[rule][i]
            i = 0
            continue
        cond, dest = rules[rule][i].split(":")
        #print(cond, eval(cond),dest)
        if eval(cond):
            if dest == "A":
                accepted.append((x,m,a,s))
            if dest == "A" or dest == "R":
                break
            rule = dest
            i = 0
        else:
            i += 1
        
print(sum([sum(i) for i in accepted]))

"""