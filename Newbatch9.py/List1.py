#pgm1
names=['ram','sheela','aman','rohit']
print(names)
print(names[0])

# #pgm2
#value retrive
print(names[1])

#value add
names.append('meera')
print(names)

#value update
names[2]='raj'
print(names)

#value delete
names.pop()
print(names)
names.pop(1)
print(names)


#pgm3
country=['India','korea','japan','peru']

print(country)
print(country[0])
country.append('thiland')
print(country)
country[2]='malysia'
country.pop()
country.pop(1)
print(country)

#pgm4
# any particular element available in list

vegetables=['tomato','brinjal','onion','potato']
#in operator

print('potato in vegtables')
if('onion in vegetables'):
    print('vegi is available')
else:
    print('vegi is not available')    


#pgm5
## loop in list

city=['mumbai','delhi','kolkota','chennai']

#for in range

for x in range(4):
    print(x)
    print(city[x])

#without range
for x in city:
    print(x)


#
country = ["india","pakistan","srilanka","japan"]
# range(start,end ,step)
# range(4) # by default - 0
for x in range(4):
    #print(x)
    print(country[x])

for cntry in country:
    print(cntry)    


