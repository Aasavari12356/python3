info = ['aasavari','bedade',30,13]
print(info[0])   #retrive

info[0]='shona'
print(info[0])   #replace

info.append('mumbai')   #add
print(info)

info.remove('bedade')   #delete
print(info)

#pgm2

info2 ={

     'firstname': 'aasavari' ,
     'lastname' :  'bedade'  ,
     'age'      :'30' ,
     'rollnumber':'13'
}

print(info2)
print(type(info2))

print(info2['firstname'])

print(info2['lastname'])

info2['lastname'] = 'avhad'
print(info2) 

info2['city'] = 'nashik'
print(info2)

info2.pop('age')
print(info2)

#revision

vechicle ={

    'color':'white' ,
    'type' :'mahindra'

}
print(vechicle)

print(vechicle['type'])

vechicle['color'] = 'black'
print(vechicle)

vechicle['reg.no.'] = (1343)
print(vechicle)

vechicle.pop('type')
print(vechicle)

#pgm3

fruits = ['apple','banana','chikoo','apple']
print(fruits)
print('apple' in fruits)
fruits.count('apple')
print(fruits)
