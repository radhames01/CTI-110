# Program that ask for the price of the meal and \
# print the total with tips and taxes
# 11 June 2017
# CTI-110 M2HW2 - Tip Tax Total
# Radhames Flete Perez



# M = meal
# T = taxes
# TP = tips


M=int(input("Enter the value of the Meal: "))
TP=M*0.18
T=M*0.07

print("Total")
print("Meal: ",M)
print("Tips(18%):",TP)
print("Taxes(7%):",round(T,3))
Total=M+TP+T
print("The Total is: ",Total)
