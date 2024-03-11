#pgm1
## int as parameter and int as return type
def add(x,y):
    return x+y
q=add(2,3)
print(q)

#pgm2
## float as parameter and float as return type 
def sub(x,y):
    return x-y
q1=sub(12.5,2.4)
print(q1)

#pgm3
## boolean as parameter and boolean as return type 
def canDrive(age,havevehicle):
    if age > 18 and havevehicle:
        return True
    else:
        return False
w=canDrive(19,True)
print(w) 

#pgm4
## string as parameter and string as return type 
def greet(name):
    return ("welcome "+name)
p=greet("aasavari !")
print(p)

#pgm5
## list as parameter and list as return type 
name=["sawari","sham","era"]
def addname(lst):
    lst.append("swara")
    return lst
o=addname(name)
print(o)

#pgm6
## dictionary as parameter and dictionary as return type 

info={
    "firstname":"aasavari",
    "lastname":"bedade"
}

def addcity(information):
    information["city"]="mumbai"
    return information
i=addcity(info)
print(i)

#pgm7
## set as parameter and set as return type
setA={11,22,33}
def addNo(seta):
     seta.add(44)
     return seta

u=addNo(setA)
print(u)

#pgm8
## tuple as parameter and tuple as return type
numbers=(11,22,33,44)
def addvalue(tupA):
    tupA=list(tupA)
    tupA.append(55)
    tupA=tuple(tupA)
    return tupA
k=addvalue(numbers)
