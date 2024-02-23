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

# setA = {11,22,33}
# def addEtoS(x):
#     setA.add(x)
#     return setA
# l = addEtoS(23)
# print(type(l))



