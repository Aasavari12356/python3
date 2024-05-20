#upper()
first_name='aasavari'
q1=first_name.upper()
print(q1)

#lower()
last_name='BEDADE'
q2=last_name.lower()
print(q2)

#capatalise()
q3=first_name.capitalize()
print(q3)

#isupper
q4=first_name.isupper()
print(q4)

q5=last_name.isupper()
print(q5)

#islower
q6=first_name.islower()
q7=last_name.islower()
print(q6)
print(q7)

#isalpha()
q8=first_name.isalpha()
print(q8)

#isnum()
q9=last_name.isnumeric()
print(q9)

#iaalnum()
email='bedade123'
q10=email.isalnum()
print(q10)

#repalce()
info='i am learning js'
q11=info.replace('js', 'python')
print(q11)

#join()
info2=('aasavari','bedade','8108580033')
q12='@'.join(info2)
print(q12)

#endswith n startwith()
fruit='apple'
q13=fruit.endswith('e')
q14=fruit.endswith('le')
q15=fruit.startswith('a')
q16=fruit.startswith('ap')
print(q13)
print(q14)
print(q15)
print(q16)

#len()
str=' goa '
print(len(str))

q17=str.lstrip()
print(q17)
print(len(q17))

q18=str.rstrip()
print(len(q18))

q19=str.strip()
print(len(q19))


#slicing()



first_name = "chinmay"

# 0  1  2  3  4  5  6
# c  h  i  n  m  a  y
#-7 -6 -5 -4 -3 -2 -1

#print(first_name[startIndex:Endindex(included):steps])
print(first_name[1::])
print(first_name[1:len(first_name):])
print(first_name[0:6:2])
print(first_name[1:-1:1])
print(first_name[-5:-1])
print(first_name[-1:-7:-2])
print(first_name[::-1])            



