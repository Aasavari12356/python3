#lambda function
def add(x,y):
    return x+y
q=add(2,3)
print(q)

add= lambda x,y:x+y
f=add(45,5)
print(f)

#pgm2
multiply= lambda x:x*x
w=multiply((4))
print(w)

#pgm3
#function as parameter as to another parameter
add=lambda x,y:x+y
def addition (fn,x,y):
    f=fn(x,y)
    return f
e2=addition(add, 50,10)
print(e2)


sub=lambda a,b:a-b
def subtraction (fn,a,b):
    f1=fn(a,b)
    return f1
e3=subtraction(sub,30,10)
print(e3)

#pgm4
# function as a return type 

def add ():
   return lambda x,y:x+y
e1=add()
print(e1)
e4=e1(12,3)
print(e4)


 