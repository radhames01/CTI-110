# Program that caculate the penies per day and print the total aunount in dollars
# 19 June 2017
# CTI-110 M4HW2 - Pennies for Pay 
# Radhames Flete Perez



penies=1
x=0
Dollars=0
Dollarspdays = 0

Days=int(input("Enter the number of worked days>"))

while x < Days:
    Dollarspdays = penies / 100
    Dollars = Dollars + penies
    x=x+1
    penies*=2
    print(Dollarspdays,"$ were earned during day number",x)

print("")
print("the total earned during",x,"days are: $",Dollars/100)


