#pgm1
names= ["Aasavari","Bedade", "ram"]
print(type(names))

info= ["Aasavari","bedade",30, 13]

info={
    "first-name":"Aasavari",
    "last-name":"bedade",
    "age":30,
    "rollno":13

}
print(info)
print(type(info))

#pgm2
names= ["sawari","shreya","shrauo","swara"]
print(names)
print(names[1])

names.append("shreeja")
print(names)

names.pop(3)
print(names)

names.remove("shrauo")
print(names)

names[0]="soham"
print(names)

#pgm3
names= ['raj','ram','ramesh','roham']
#in range
for x in range(len(names)):
    print(x)
    print(names[x])
#without range
    for item in names:
        print(item)

#pgm4
student={
    "first_name":"Aasavari",
    "last_name":"bedade",
    "age":30,"rollNo":13
}
print(student)

print(student["first_name"])

student["last_name"]="avhad"
print(student)

student['city'] = "pune"
print(student)
student.pop('first_name')
print(student)