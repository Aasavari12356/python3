names=['ankur','amisha','amar','aerna']
#retrive
print(names[0])

# add
names.append('aasha')
print(names)

# update
names[1]='anjli'
print(names)

# delete
names.pop()
print(names)
names.pop(2)
print(names)

# in operator
print('ankur in names')
if('ankur is in names'):
    print('complete names is available')
else:
    print('something is missing')    

# for range loop, without range, while
country=['India','myanmar','korea','japan']

for x in range(4):
    print(x)
    print(country[x])
    

for x in country:
    print(x)    


i1 =0
while i1 <len(country):
    print(country[i1])
    i1=i1+1

#methods in list

vegi=['tomato','brinjal','bitter gourd','potato']
#append
vegi.append('capsicum')
print(vegi)

#delete
vegi.pop()
vegi.pop(3)
vegi.remove('brinjal')
print(vegi)

#clear
num=[11,22,43]
num.clear()
print(num)

#insert
num.insert(0,1)
num.insert(1,11)
num.insert(2,111)
num.insert(3,1111)
num.insert(2,11111)
print(num)

#extend
a=[11,22,33]
b=[44,55,66]
a.extend(b)
print(a)
print(b)
    
