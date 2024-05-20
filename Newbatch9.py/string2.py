#pgm1
listA=['ajay','sameer','kiran']
print(listA)
print(type (listA))

#pgm2
first_name='sameer'
print(type(first_name))

#string stores the values by index
print(first_name[0])


#can we update the list n string
listA[0]='aman'
print(listA)   #list can update

# first_name[0]='a'
# print(first_name)   #string can't update

#pgm3
#Loops

fruits="apple"

7
for x in range(len(fruits)):
    print(x)
    print(fruits[x])

for x in fruits:
    print(x)  

i=0
while(i<len(fruits)):
    print(fruits[i])
    i=i+1      


#pgm4
city = "pune"
# enup
rev = "" 
for char in city:
    rev =  char + rev
            #p   + ""  ------> p
            #u   + p   ------> up
            #n   + up  -------> nup
            #e   + nup -------> enup
print(rev)


name="ankur"
rev=""
for char in name:
    rev= char + rev

print(rev)  


#slicing

#pgm5

city3 = "pandharpur"

#   0   1    2    3   4  5   6   7   8   9
#   p   a    n    d   h  a   r   p   u   r
#  -10  -9  -8   -7  -6 -5   -4 -3  -2  -1
#city3[startIndex:endIndex(not included):steps]


print(city3[1::])
print(city3[2:5:])
print(city3[0:9:2])
print(city3[-1::])
print(city3[::-1])
print(city3[-10:5:])

