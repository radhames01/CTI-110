# Program that read, print and sum the numbers in a file
# 29 June 2017
# CTI-110 M6HW2 - Random Number File Reader
# Radhames Flete Perez


def main():

    file = open('one.txt')
    Sum=0
    Tnum=0
    x=0
    for line in file:
    
        num=int(line)
        Sum= Sum + num
        Tnum = Tnum + 1
        x=x+1
        print(x,"-",num)

    print("")
    print("The Total Sum of all numbers is:",Sum,"\n")
    print("There are",Tnum,"random numbers in the file")


main()

input()


