f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\25\input")

def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return s

totalFule = 0
for idx, line in enumerate(f.read().strip().split("\n")):
    totnum = 0

    for i,c in enumerate(line[::-1]):
        if c == "=":
            totnum -= 2 * (5**i)
        if c == "-":
            totnum -= 1 * (5**i)
        if c == "1":
            totnum += 1 * (5**i)
        if c == "2":
            totnum += 2 * (5**i)
    totalFule += totnum
    #print(totnum)
print(totalFule,to_base_5(totalFule))

fromPrev = False
string = []
for c in str(to_base_5(totalFule))[::-1]:
    if c == "0":
        if fromPrev:
            string.append("1")
        else:
            string.append("0")
        fromPrev = False
    if c == "1":
        if fromPrev:
            string.append("2")
        else:
            string.append("1")
        fromPrev = False
    if c == "2":
        if fromPrev:
            string.append("=")
            fromPrev = True
        else:
            string.append("2")
    if c == "3":
        if fromPrev:
            string.append("-")
        else:
            string.append("=")
        fromPrev = True
    if c == "4":
        if fromPrev:
            string.append("0")
        else:
            string.append("-")
        fromPrev = True
    #print(c,string[-1])
print("".join(string[::-1]))



