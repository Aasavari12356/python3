# program 1
# x , y   ---- formal arguments 
# 12, 13  ---- actual arguments 
def addA(x,y):
    return x+y 
q1=addA(2,4)
print(q1)


# program 2 "positional argument"
def subB(x,y):
    return x-y
q2=subB(y=15,x=20)
print(q2)

# program 3 "default arguments"
def mulA(x=2,y=5):
    return x*y
a1=mulA()
a2=mulA(x=3,y=1)
print(a1)
print(a2)

# program 4 - variable length arguments
def addAll(*args):
    print(args)
    total=0
    for i in args:
        total=total+i
        return total
e5=addAll(1,2,3,4,5,6,7,8,9,99,88,77,66,5,44,33,22,11)


# def addAll(*args):
#     print(args)
#     total = 0 
#     for i in args:
#         total  =  total + i
#     return total
    

# e5 = addAll(1,2,3,4,5,6,73,4,5,6,6,55,6,7,3,4,5,6,7)
