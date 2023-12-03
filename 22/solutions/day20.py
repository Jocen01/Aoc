f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\20\input")

class Node:
    def __init__(self, value, next , prev) -> None:
        self.value = value
        self.next = next if next != None else self
        self.prev = prev if prev != None else self

    def moveRight(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.prev = self.next
        self.next = self.next.next
        self.next.prev = self
        self.prev.next = self
    
    def moveLeft(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = self.prev
        self.prev = self.prev.prev
        self.next.prev = self
        self.prev.next = self

    def appendRight(self,value):
        node = Node(value, self.next, self)
        self.next.prev = node
        self.next = node
        return node

    def print(self):
        temp = self.next
        l = []
        l.append(self.value)
        while temp != self:
            l.append(temp.value)
            temp = temp.next
        print(" ".join(map(str,l)))

    
        


nodes = []
noll = None

for idx,line in enumerate(f.read().strip().split("\n")):
    if idx == 0:
        nodes.append(Node(int(line)*811589153,None,None))
    else:
        nodes.append(nodes[-1].appendRight(int(line)*811589153))
        if int(line) == 0:
            noll = nodes[-1]
#print(len(nodes),noll.value,noll.next.value,nodes.index(noll))
noll.print()
for _ in range(10):
    for n in nodes:
        if n.value < 0:
            for _ in range((n.value*-1)%(len(nodes)-1)):
                n.moveLeft()
        else:
            for _ in range(n.value%(len(nodes)-1)):
                n.moveRight()
    #noll.print()
t = noll
res = 0
for i in range(3):
    for _ in range(1000):
        t = t.next
    print(t.value)
    res += t.value
print(res)
