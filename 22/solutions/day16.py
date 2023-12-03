f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\16\input")

vValue = {}
vNext = {}
dims = {}
mask = {}

for idx,line in enumerate(f.read().strip().split("\n")):
    print(line)
    l1,l2= line.split("; ")
    name = l1.split()[1]
    print(l1.split("="))
    value = int(l1.split("=")[-1])
    TO = [v for v in l2.strip("tunnels lead to valves ").split(", ")]
    vNext[name] = TO
    vValue[name] = value
    dims[name] = [-1 for _ in range(31)]
    mask[name] = idx

#def cost(pos, time, tot,visited):
#    global vValue
#    global vNext
#    if dims[pos][time] >= tot:
#        return dims[pos][time]
#    if time == 0:
#        #saved[(pos,time)] = tot
#        dims[pos][time] = max(tot,dims[pos][time])
#        return dims[pos][time]
#    if time == 1:
#        tot += vValue[pos] * time
#        time = 0
#        dims[pos][time] = max(dims[pos][time],tot)
#        return dims[pos][time]
#    if vValue[pos] != 0 and pos not in visited:
#        visited.add(pos)
#        time -= 1
#        tot += vValue[pos] * time
#        resul = 0
#        for next in vNext[pos]:
#            resul = max(resul,cost(next,time-1,tot,visited))
#        dims[pos][time] = max(tot,resul)
#        visited.remove(pos)
#        tot -= vValue[pos] * time
#        time += 1
#    resul = 0
#    for next in vNext[pos]:
#        resul = max(resul,cost(next,time-1,tot, visited))
#    if dims[pos][time] < resul:
#        dims[pos][time] = resul
#    return dims[pos][time]
#
#print(cost("AA",30,0,set()))
#print(dims)
#S = set()
#for v in list(dims.values()):
#    for t in v:
#        S.add(t)
#print(S)
i = 0
visited = {}
best = [0]*27

def DP(time, opened, node,node2,tot):
    global i
    global vValue
    global vNext
    global visited
    global best
    

    if time <= 0:
        return 0
    if (time, opened, node,node2) in visited:
        return visited[(time, opened, node,node2)]
    if time < 20 and best[time] > tot * 1.1:
            return 0
    ans = max([max([DP(time-1,opened,nex,nex2,tot) for nex in vNext[node]]) for nex2 in vNext[node2]])

    if vValue[node] != 0:
        alt = max([vValue[node] * (time-1) + DP(time-1,opened|(1<<mask[node]),node,nex,tot + vValue[node] * (time-1)) for nex in vNext[node2] if opened&(1<<mask[node]) == 0] + [0])
        ans  = max(ans,alt)
    if vValue[node2] != 0:
        alt = max([vValue[node2] * (time-1) + DP(time-1,opened|(1<<mask[node2]),nex,node2,tot + vValue[node2] * (time-1)) for nex in vNext[node] if opened&(1<<mask[node2]) == 0] + [0])
        ans  = max(ans,alt)
    if vValue[node] != 0 and vValue[node2] != 0 and node != node2 and opened&(1<<mask[node]) == 0 and opened&(1<<mask[node2]) == 0:
        ans = max(ans, vValue[node] * (time-1) + vValue[node2] * (time-1) + DP(time-1,opened|(1<<mask[node])|(1<<mask[node2]),node,node2,tot + vValue[node] * (time-1) + vValue[node2] * (time-1)))


    visited[time,opened,node,node2] = ans
    i += 1
    if i %1000000 == 0:
        print(i//1000000)
    if time > 22:
        print(time)
    best[time] = max(best[time],ans)
    return ans

print(DP(26,0,"AA","AA",0))
print(vValue)
