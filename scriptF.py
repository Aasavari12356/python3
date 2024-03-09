alpha=("a","b","c","d")
print(alpha)
print(type(alpha))
print(len(alpha))
aa=list(alpha)
print(aa)
print(type(aa))

#pgm1
namee=['aasavari','pooja','leena']
print(type (namee))

#pgm2
info={
    'firstname':'aasavari',
    'lastname':'bedade',
    "age":31
}
print(type(info))

#pgm3
name='aasavari'
print(type(name))

#pgm4
x=(11,22,33,44)
print(type(x))

#pgm5
a={11,22,33,44}
print(type(a))

#pgm6
q=11
print(type(q))

#pgm7
# Set
setA = {11,22,33,44}
print(type(setA))

# allow duplicate values 
setB = {11,22,33,44,44,55,55}
print(setB)
print(len(setB))

#stores the value by index??
#print(setB[0])
for i in setB:
    print(i)

# program 2
# add()
setC = {11,22,33,44,55}   
setC.add(66)
print(setC)

setC.pop()
print(setC)

setC.remove(22)
print(setC)