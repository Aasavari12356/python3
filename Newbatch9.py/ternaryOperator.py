#ternary operator
#pgm1

a=10
b=5

if a > b :
    print('a is greater than b')
else:
    print('b is less than a')    

print('a is greater than b') if a > b else('b is greater than a')   


#pgm2

age=16

f=('can drive') if age >= 17 else('cant drive')
print(f)