print(1)
print(2)
print(3)
print(4)
print(5)

# program 2
#range(startIndex,endIndex (not included),steps)
#default startIndex  - 0

for x in range(3):
    print(x)

for x in range(1,10):
    print(x)

for x in range(2,21,2):
    print(x)

for x in range(20,1,-2):
    print(x)

for x in range(50,4,-5):
    print(x)

# program 3
# break statement with for 

for x in range(10,5,-1):
    if x == 7:
        break
    print(x) # 10 # 9 # 8

for x in range(10,5,-1):
    print(x) 
    if x == 7:
        break

# program 4
for x in range(1,5): # 2 # 3 # 4
    if x == 3:
        continue
    print(x) # 1 # 2 # 4

for x in range(10,5,-1): 
    if x == 7:
        continue
    print(x) 

    