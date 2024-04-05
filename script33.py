
#Duck typing 

#class - 1
class Duck:
    def talk(self):
        print("quack quack")

# class -2
class Human:
    def talk(self):
        print("Hi hello")

def call_talk(obj):
    obj.talk()


duckA = Duck()
amol = Human()
call_talk(duckA)
call_talk(amol)

#pgm2
class Duck:
    def talk(self):
        print("quak quak")

class Human:
    def talk(self):
        print("hi hello")

class Dog:
    def talk(self):
        print("bow bow")

def talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    else:
        obj.bark()
            

duckB=Duck()
aasavari=Human()
moti=Dog()
call_talk(moti)

                            
        
#operator Overloading
print(1+1)
print("hello"+"world")
class BookX:
    def __init__(self,pages):
        self.pages=100

        

class BookY:
    def __init__(self,pages):
        self.pages=200

def __add__(self,others):
    return self.pages+others.pages  

Ramayan=BookX(100)
Mahabharat=BookY(200)

print(Ramayan.pages+Mahabharat.pages)
#print(Mahabharat + Ramayan)


#overriding

class WorldBank:
    def loan(self):
        print('I am loan from WorldBank')

    def save(self):
        print('I am save from WorldBank')


class SBI(WorldBank):
    def loan (self):
        print('I am loan from SBI ')

    def save(self):
        print('I am save from SBI') 



class PNB (WorldBank):
    def loan (self):
        print('I am from PNB')

    def save (self):
        print('I am save from PNB')


Ghatkopar= SBI()
Andheri=PNB()
Ghatkopar.loan()
Ghatkopar.save()


# class WorldBank:
#     def loan(self):
#         print("I am loan from WB")

#     def save(self):
#         print("I am save from WB")

# class SBI(WorldBank):
    
#     def loan(self):
#         print("I am loan from SBI")

#     def save(self):
#         print("I am save from SBI")
    
   
# class PNB(WorldBank):
#    def loan(self):
#         print("I am loan from PNB")

#    def save(self):
#         print("I am save from PNB")

# nagpur = SBI()
# wardha = PNB()

# nagpur.loan()
# wardha.save()


