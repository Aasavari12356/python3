numbers=[1,2,3,4,5]
#map
e= lambda x:x+5
q1=list(map(lambda x:x+5,numbers))
print(q1)

#pgm2
birthyear=[1984,1985,1987,1989,1993,1995]
q2=list(map(lambda x:2024-x,birthyear))
print(q2)

#pgm3
marks=[30,40,55,47,68,88]
q3=list(filter(lambda x:x>50,marks))
print(q3)

#pgm4
transection=[55,66,-44,88,-55,-77]
# deposit=[x for x in transection if x > 0]
# withdrawal=[x for x in transection if x < 0]
# print(deposit)
# print(withdrawal)
q4=list(filter(lambda x:x > 0,transection))
print(q4)
q5=list(filter(lambda x:x < 0,transection))
print(q5)


#reduce
#pgm5
from functools import reduce


listA=[11,22,33]
q6=(reduce(lambda x,y:x+y,listA,5))
print(q6)

# e = reduce(lambda acc,el:acc+el,lista,5)
# print(e)




