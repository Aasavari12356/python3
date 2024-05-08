# search()
# findall()
# match()
# split()
# sub()
# group()

# \w [a-z A-Z 0-9]
# \W [not [a-z A-Z 0-9]]
# \d - [0-9]
# \D - not[0-9]
# \b - blank space
# \A - match only start of string 
# \Z - match only at end 


#pgm1
import re
str='an apple a day keeps doctor away'
#list=re.findall(r'a[\w]*',str)
list1=re.findall(r'\ba[\w]*',str)
print(list)
print(list1)

#pgm2
import re
str = 'The meeting will be conducted on 1st and 21st of this month'
# 1st  21st

list2= re.findall(r'\b\d[\w]*',str)
list3=re.findall(r'\b\d[\d]*',str)
print(list2)
print(list3)


#pgm4
import re
str = "one two three four five six seven 8 9 10"
# [three,seven]
list4=re.findall(r'\b\w{5}',str)
print(list4)


list4A=re.search(r'\b\w{5}',str)
print(list4A)

list4B=re.match(r'\b\w{5}',str)
print(list4B)



#pgm5
list5=re.findall(r'\b\w{3,}',str)
print(list5)

str = "one two three four five six seven aa 8 9 10"
listD = re.findall(r'\b\w{3,5}\b',str)
print(listD)


str = "one two three four five six seven aa 8 9 10"
listD = re.findall(r'\b\d{1,}\b',str)
print(listD)

#pgm6
str = "one two three four five six seven aa 8 9 10 two"
listE=re.findall(r't[\w]*\Z',str)
print(listE)

str = "three one two three four five six seven aa 8 9 10 two"
listF1 = re.findall(r'\At[\w]*',str)
print(listF1)

