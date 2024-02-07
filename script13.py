#pgm1
info={
    "first_name":"Aasavari",
    "last_name":"bedade",
    "age":30,
    "rollNo":13
}
info2=info
info2["age"]= 25
print(info)
print(info2)

info3=info.copy()
info3['age']=27
print(info)
print(info3)

#pgm2
info={
    "first_name":"Aasavari",
    "last_name":"bedade",
    "age":30,
    "rollNo":13
}


#pop(key)
info.pop("age")
print(info)

info.popitem()
print(info)

info.update({'city':'mumbai'})
print(info)

info.clear()
print(info)

#pgm3
info={
    "first_name":"Aasavari",
    "last_name":"bedade",
    "age":30,
    "rollNo":13
}
q1=info.get('age')
print(q1)

#pgm4
vehicle={
    'color':'white',
    'type':'mahindra',
    'regno':123
}
print(vehicle['color'])
for item in vehicle:
    print(item,vehicle[item])

for x in vehicle.keys():
    print(x)

for y in vehicle.values():
    print(y)

for k,v  in vehicle.items():
    print(k , v)