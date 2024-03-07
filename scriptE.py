name='aAasavari'
print(type (name))
name1=['sham','ram']
print(type(name1))
info={
    'name':'sawari',
    'age':31
}
print(type(info))
#--------------------------------------->

#pgm2
flower=['lilly','rose']
flower[0]='jasmine'
print(flower)

# flower1=('lotus','jasmin')
# flower1[0]='rose'
# print(flower1)

#pgm3
#does  tuple stores the value by index??
# how to define tuple
tupleA = ("A","B","C")
print(tupleA)
print(type(tupleA))
print(tupleA[0])

#pgm4
#for with range
for x in range (3):
    print(x)
    print(tupleA[x])

#without range
for item in tupleA:
    print(item)

#while
i=0
while(i<3):
    print(tupleA[i])
    i=i+1

#pgm4
tupleB=11,12
print(tupleB)
print(type(tupleB))
tupleC=(11,22,33)
a,b,c=tupleC
print(tupleC)
print(a)
print(b)