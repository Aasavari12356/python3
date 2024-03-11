#pgm1
class person:
    # properties and method
    first_name= 'aasavari'
    last_name= 'bedade'
    age= 31


    def display(self):
        print(self.first_name+ self.last_name)


akay=person()
print(akay.first_name)
print(akay.last_name)
print(akay.age)
akay.display()

kavya=person()
print(kavya.first_name)
print(kavya.last_name)
print(kavya.age)
kavya.display()

kavya.first_name="kavya"
kavya.last_name="das"
kavya.age=25
kavya.city="nagpur"
print(kavya.first_name)
print(kavya.city)

#pgm2
class person:
 def __init__(self,fn,ln,age):
    self.first_name=fn
    self.last_name=ln
    self.age=age


def display(self):
    print(self.first_name+self.last_name)

def displayAge(self):
    print(self.age)

akay = person("akay","puri",20)
aasavri = person("aasavari","bedade",23)
kavya = person("kavya","das",45)

#akay.display()
#aasavri.display()
#aasavri.displayAge()
#print(aasavri.age)

#pgm5

# program 3 
class Vehicle:
    def __init__(self,color,type):
        self.color  = color 
        self.type = type

    def displayColor(self):
        print(self.color)

audi = Vehicle("red","sedane")
bmw = Vehicle("blue","SUV")
audi.displayColor()