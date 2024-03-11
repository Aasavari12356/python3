#pgm1
setA={1,2,3}
setB={11,22,33}
e=setA.union(setB)
print(e)

#pgm2
setA={11,22,33,44}
setB={44,55,66,77}
q=setA.intersection(setB)
print(q)
q1=setA.intersection_update(setB)
print(setA)
print(setB)

#pgm3
setA={11,22,33}
setB={33,44,55}
q2=setA.symmetric_difference(setB)
q3=setA.symmetric_difference_update(setB)
print(q2)
print(setA)

#pgm4
seta={44,55,66}
setb={66,77,88}
q4=seta.difference(setb)
q5=seta.difference_update(setb)
print(q4)
print(seta)

#pgm5
setC={1,2,3,4}
setD={1,2,3,4,5,6,7,8}
q6=setC.issubset(setD)
print(q6)
q7=setD.issuperset(setC)
print(q7)
q8=setC.issuperset(setD)
print(q8)

#pgm6
setW={1,2,3,4}
setW.add(5)
print(setW)

#pgm7
# setW.clear()
# print(setW)

setW.pop()
print(setW)

setW.remove(2)
print(setW)


#pgm8
setW.update({11,22,33,44})
print(setW)


#pgm9
r=setW.discard(99)
print(r)

r1=setW.discard(33)
print(r1)