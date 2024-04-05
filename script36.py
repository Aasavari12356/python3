#compile time(1)
#pgm1
# def add ():
# print(8+8)    

#run time(2)
#pgm2
# x=int(input("Enter the value of 1"))
# y=int(input("Enter the value of 2"))
# print(x/y)

# listA=[11,22,33,44]
# print(listA[4])

#pgm3
# def calculateBonusPlusSalary(Salary):
#     return 0.10*Salary
# print(calculateBonusPlusSalary(1000))
# print('hello')
# try:
#     x=int(input('Enter the value of 1'))
#     y=int(input('Enter the value of 2'))
#     print(x/y)
# except Exception:
#     print('Invalid Input')
# print('bye')    

# #pgm4
# try:
#     names=['surbhi','pallu','lalita']
#     x=int(input('Enter the value A'))
#     y=int(input('Enter the value B'))
#     print(x/y)
#     print(names[3])
#     print(a)

# except ArithmeticError:
#     print('Invalid input') 
# except IndexError:
#     print('increse value of your list')
# except NameError:
#     print('not defined')
# except Exception:
#     print('something went wrong') 
# print('bye')   

#pgm5
# try:
#     names=['sarika','amol','pavan'] 
#     x=int(input('Enter the value A') )
#     y=int(input('Enter the value B') ) 
#     print(x/y)

# except ArithmeticError:
#     print('invalid number')

# else:
#     print('hello')   

#pgm6
# try:
#     names=['sarika','amol','pavan'] 
#     x=int(input('Enter the value A') )
#     y=int(input('Enter the value B') ) 
#     print(x/y)

# except ArithmeticError:
#     print('invalid number')

# finally:
#     print('I will always execute')      


#pgm7
# print('hello')
# try:
#     x=int(input('Enter the value A'))
#     y=int(input('Enter the value B'))
#     print(x/y)
# except ArithmeticError:
#     print('invalid number')
# else:
#     print('hi')
# finally:
#     print('I will always execute')

# print('bye')    

#logical error
# def avg(list):
#     total=0
#     for x in list:
#         total=total+x
#     avg=total/len(list)  
#     return total,avg

# try:
#     t,a=avg([2,3,4,5,"a"]) 
#     print(t)
#     print(a)
# except TypeError:
#     print('type error')
# except ZeroDivisionError:
#     print('Zero division,cannot pass empty list')
# except Exception:
#     print('error')             
    

# try:
#     x=int(input('Enter the the number:'))
#     y=1/x
# finally:
#     print('we are not catching the exception...')
# print('the inverse is',y) 

#handling the assertion

# try:
#     x=int(input('Enter the number between 5 and 10'))
#     assert x>=5 and x<=10
#     print('enter the number is',x)
# except AssertionError:
#     print('the condition is not fulfilled')    



class lowBalance(Exception):
    def __init__(self,msg):
        self.msg=msg

def check(dict):
    for k,v in dict.items():
        if (v < 20000):  
            raise lowBalance('the value is below 20k,please add amount') 

try:
    bank={'ram':1000,'sameer':300000,'ajay':50000} 
    check(bank)
    print('all above 20 thousand')
except lowBalance as me:
    print(me)    





    
