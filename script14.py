info2 ={
    'first_name' : 'Aasavari',
    'last_name' : 'bedade' 

}
#3
info2.pop('last_name')
print(info2)
#4
info2.update({'rollNo':13})
print(info2)
#5
info2.popitem()
print(info2)
#6
info2.clear()
print(info2)

info4={
    "first_name":"Aasavari",
    "last_name":"bedade"
 }
for key in info4.keys():
    print(info4)

for value in info4.values():
    print(info4)

#1pgm
e= dict.fromkeys(['amol','ram','sham'])
print(e)
#pgm2
info3 = {
    "admin":"chinmay",
    "customer":"sameer",
    "support":"raj"
}
info3.setdefault('manager',None)
print(info3)

f= dict.fromkeys(["key1","key2","key3"])
print(f)

#tuple

listname = ['amol','raj','sham']
print(listname)
print(type(listname))
listname.append("ram")
print(listname)
listname[0]= "sarika"
print(listname)

lastname = ('bedade','avhad')
print(lastname)
print(type(lastname))

#pgm1
tupleB = (11,22)
tupleA = ("chinmay","raaj")
tupleC = (["ninad","vijeet"],["rohit","ameya"])
tupleD = 11,12
print(type(tupleD))

#pgm2
names = ("sonal","sham","ram")
print(names[0])
print(names[1])
print(names[2])

for x in range(len(names)):
    print(names[x])


for item in names:
    print(item)

#pgm3
tupleD = (11,22,33,44,33,55,33,66,77,88)
q= tupleD.count(33)
print(q)

w = tupleD.index(22)
print(w)