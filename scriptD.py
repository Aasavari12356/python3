#pgm1
first_name='aasavari'
print(first_name.upper())
print(first_name.lower())
print(first_name.isupper())
print(first_name.islower())

#pgm2
last_name=' bedade '
print(len(last_name))
print(len(last_name.lstrip()))
print(len(last_name.rstrip()))
print(len(last_name.strip()))

#pgm3
last_name='avhad'
print(last_name.startswith('a'))
print(last_name.startswith('av'))
print(last_name.startswith('Avh'))

print(last_name.endswith('d'))
print(last_name.endswith('had'))
print(last_name.endswith('D'))

#pgm4
marks='1234'
print(marks.isalpha())
print(marks.isdigit())
print(marks.isalnum())
print(type(marks))

#pgm5
full_name=' a'
print(full_name.isspace())

#pgm6
firstN='aasavari'
print(firstN.capitalize())

e1='I Am Learning Python'
print(e1.istitle())

#pgm7
info=['aasavari','bedade','8108580033']
e2='@'.join(info)
print(e2)

#pgm8
email='aasavari@gmail.com'
e3=email.split('@')
print(e3)

#pgm9
emailaddress='aasavari'
print(emailaddress.find('a',6))
print(emailaddress.find('a',8))

#pgm10
#removeprefix()
email1= 'gmail.com@aasavari'
email2= 'gmail.com@pranil'
email3= 'gmail.com@sham'

print(email3.removeprefix('gmail.com@'))
students=['aasavari','pranil','sham']
lista=[]
for i in students:
    q1=i.removeprefix('gmail.com@')
    lista.append(q1)
    print(lista)

#pgm11
students = {
    "1":"chinmayadmin",
    "2":"poorvaceo",
    "3":"shamcustomer",
    "4":"nirnaymanager"
}

# roles = ["admin","ceo","customer","manager"]
# names = []
# #names =["chinmay","poorva","sham","nirnay"] 
# for name in students.values():
#   for role in roles:
#     if role in name:
#       q2 = name.removesuffix(role)
#       names.append(q2)
# print(names)

#pgm12
#swapcase()
a='hello'
print(a.swapcase())

#pgm13
#zfill()
name='aasavari'
name1='pranil'
print(name.zfill(10))
print(name1.zfill(10))
