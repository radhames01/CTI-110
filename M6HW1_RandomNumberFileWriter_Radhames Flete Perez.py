# Program that ask how many number will be generate and save in a file
# 29 June 2017
# CTI-110 M6HW1 - Random Number File Writer
# Radhames Flete Perez


import random


def main():

    Fhold=int(input("How many random numers will the file hold?\n"))
    print("")
    file=open('one.txt','w')

    for i in range (Fhold):
        num=random.randint(1,501)
        print(num)
        y=str(num)

        r = file.write(y+"\n")   
    
    file.close()


main()
input()
