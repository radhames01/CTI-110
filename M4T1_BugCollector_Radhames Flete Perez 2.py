# Program that add the number of bug collected during five days
# 15 June 2017
# CTI-110 M4T1 - Bug Collector
# Radhames Flete Perez


bug = 0
collec = 0
y=1
for x in range (1,6):
    print("Number of bug collected one day",y,"?")
    y=y+1
    bug=int(input(" "))
    collec = collec + bug

print("The total of bug collected during the five days are:",collec)
