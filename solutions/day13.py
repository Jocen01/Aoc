f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\13\input")

def comp(left, right):
    #print(left,right)
    if len(left) == 0 and len(right) > 0:
        return 1
    elif len(left) > 0 and len(right) == 0:
        return -1
    elif len(left)== 0 and len(right) == 0:
        return 0
    for i in range(min(len(left),len(right))):
        if type(left[i]) == type(list()) and type(right[i]) == type(list()):
            if comp(left[i],right[i]) != 0:
                return comp(left[i],right[i])
        elif type(left[i]) == type(list()):
            if comp(left[i],[right[i]]) != 0:
                return comp(left[i],[right[i]])
        elif type(right[i]) == type(list()):
            if 0 != comp([left[i]],right[i]):
                return comp([left[i]],right[i])
        elif left[i] > right[i]:
            return -1
        elif left[i] < right[i]:
            return 1
    if len(left) > len(right):
        return -1
    if len(left) < len(right):
        return 1
    return 0

def buildlist(string):
    l = []
    op = 0
    for c in string:
        if c == "[":
            op += 1


import ast
from functools import cmp_to_key
x = '[ "A","B","C" , " D"]'
x = ast.literal_eval(x)
print(x)
print(comp([[2],[]],[[5],[[[4,3,5],[5,9,10,6,7],[5],4,[9,7,6,2]],2,[]]]))

tot = []
for idx,line in enumerate(f.read().strip().split("\n\n")):
    left, right = line.split("\n")
    tot.append(ast.literal_eval(left))
    tot.append(ast.literal_eval(right))
    #if comp(ast.literal_eval(left),ast.literal_eval(right)) == 1:
    #    tot.append(idx+1)
    #print(idx)
tot.append([[2]])
tot.append([[6]])
tot = sorted(tot, key=cmp_to_key(comp), reverse=True)
print(tot[0])
print(tot.index([[2]]),tot.index([[6]]),tot.index([[2]])*tot.index([[6]]))
