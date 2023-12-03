f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\10\input")
image = [[]for _ in range(7)]
row = 0
cykle = -1
tot = 0
X = 1
def draw(image,row,cykle,X):
    print(cykle,X)
    if abs(X-cykle) <= 1:
        image[row].append("#")
    else:
        image[row].append(".")

for idx,line in enumerate(f.read().strip().split("\n")):
    if line == "addx 1":
        print(cykle)
    if line == "noop":
        cykle += 1
        cykle = cykle%40
        if cykle == 0:
            row+=1
        draw(image,row,cykle,X)
    else:  
        _,x = line.split()
        cykle += 1
        cykle = cykle%40
        if cykle == 0:
            row+=1
        draw(image,row,cykle,X)
        cykle+=1
        cykle = cykle%40
        if cykle == 0:
            row+=1
        draw(image,row,cykle,X)
        X += int(x)
    
for l in image:
    print("".join(l))