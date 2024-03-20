class Person:
    # fields or properties
    first_name='Aasavari'
    last_name='bedade'

    def walk(self):
        print('I am walking')

    def talk(self):
        print('I am talking')

savari=Person()
print(savari.first_name)    
print(savari.last_name)
savari.walk()
savari.talk()

aaryan=Person()
print(aaryan.first_name)
print(aaryan.last_name)
aaryan.walk()
aaryan.talk()

aaryan.first_name='amol'
aaryan.last_name='rao'
print(aaryan.first_name)
print(aaryan.last_name)

#pgm2
class PersonA:
    
    # constructor
    def __init__(self,fn,ln):
        self.first_name  = fn 
        self.last_name = ln 

    def talk(self):
        print('I am talking')

    def walk(self):
        print('I m walking')   
   
shreya=PersonA('soham','avhad')
janu=PersonA('sai','avhad')

print(shreya.first_name)
print(shreya.last_name)

print(janu.first_name)
print(janu.last_name)

janu.city='nashik'
print(janu.city)


#pgm3
class Vehicle:
    def __init__(self,color,type):
        self.color=color
        self.type=type

    def displaycolor(self):
        print(self.color)

    def displaytype(self):
        print(self.type)    

bmw = Vehicle('red','sedane')
audi=Vehicle('blue','suv')       
audi.displaytype()
          





# class PersonB:
#     # constructor
#     def __init__(self,fn,ln):
#         self.first_name  = fn 
#         self.last_name = ln 

#     def talk(self):
#         print("I am talking")
    
#     def walk(self):
#         print("I am walking")

# amol = PersonB("amol","rao")
# chinmay = PersonB("chinmay","deshpande")

# print(amol.first_name)
# print(amol.last_name)

# print(chinmay.first_name)
# print(chinmay.last_name)