f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\14\input")
edges= []
maxX = 0
minY = 500
maxY = 500
for idx,line in enumerate(f.read().strip().split("\n")):
    edges.append([])
    for cords in line.split(" -> "):
        x,y = cords.split(",")
        maxX = max(maxY,int(y))
        edges[idx].append((int(x),int(y)))
graph = [["." for _ in range(800)]for _ in range(maxY+1)]
for line in edges:
    for i in range(len(line)-1):
        FROM = line[i]
        TO = line[i+1]
        for x in range(min(FROM[0],TO[0]),max(FROM[0],TO[0])+1):
            for y in range(min(FROM[1],TO[1]),max(FROM[1],TO[1])+1):
                #print(x,maxX)
                graph[y][x] = "#"
for i in range(800):
    graph[162][i] = "#"
tot = 0
FIN = False
graph[0][500] = "+"
while "o" not in graph[-1]:
    start = (0,500)
    moved = True

    while moved:
        #print(start[0],start[1],len(graph),len(graph[0]) 

        if graph[start[0]+1][start[1]] == ".":
            start = (start[0]+1,start[1])

        elif graph[start[0]+1][start[1]-1] == ".":
            start = (start[0]+1,start[1]-1)

        elif graph[start[0]+1][start[1]+1] == ".":
            start = (start[0]+1,start[1]+1)

        
        #elif start[0] > 5:
        #    #print(start)
        #    pass
        else:
            moved = False
            if start[0] == 0:
                FIN = True
            graph[start[0]][start[1]] = "o"
            #print(start)
            tot += 1
    if FIN: break
for i,line in enumerate(graph):
    print("".join(line[492:510]))
    if i > 20:
        break
print(graph[161][450:570])
print(tot)


