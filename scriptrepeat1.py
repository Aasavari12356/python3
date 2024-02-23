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

