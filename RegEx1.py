#\w[az AZ 09]
# \W [ non alpha numeric (special cha n all)]


#pgm1
#only one occurance
# method1= search
import re
str="man mop sun hat"
result= re.search(r'm\w\w',str)
print(result.group())
if result:
    print(result.group())

#pgm2
# method2= findall
# to find out all occurance, it gives all the occurances
str2="man sun map ran fun map rap shape mate fate"
list= re.findall(r'm\w\w',str2)
print(list)

#pgm3
# method3= match
# start of the string search karna hai


str3 = "python is good language to learn"
q3 = re.match(r'p\w\w',str3)
print(q3.group())
if q3:
    print(q3.group())

#pgm4
# method4= split

import re
str4="This ; is the : 'Core' python's book"
result1= re.split(r'\W+',str4) 
print(result1)   


#pgm5
# method5= subtitute
str5= " I am learning javascript"
q2= re.sub(r'javascript','python',str5)
print(q2)

#pgm5.1
str6= " i am learning javascript and advance javascript"
q3= re.sub(r'javascript','python',str6)
print(q3)