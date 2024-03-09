#1
def addA(x,y):
    return x+y
q1=addA(2,3)
print(q1)

#2  ERROR Missing positional arguments
# def addB(x,y):
#     return x+y
# q2=addB()
# print(q2)

#3
def addC(x=3,y=4):
    return x+y
q3=addC()
print(q3)

#4
def addD(x=2,y=2):
    return x+y
q4=addD(5,5)
print(q4)

#5
def addF(x,y):
    return x+y
q5=addF(y=10,x=20)
print(q5)

#6
def myfunction():
    a=1
    b=2
    a=a+1
    print(a)
    print(b)
q6=myfunction()
#print(a)

#7
a=1
def myfunction2():
    a=5
    b=6
    a=a+1
    print(a)
    print(b)
q7=myfunction2()
print(a) 

#8
a=10
def myfunction3():
    print(a)
    print(10)
q8=myfunction3()
print(a)  

#9
h=10
def myfunction4():
    global h
    h=99
    print(h)
q9=myfunction4()
print(h)    

#10
#practice again again


def addD(*args):
    print(args)
    total = 0
    for x in args:
        total = total + x
    return total
e3 = addD(1,2,33,4,55,6,7,88,9,55,66,77,8,99,44,55)
print(e3)


#11
def addinfo(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs
e4 = addinfo(first_name = "shivani",last_name ="hedau",age= 30)
print(e4)