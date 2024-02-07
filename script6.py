#conditional statement
#pgm1

numT = 13
if numT > 0 and numT <=5:
    print("5% Discount")
if numT > 5 and numT <= 10:
    print("10% Discount")
if numT > 10:
    print("15% Discount")

#pgm2
numT = -17
if numT > 0 and numT <= 5:
    print("5% Discount")
elif numT > 5 and numT <= 10:
    print("10% Discount")
elif numT > 10:
    print("15% Discount")
else:
    print("Incorrect inputs")
