# # for and while 
# # break and continue
# #range(startIndex, endIndex (not included),steps )
# # by default start index is 0



#for loop with range
#pgm1
for x in range(1,11):
    print(x)

for x in range(2,21,2):
    print(x)    

for x in range(50,4,-5):
    print(x)    

for x in range(5):
    print(x*2) 


for x in range(5):
    if x == 3:
        break
    print(x)   


for x in range(5):
    if x == 3:
        print(x)
        break


for x in range(5):
    if x==3:
        continue
    print(x)

for x in range(6):
    print(x)
    if x ==3:
        continue   

for x in range(6):
    if x == 3:
        continue
    print(x)     
       



#for loop without range

#pgm2
list=[1,2,3,4,5,6] 
for x in list:
    print(x)     


# #while loop

i=0
while(i<=3):
    print(i)
    i=i+1   




i2=0
while(i2<=2):
    
    print('hi')
    i2=i2+1  


i3=10
while(i3>0):
    print(i3)
    i3=i3-1

i4=0
while(i4<=20):
    print(i4)
    i4=i4+2

i5=50
while(i5>4):
    print(i5)
    i5=i5-5

 


# i6 = 1
# while(i6 <= 5):
#     if i6 == 4:
#         break
#     print(i6) #1
#     i6 = i6 + 1 

# i7=1
# while(i7<=5 ):
#     print(i7)
#     if i7 == 4:
#         break
#         i7=i7+1 


# break and continue with while loop

i6 = 1

while(i6 <= 5):
    print(i6) # 1 # 2
    if i6 == 2:
        break
    i6 = i6 + 1 # 2


i6 = 1
while(i6 <= 5):
    if i6 == 2:
        break
    print(i6) #1
    i6 = i6 + 1 # 2

i7 = 5
while(i7 >= 1):
    print(i7) # 5 # 4 # 3  # 2
    if i7 == 2:
        break
    i7 = i7 - 1 # 4 # 3 # 2


i8 = 1
while(i8 <= 5):
    if i8 == 3: 
        i8 = i8 + 1 # 4
        continue
    print(i8) # 1 # 2 # 4 #5
    i8 = i8 + 1 # 2 # 3 # 5 # 6