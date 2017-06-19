# Program that add the number of bug collected during five days
# 15 June 2017
# CTI-110 M4T1 - Bug Collector
# Radhames Flete Perez



bug=0
collec=0
while bug < 5:
    if bug==0:
        print("Enter the number of Bugs collected on day one.")
    elif bug==1:
        print("Enter the number of Bugs collected on day two.")
    elif bug==2:
        print("Enter the number of Bugs collected on day three.")
    elif bug==3:
        print("Enter the number of Bugs collected on day fourth.")
    elif bug==4:
        print("Enter the number of Bugs collected on day five.")
        
    bug = bug + 1
    collection = int(input(" "))
    collec = collec + collection

print("The total of bug collected during the five days are:",collec,'.')
