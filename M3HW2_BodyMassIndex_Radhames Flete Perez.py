# Program that calculate the boddy fat or BMI
# 15 June 2017
# CTI-110 M3HW2 - Body Mass Index
# Radhames Flete Perez



# BMI = weight * 703 / height^2

print("Hello")

weight = float(input("Please enter your weight in pounds."))

height = float(input("Please enter your height in inches."))

pounds = weight * 703
inches = height * height

BMI = pounds / inches
BMI = BMI /100

print("Your BMI is",format(BMI,".2f"),"%")



if BMI <18.5:
    print("The person is considerer to be underweight.")
elif BMI >=18.5 and BMI <=25.0:
    print ("The person is in optimal weight.")
else:
    print("The person is considerer to be overweight.")
