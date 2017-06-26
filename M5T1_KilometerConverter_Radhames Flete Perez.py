# Program that conver kilometers to miles
# 26 Jun 2017
# CTI-110 M5T1_KilometerConverter 
# Radhames Flete Perez


def kilotomiles():
    Kilometers = float(input("Enter the number of Kilometers to be converted.\n"))

    Miles = Kilometers * 0.6214

    print("there are",Miles,"Miles in",Kilometers,"kilometers")

def milestokilo():
    Miles = float(input("Enter the number of Miles to be converted.\n"))
    Kilometers = Miles / 0.6214
    print("There are",Kilometers,"Kilometers in",Miles,"Miles")



print("Select the type of convertion.")
print("1 - Kilometers to Miles.")
print("2 - Miles to Kilometers.") 
x= int(input(""))

if x == 1:
    kilotomiles()
    
elif x == 2:
    milestokilo()
    
else:
   # x < 1 or x >2:
    print("wrong. Try again")
