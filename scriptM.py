#instance method
class Person:
    #constructor
    def __init__(self,fn,ln):
        self.firstname=fn #instance variable
        self.lastname=ln  #self=refn
        #instance method

    def displayname(self):
        print(self.firstname+self.lastname)

    def updateName(self,ln):
        self.lastname =ln

#object
Boy=Person('swarup','avhad')
print(Boy.firstname)
print(Boy.lastname)

#Boy.displayname()
Boy.updateName("dani")

# class instance , class method

# class PersonB:
#     country:"India"


#     def __init__(self,fn,ln):
#         self.firstname=fn
#         self.lastname=ln

#     def updateName(self,fn,ln):
#         self.firstname=fn
#         self.lastname=ln

        # #class method
        # @classmethod
        # def updateCountry(cls,cnty):
        #     cls.country=cnty

# h=PersonB('ajay','dhawan')
# print(h.firstname)
# print(h.lastname)
# print(h.country)


class PersonB:
    country = "India"

    # constructor
    def __init__(self,fn,ln):
        # instance variable
        self.firstName = fn 
        self.lastName = ln

    # instance method
    def updateName(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    # class method
    @classmethod  
    def updateCountry(cls,cnty):
        cls.country = cnty  

h = PersonB("amir","jain")
print(h.firstName)
print(h.lastName)
print(h.country)
h.country="Bharat"
h2=PersonB('neha','rane')
print(h2.firstName)
print(h2.lastName)
print(h2.country)


# static method 
# count number of objects 

class PersonC:
    count=0
    country="India"

    def __init__(self,fn,ln):
        self.firstname=fn
        self.lastname=ln
        PersonC.count=PersonC.count+1

    def displayName(self):
       print( self.firstname+self.lastname)


    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty

        @staticmethod
        def countobj():
           return PersonC.count
        
amol  = PersonC("akay","singh")
raj = PersonC("ajit","rane")

a = PersonC.countobj()
print(a)




    

    

