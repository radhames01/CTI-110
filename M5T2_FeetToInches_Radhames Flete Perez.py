# Program that conver feet to inches
# 26 Jun 2017
# CTI-110 M5T2_FeetToInches 
# Radhames Flete Perez






# 1 Foot = 12 inches


def feet_to_inches():
    Feets = float(input("Enter the numbers of Feets to be converted.\n"))
    Inches = Feets * 12
    print("There are",Inches,"Inches in",Feets,"Feets")


def inches_to_feet():
    Inches = float(input("Enter the numbers of Inches to be converted.\n"))
    Feets = Inches / 12
    print("There are",Feets,"Feets in",Inches,"Inches")


print("Select the type of convertion.\n")
print("1 - Feets to Inches.")
print("2 - Inches to Feets.")
x=int(input(""))

if x == 1:
    feet_to_inches()

elif x == 2:
    inches_to_feet()

else:
    print("wrong selection")
