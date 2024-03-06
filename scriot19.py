#list compression----------->o/p= list
#[expression:loop:condn.]
#table of 2
q=[1,2,3,4,5,6,7,8,9,10]
x=[i*2 for i in q]
print(x)
#even no.
q1=[i for i in q if i%2==0]
print(q1)
#odd no.
q3=[i for i in q if i%2!=0]
print(q3)
#make every charcter to upper
names = ["chinmay","sarika","poorva","tanmay"]
x1=[i.upper() for i in names]
print(x1)

names = ["chinmay","sarika","poorva","tanmay"]
x2=[i.upper() for i in names if i.endswith("y")]

names = ["chinmay","sarika","poorva","tanmay"]
x3=[i.upper() for i in names if i.endswith("a")]
print(x3)

z=[
    {
     "firstName":"chinmay",
        "lastName":"deshpande",
        "age":19,
        "vehicle":True
},
{
     "firstName":"tnmay",
        "lastName":"deshmukh",
        "age":17,
        "vehicle":False
},
{
     "firstName":"chikoo",
        "lastName":"dighe",
        "age":39,
        "vehicle":True
},
{
     "firstName":"mayuri",
        "lastName":"chavan",
        "age":19,
        "vehicle":False
}]

# s3=[z['firstName'] for i in z ]
# print(s3)

s4=[11,22,33,44]

s5=[i for i in s4 if i % 2 ==0]
print(s5)

s5=[i for i in s4 if i % 2 !=0]
print(s5)

#ternaray operator(error)
# s6= ["even" if i%2 == 0 else "odd" for i in s4]
# print(s6)
#x10 = ["even" if x%2 == 0 else "odd" for x in x8](e.g.)


# students 
students  = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":19,
        "vehicle":True
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":4,
        "vehicle":True
    },
    {
        "firstName":"pranali",
        "lastName":"pansare",
        "age":19,
        "vehicle":False

    },



    {
        "firstName":"tavish",
        "lastName":"anade",
        "age":39,
        "vehicle":True
    }

]

c3=[i['firstName'] for i in students if i['age'] >= 18 and i['vehicle'] == True]
print(c3)

c4=[i['firstName'] if i['age'] > 18 and i['vehicle'] else None for i in students ]
print(c4)

q4 = [x for x in c4 if x != None]
print(q4)

#["chinmay":'candrive',"sarika":"cannot drive","pranali":"cannot","tavish":"candrive"]

# c5=[i['for i in studnts]