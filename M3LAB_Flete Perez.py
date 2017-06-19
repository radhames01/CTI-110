# Program that print your grade based on the Score
# 14 June 2017
# CTI-110 M3LAB - Debugging
# Radhames Flete Perez


def ScoreCal():
    
    Score = int(input("Enter the Student Score."))

    if Score > 100 or Score < 0:
        print("Wrong Score")
    elif Score >= 90 and Score <=100:
        print("Your grade is A.")
    elif Score >= 80 and Score <=89:
        print("Your Grade is B.")
    elif Score >= 70 and Score <=79:
        print("Your Grade is C.")
    elif Score >=60 and Score <=69:
        print("Your Grade is D.")
    else:
        print("Your Grade is D.")


print(" Options : ")
print(" 1 - Grade Calculator\n","2 - Nothing")
Option = int(input(" \n"))

if Option == 1:
    ScoreCal()
else:
    print("Not Available.")
