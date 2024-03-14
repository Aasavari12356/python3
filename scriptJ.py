#list compression
lst=[1981,1984,1985,1995]
ages=[]
for x in lst:
    ages.append(2024-x)
print(ages)  

#pgm2
#[expresion-loop-condition]
q=[2024-x for x in lst] 
print(q)

#pgm3
numbers=[1,2,3,4,5,6,7]
q1=[x*x for x in numbers]
print(q1)

#pgm4
q2=[x for x in numbers if x % 2 ==0 ]
print(q2)

q3=[x for x in numbers if x % 2 != 0]
print(q3)

q4=["even" if x % 2 == 0 else "odd" for x in numbers]
print(q4)

#pgm5
names=['ram','sham','priya','leela']
q5=[x for x in names if len(x)>4]
print(q5)