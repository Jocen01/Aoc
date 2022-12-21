
blueprints = []
f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\19\input")
for idx,line in enumerate(f.read().strip().split("\n")):
    blue = line.split()
    blueprints.append([int(blue[6]),int(blue[12]),int(blue[18]),int(blue[21]),int(blue[27]),int(blue[30])])
#print(blueprints)



def DP(ore,clay,obs,geode,oreM,clayM,obsM, geoM, time):
    global best
    global cost
    if time == 32:
        best[time] = max(best[time],geode)
        return geode
    if time  < 5:
        print(time)
        #return 0
    if ore > 100 or clay > 50 or obs > 25:
        return 0
    if oreM > 4 or clayM > cost[3] or obsM > cost[5]:
        return 0
    #if obs - obsM >= cost[5] and ore - oreM >= cost[4]:
    #    return 0
    M = 0
    if ore >= cost[4] and obs >= cost[5]:
        M = max(M,DP(ore-cost[4]+oreM, clay+clayM, obs-cost[5]+obsM, geode+geoM, oreM, clayM, obsM, geoM+1, time + 1))
    if ore >= cost[2] and clay >= cost[3]:
        M = max(M, DP(ore-cost[2]+oreM, clay-cost[3]+clayM, obs+obsM, geode+geoM, oreM, clayM, obsM+1, geoM, time + 1))
    if ore >= cost[1] and ore - oreM < cost[1]:#
        M = max(M, DP(ore-cost[1]+oreM, clay+clayM, obs+obsM, geode+geoM, oreM, clayM+1, obsM, geoM, time + 1))
    if ore >= cost[0] and ore - oreM < cost[0]:#
        M = max(M, DP(ore-cost[0]+oreM, clay+clayM, obs+obsM, geode+geoM, oreM+1, clayM, obsM, geoM, time + 1))
    
    
    
    M = max(M, DP(ore+oreM, clay+clayM, obs+obsM, geode+geoM, oreM, clayM, obsM, geoM, time+1))
    best[time] = max(best[time],geode)
    return M
tot = []
print("running")
for b in blueprints:
    cost = b
    best = [0 for _ in range(33)]
    r = DP(2,0,0,0,1,0,0,0,2)
    tot.append(r)
    print(r)
    print(best)
res = 0
for idx, i in enumerate(tot):
    res += (idx+1)*i
    print((idx+1)*i, " ", end="")
print(res)

