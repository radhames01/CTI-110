# Program that classified according to the age
# 14 June 2017
# CTI-110 M3HW1 - Age Classifier
# Radhames Flete Perez




def Oneorless():
    Age = int(input("Enter the numbers of weeks\n"))
    print("This is a baby and he/she is",Age,"weeks old.\n")

def Oneormore():
    Age = int(input("Enter your Age Please.\n"))
    if Age >=0 and Age <= 1:
        print("He / She is a Infant.")
    elif Age >1 and Age <13:
        print("He / She is a Child.")
    elif Age >= 13 and Age <20:
        print("He / She is a Teenager.")
    else:
        print("He / She is an Adult.")



print("Make a Selection\n","1 - 1 Year old or less\n","2 - 1 Year or older")
Option = int(input(" \n"))

if Option ==1:
    Oneorless()
elif Option ==2:
    Oneormore()
else:
    print("Invalid option.")
