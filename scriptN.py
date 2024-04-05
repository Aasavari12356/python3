# program 1
# single inheritance 
# parent - constructor , child no constructor



class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln
        self.adharNo= adharNo

    def displayName(self):
        print(self.firstName  + self.lastName)

amit = Student("amit","rahane","12345")
print(amit.firstName)
print(amit.lastName)
print(amit.adharNo)
amit.displayName()


# class Teacher(Student):
#     salary:100000
#     def displaySalary(self):
#         print(self.salary)

# amit1=Teacher('ajay','pansare','234')
# print(amit1.firstName)
# print(amit1.lastName)
# print(amit1.adharNo)
# print(amit1.salary)
# amit1.displayName()

class Teacher(Student):
    salary = 100000
    def displaySalary(self):
        print(self.salary)

amolT = Teacher("amolT","raoT",123)
print(amolT.firstName)
print(amolT.lastName)
print(amolT.adharNo)
print(amolT.salary)

amolT.displayName()
amolT.displaySalary()
        
#pgm2
#single inheretance

class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstname=fn
        self.lastname=ln
        self.adharNo=adharNo

    def displayName(self):
        print(self.firstname+self.lastname)    

class Teacher(Student):
    def __init__(self, fn, ln, adharNo,salary):
        super().__init__(fn, ln, adharNo)
        self.salary = salary

        def displaySalary(self):
            print(self.salary)

aasavari=Teacher('aasavari','bedade',1234,20000)      
print(aasavari.firstname)  
print(aasavari.lastname)
print(aasavari.adharNo)
print(aasavari.salary)  

aasavari.displaySalary()


        