#function Dataype with return
#int as a parameter n int as a return
def add(x,y):
    return x+y
q=add(12,3)
print(q)
print(type(q))

#float as a parameter n float as return
def add(x,y):
    return x+y
q1=add(20.3,3.7)
print(q1)
print(type(q1))

#string as a parameter n string as return
def name(word):
    return "Hi "+word
q2=name("Sawari")
print(q2)
print(type(q2))

#list as parameter n list as return
cities=['mumbai','nashik','pune']
def addCity(lst):
    cities.append('wardha')
    return lst
q3=addCity(cities)
print(type(q3))

#dict as parameter n dic as return
info={
    "name":"sawari",
    "edu":"degree"
    }
def addLang(dictA):
    dictA["language"]="english"
    return dictA
q10=addLang(info)
print(type(info))

#tupple as parameter n tupple as return
a11 = 12,13
a1 = (12,13)
print(type(a1))

def addElementToTuple(tupA):
    tupA=list(tupA)
    print(tupA)
    tupA.append(40)
    print(tupA)
    tupA=tuple(tupA)
    return tupA
l=addElementToTuple(a1)
print(type(l))
    
#set as parameter n set as return
setA={11,22,33}
def addEtoF(x):
    setA.add(x)
    return setA
l=addEtoF(23)
print(type(l))

#lambda
def add(x,y):
    return x+y
q=add(2,4)
print(q)

addB=lambda x,y:x+y
z=addB(3,3)
print(z)

name=['ajay','aman','amit','amar']
def changename(lst):
    lst[0]='akay'
    return lst
e4=changename(name)
print(e4)
print(name)

lstA=[1,2,3,4,5]
n=[]
for i in lstA:
    n.append(i*5)
print(n)

# list comprehension -- o/p - list
#[expression:loop:condition]
e4=[i*5 for i in lstA]
print(e4)

lstB=[1,2,3,4,5,6,7]
q5=[i+5 for i in lstB]
print(q5)

lstC = [44,55,66,77,33,44,55,66,77,11,22,33,7,8,9]
listD= []
for x in lstC:
    if x % 2 == 0:
        listD.append(x)
print(listD)

listF=[x for x in lstC if x % 2 == 0]
print(listF)




