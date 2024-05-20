#script8
#list method
names=['ajay','namit','manas']
#retrive
names[0]='ankur'
print(names)
#update
names[2]='manoj'
print(names)
#add
names.append('akshay')
names.insert(1, 'manasi')
print(names)
#pop
names.pop()
names.pop(2)
print(names)
#in
print('tanmay' in names)

#pgm2 Dictionary
info={
    "first name":"Aasavari",
    "last name":"bedade",
    "roll no": 13
}
print(info)
#retrive
e=info["first name"]
print(e)
#update
info["last name"]='avhad'
print(info)
#add
info["city"]="nashik"
print(info)
#delete
info.pop("roll no")
print(info)

#pgm3
vechile={
    "color":"white",
    "model no": 234,
    "color":"black"
}
print(vechile)
#length
print(len(vechile))
#in
print("type" in vechile)
#duplicate key
print(vechile)

# script9
info={
    "first name":"Aasavari",
    "last name":"bedade",
    "roll no": 13
}
print(type(info))
print(info['first name'])#retrive
info['first name']='sawari'#update
print(info)
info['city']='mumbai' #add
print(info)
info.pop('last name')
print(info)

vehicle={
    'color':'red',
    'type':'sedane'
}
#vehicle.clear()
# del()
# print(vehicle)

#vehicle.pop('color')
e = vehicle.popitem()
print(e)
print(vehicle)

info={
    "first name":"Aasavari",
    "last name":"bedade",
    "roll no": 13
}

for i in info.keys():
    print(i)

for i in info.values():
    print(i)

for i in info.items():
    print(i)

print(info['first name'])
for i in info:
    print(i,info[i])



# list / dictionary 

# program 1
# upper()
first_name = "chinmay"
print(len(first_name))
e = first_name.upper()
print(e)


# lower()
last_name = "Deshpande"
e2 = last_name.lower()
print(e2)


middle_name = "SHIRISH"
e3 = middle_name.isupper()
print(e3)

e4 = e2.islower()
print(e4)

# lower(), upper() , islower() ,isupper()
# program 2

city = "pune"
e5 = city.startswith("pu")
e6 = city.startswith("P")
print(e5)
print(e6)

e7 = city.endswith('e')
e8 = city.endswith('une')
print(e7)
print(e8)

city2 = "chandrapur"
e9 = city2.count('a')
print(e9)

# program 3

city3 = " wardha"
print(len(city3))
e10 = city3.lstrip()
print(e10)
print(len(e10))

city4 = " wardha "
print(len(city4))
e11 = city4.rstrip()
print(len(e11))

city5 = " wardha "
e12 = city5.strip()
print(len(e12))

# program 4
info = "I am learning javascript"
e13 = info.replace("javascript","python")
print(e13)
print(info)


# program 5
e14 = "123".isdigit() #  0 - 9
print(e14)

e15 = "1233#"
e16 = e15.isalpha()
print(e16)

e17 = e15.isalnum()
print(e17)

e18 = "hello"
e19 = "1234"
e20 = "h123"
e21 = "h12#"
print(e19.isalnum())
print(e20.isalnum())
print(e21.isalnum())




