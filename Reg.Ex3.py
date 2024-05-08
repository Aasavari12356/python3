#pgm1
import re
str = "anil akhil anant an ak arun arati arundhanti abhjit ankur"
q1=re.findall(r'\ba[nk][\w]*\b',str)
print(q1)

#pgm2
import re

#dd mm yyyy

str2='Aasavari 13-09-1993 , Kunal 09-10-1995 , Monika 15-4-1989'
q2=re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str2)
q3=re.findall(r'\d{2}-\d{2}-\d{4}',str2)
print(q2)
print(q3)

#pgm3
str3="Hello world"
q4=re.search(r'^He[w]*',str3)
if q4:
    print("string starts with He")
else:
    print("string does not starts with He")


#pgm4
str4="Hello World"
q5=re.search(r'[w]*$ld',str4)
if q5:
    print('string ends with ld')
else:
    print('string does not end with ld ')    