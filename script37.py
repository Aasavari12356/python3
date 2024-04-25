# A single try block can be follwed by several except block                    -----> True
# Multiple except blocks can be used to handle multiple excpetions             -----> True
# We cannot write except block with try block                                  -----> True
# We cannot write try block with except block                                  -----> False
# Else block and finally block are not compulsory                              -----> True
# When there is no exception raised else block is executed after try block     -----> True
# Finally block is always executed                                             -----> True


#pgm1

print("Start")
try:
    names=["sameer","veena","kirti"]
    a=int(input("Enter the input of A"))
    b=int(input("Enter the input of B"))
    print(a/b)
    print(names[2])

except ArithmeticError:
    print("Enter correct input number...")

except IndexError:
    print("please add more value in list")

else:
    print("Done")    

finally:
    print("I always print")




#pgm2
# print("hello")
# try:
#     print(23/0)
# finally:
#     ("I always run...")    

# print("bye")    

#pgm3
def calAvg(list):
    [11,22,33][4]
    total=0
    for item in list:
        total=total+item
    avg= total/len(list) 
    return total,avg

try:
    a,b= calAvg([11,22,33,"a"])


        



