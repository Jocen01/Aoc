import numpy as np
import sympy


f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\24\input")
N = f.read().split("\n")

inp = [[l.split(", ") for l in line.split(" @ ")] for line in N]
mi = 200000000000000
ma = 400000000000000

def pts2line(p, q):
    return (-q[1] + p[1],
          q[0] - p[0],
          p[0]*q[1] - p[1]*q[0])

def line_intersection(l1, l2):
    a1,b1,c1 = l1
    a2,b2,c2 = l2
    cp = a1*b2 - a2*b1
    if cp != 0:
        return float(b1*c2 - b2*c1)/cp, float(a2*c1 - a1*c2)/cp
    else:
        return False
tot = 0
"""
for idx,l1 in enumerate(inp):
    ((x1,y1,_), (dx1,dy1,_)) = map(int,l1[0]),map(int,l1[1])
    for jdx,l2 in enumerate(inp[idx+1:]):
        ((x2,y2,_), (dx2,dy2,_)) = map(int,l2[0]),map(int,l2[1])
        t = 3.333
        line1 = pts2line((x1,y1),(x1+dx1,y1+dy1))
        line2 = pts2line((x2,y2),(x2+dx2,y2+dy2))
        l = line_intersection(line1,line2)
        if l:
            x,y = l
            if (x-x1)/dx1 < 0: continue
            if (x-x2)/dx2 < 0: continue
            if mi <= x <= ma and  mi <= y <= ma:
                tot += 1
                #print(x1,y1,x2,y2, x,y)"""
def norm(P):
    return (P[0]**2 + P[1]**2 + P[2]**2)**(0.5)

def dist3D(A, u, p):
    AP = tuple(A[i] - p[i] for i in range(3))
    cross = tuple(AP[i]*u[(i+1)%3] - AP[(i+1)%3]*u[i]
        for i in range(3))
    return norm(cross)/norm(u)

t = [0,0,0]
vectors = []
dirs = []
for idx,l1 in enumerate(inp):
    ((x,y,z), (dx,dy,dz)) = map(int,l1[0]),map(int,l1[1])
    vectors.append((x,y,z))
    dirs.append((dx,dy,dz))
pos = vectors[0]
dir = (vectors[0][0]-vectors[1][0],vectors[0][1]-vectors[1][1],vectors[0][2]-vectors[1][2])
for dx in range(-100,100):
    for dy in range(-100,100):
        for dz in range(-100,100):
            px,py,pz = vectors[0]


def day24_part2(s):
  array = np.array([line.replace('@', ',').split(',')
                    for line in s], float) 
  print(array) 
  p, v, t = (sympy.symbols(f'{ch}(:3)') for ch in 'pvt')
  print(p,v,t)
  equations = [
      array[i, j] + t[i] * array[i, 3 + j] - p[j] - v[j] * t[i]
      for i in range(3) for j in range(3)
  ]
  return sum(sympy.solve(equations, (*p, *v, *t))[0][:3])
print(day24_part2(N))
    

