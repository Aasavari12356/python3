#list type
#pgm1

names=["aasavari","swaroop","shreeja","soham"]
print(names)
q1=len(names)
print(q1)

#pgm2

e= names.append('sham')
print(names)
print(e)

#pgm 3

names= ['shauo','janu','gaahu','sai']
names.clear()
print(names)

#pgm4

marks=['22','33','444','55555',"22","22"]
q2= marks.count(22)
print(q2)

#pgm5

fruits= ["mango","chikoo","apple"]
fruits.extend (["grapefruit","grapes"])
print(fruits)



fruits.insert(1,"papaya")
print(fruits)

#pgm6

fruits.pop(4)
print(fruits)

#pgm7

veg=['potato','tomato','cauliflowe','fenugreek']
veg.reverse()
print(veg)

veg.remove('tomato')
print(veg)

e2= veg.index('potato')
print(e2)




city = ["pune","mumbai","nagpur"]
city2 = city.copy()
city[1] = "surat"
print(city)
print(city2)




