#pgm1
class Person:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln


    def display_name(self):
        print(self.first_name+self.last_name)   

aasavari=Person("aasavari","bedade")
amol=Person("amol","rao") 

print(aasavari.first_name)
print(amol.first_name)

print(aasavari.last_name)
print(amol.last_name)

aasavari.display_name()
amol.display_name()

#pgm2

# class PersonA:
#     country = "India"
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln

#     def __display_name(self):
#         print(self.first_name+self.last_name)

# sawari=PersonA("shona","bedade")
# print(sawari.first_name)
# print(sawari.last_name) 
# print(sawari.country)    

# amol=PersonA("amol","rao")
# amol.country="Bharat"
# print(amol.first_name)
# print(amol.last_name) 
# print(amol.country)

# chinamay=PersonA("chinmay","dani")
# print(chinamay.country)

# PersonA.changeCountry("Hindustan")
# print(sawari.country)
# print(amol.country)
# print(chinamay.country)


class Person2:
    country = "bharat"
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)

    @classmethod
    def changeCountry(cls,cnty):
        cls.country = cnty

amol = Person2("amol","rao")
chinmay = Person2("chinmay","deshpande")
ninad = Person2('ninad',"dani")

print(amol.firstName)
print(amol.lastName)
print(amol.country)
amol.country = "india"
print(amol.country)
print(chinmay.country)
print(ninad.country)
Person2.changeCountry("Hindustan")
print(amol.country)
print(chinmay.country)
print(ninad.country)