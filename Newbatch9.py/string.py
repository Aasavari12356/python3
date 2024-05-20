#string topic
# index starts from 0
#string can store ch by index. ----> True

#pgm1

city="pune"

# 0 1 2 3
# p u n e

print(city[0])
print(city[2])

#pgm2
#loops using for loop 
#with range

for x in range(len(city)):
    print(city[x])

#without range

for ch in city:
    print(ch) 

#pgm3
#while loop

city1="nagpur"

i=0
while(i<len(city1)):
    print(city1[i])
    i=i+1



#pgm4
# particular character or substring available or not 

fruit=["apple","grapes","papya"]
print("p" in fruit)
print("grapes" in fruit)
print("k" in fruit)

