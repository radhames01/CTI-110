# Program that calculate the Areas of Rectangles
# 12 Jun 2017
# CTI-110 M3T1 - Areas of Rectangles
# Radhames Flete Perez

# area=leght * width
# A1-2=area
# L1-2=legth
# W1-2=width
 


L1=int(input("enter the legth for the first rectangle\n"))
W1=int(input("enter the width for the first rectangle\n"))
A1=L1*W1
print("The area of the first rectangle is:",A1," \n")

L2=int(input("enter the legth for the second rectangle\n"))
W2=int(input("enter the width for the second rectangle\n"))
A2=L2*W2
print("The area of the second rectangle is:",A2," \n")

print("The area of the first rectangle is:",A1)
print("The area of the second rectangle is:",A2," \n")

if A1>A2:
    print("the first rectangle has the greater area.\n")
if A1<A2:
    print("the Second rectangle has the greater area.\n")
if A1==A2:
    print("Both rectangles has the same area.\n")
