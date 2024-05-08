#pgm1
names=['arjun','amol','aakash','amir']
names2=names
print(names2)
names2[1]='aasha'
print(names)
print(names2)


#pgm2
city=['mumbai','nashik','pune']
city2=city
print(city2)
city2[1]='nagpur'
print(city2)
print(city)

#pgm3
names=['arjun','amol','aakash','amir']
names.pop()
print(names)
names.pop(1)
print(names)
names.remove('aakash')
print(names)

#append()
vegi=['tomato','potato','brinjal']
vegi.append('capsicum')
print(vegi)

#sort()
vegi.sort()
print(vegi)

#reverse()
vegi.reverse()
print(vegi)

#insert()
vegi.insert(2,'bottole gourd')
print(vegi)

#clear()
vegi.clear()
print(vegi)

#extend()
a=[11,22,33]
b=[44,55]
a.extend(b)
print(a)


#index()
fruits=['apple','papaya','orange','grapes','apple']
a=fruits.index('apple')
print(a)

#count()
b=fruits.count('apple')
print(b)