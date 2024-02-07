x=10
print(x)

h=[11,22,33,44,55]
print(h)
print(type(print(h)))
print(h[1])

#pgm2
names= ["aasavari","shravani","kunal","shreeja","swaroop"]
print(names[2])

#pgm3
#using range

for x in range(len(names)):
    print(names[x])

city=["mumbai","nashik","pune","nagpur"]
print(city)
q1=len(city)
print(q1)
print(q1-1)

#pgm4
#without range
fruits=["mango","apple","banana"]
for items in fruits:
    print(fruits)

#pgm5
vegetables=["brinjal","tomato","potato"]
print("brinjal" in vegetables)
if("brinjal" in vegetables):
    print("vegetables are available")
else:
    print("vegetables are not available")