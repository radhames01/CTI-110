# Program that sum all the numbers in a file
# 11 July 2017
# CTI-110 M6HW3 - Exception Handling
# Radhames Flete Perez



def main():
    Sum=0
    x=0
    div=0
    
    try:
        FileName = input("Enter the name of the file.")
        file = open(FileName, 'r')
        
        for line in file:

            try:
                
                num = int (line)
                Sum = Sum + num
                x = x +1
            except ValueError as ERR:
                print ("Non-numeric data in file", ERR)
        
    

        print("")
        print("The total Sum of all numbers is:",Sum,"\n")
        div = Sum / x
        print("The Average is:", div)

    except IOError as ERR:
        print(" Error trying to read the file.\n", ERR)
        print(" Check the name and extention.")        
    

    
main()
