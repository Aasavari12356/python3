import re
#RegularExpression
#pgm1 search
str = 'cat man mpo run  sun mat mm9'
e= re.search(r'm\w\w',str)
f = re.search(r'\wun',str)

#e # None---- python ---- false value
if e:
    print(e.group())
else:
    print("match not found !")

if f:
    print(f.group())
else:
    print("match not found")

#pgm2 findall
str1 = 'cat man mpo run  sun mat mm9'
q = re.search(r'\w\wo',str1)
if q:
    print(q.group())
else:
    print("not found")
q1= re.findall(r'm\w\w',str1)
q2= re.findall(r'\wat',str1)
#pgm3 
#match
strC = "mon tue wed thu fri sat"
q4 = re.match(r'm\w\w',strC)
if q4:
    print(q4.group())
else:
    print("not found")

#pgm4 split
strD= "This; is the core python's book"
q5= re.split(r"\W+",strD)
print(q5)

info= 'aasavari:8108580033'
print(re.split(r'\W+',info))

 #program 5 sub
strE= 'I m learning python'
q6= re.sub(r'python','javascript',strE)
print(q6)

# search(),findall(),match(),split(),sub()

# # [A-Z , a-z , 0-9] // alphanumric  // " ", %%%
# # [/W] --- " " and special symbol
# # [/w]* zero or more repetitions
# # \d  -- represents only digits
# # \b -- only blank space

#pgm6
str6= 'an apple a day keeps doctor away'
e2= re.findall(r'\ba[\w]*',str6)
print(e2)
 #pgm7
str7='The meeting will be conducted on 1st and 21st of each month'
e3=re.findall(r'\d[\w]*',str7)
print(e3)
#pgm8
# str8='one two three four five six seven eight nine ten'
# e4=re.findall(r'\b\w\w\w\w\w',str8)
# print(e4)
str8='one two three four five six seven 8 9 10'
e4= re.findall(r'\b\w{5}',str8)
print(e4)
#pgm9
str9= 'one two three four five six seven ninteen 9 8'
e5= re.findall(r'\b\w{4,}',str9)
print(e5)
#pgm10
str10='one two three four five six seven 8 9 '
e6= re.findall(r'\b\w{3,5}\b',str10)
print(e6)
#pgm11
str11='one two three four five six seven 8 9 10'
e7= re.findall(r'\b\d{1,}\b',str11)
print(e7)
e8= re.findall(r'\b\d+\b',str11)
print(e8)

# # a regular expression to find last word starting with 's'
# # a regular expression to find last word starting with 'o'

# # '\Z' 0 end of string
# # '\A' start of string

str12 = "o one two three four five six seven seventeen two"
# e9= re.findall(r'\bs[\w]*\Z',str12)
# print(e9)
e9 = re.findall(r'\bs[\w]*\Z',str12)
e10 = re.findall(r'\A\bo[\w]*',str12)
print(e9)
print(e10)

