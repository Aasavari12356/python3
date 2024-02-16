#1
setA={11,22,33}
setB={33,55,66}
setQ=setA.union(setB)
print(setQ)
#2
setA={11,22,33}
setB={22,33,44}
setZ=setA.intersection(setB)
print(setZ)
setA.intersection_update(setB)
print(setA)

setC={11,22,33,44}
setD={33,44,55,66}
setC.intersection_update(setD)
print(setC)

#3
setA={11,22,33}
setB={33,44,55}
setQ=setA.difference(setB)
print(setQ)
setA.difference_update(setB)
print(setA)

#4
setA={55,66,77,88}
setB={99,88,44,33}
setQ=setA.symmetric_difference(setB)
print(setQ)

#5
set01={11,22,33}
set02={11,22,33,44}
setA=set02.issuperset(set01)
setB=set01.issuperset(set02)
print(setA)
print(setB)
setC=set01.issubset(set02)
print(setC)

#6
setA={11,22,33}
setB={33,44,55}
N=setB.isdisjoint(setA)
print(N)

#7
setA={11,22,33}
W=setA.discard(33)
print(W)

