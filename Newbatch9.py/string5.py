
#pgm1

birthyear=[1990,1991,1992,1993]
age=[]
for x in birthyear:
    a=2024-x
    age.append(a)
print(age)

#pgm2

marks=[56,67,78,94,77]
above75=[]
for x in marks:
    if x >= 60 and x % 2 == 0:
        above75.append(x)

print(above75)         



#pgm3
a=[11,22,33]
total=0
for x in a:
    total=total + x

print(total)    

#pgm4
cities=['mumbai','pune','nagpur']

for i in cities:
    print('welcome '+ i)




