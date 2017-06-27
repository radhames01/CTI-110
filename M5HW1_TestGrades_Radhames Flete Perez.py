# Program that Calculate and print the Average and grade of five scores
# 27 June 2017
# CTI-110 M5HW1 - Test Average and Grade
# Radhames Flete Perez


def calc_average(a,b,c,d,e):

    Total=a+b+c+d+e
    TotalScore = Total / 5 
    return TotalScore

def determine_grade(A):
    Grade = A
    if Grade < 0 or Grade > 100:
        print("wrong test Score")
    elif Grade >= 90 and Grade <=100:
        print("The Grade is: A",)
    elif Grade >= 80 and Grade <90:
        print("The Grade is: B")
    elif Grade >= 70 and Grade <80:
        print("The Grade is: C")
    elif Grade >= 60 and Grade <70:
        print("The Grade is: D")
    elif Grade >= 0 and Grade <60:
        print("The Grade is: F")

def cls():
    print("\n"*30)

def main():
    
    test1=float(input("Enter the First Score.\n"))
    test2=float(input("Enter the Second Score.\n"))
    test3=float(input("Enter the Third Score.\n"))
    test4=float(input("Enter the Fourth Score.\n"))
    test5=float(input("Enter the Fifth Score.\n"))
    cls()

    x=1
    if x == 1 :        
        print("The First Score is:",test1)
        determine_grade(test1)
        x=x+1
        print("")
        
    if x == 2 :        
        print("The Second Score is:",test2)
        determine_grade(test2)
        x=x+1
        print("")
        
    if x == 3 :        
        print("The Second Third is:",test3)
        determine_grade(test3)
        x=x+1
        print("")
        
    if x == 4 :        
        print("The Second Fourth is:",test4)
        determine_grade(test4)
        x=x+1
        print("")
        
    if x == 5 :        
        print("The Second Fifth is:",test5)
        determine_grade(test5)
        x=x+1        
        print("")

    average = calc_average(test1,test2,test3,test4,test5)   
    print("The Average Grade for the five Score is:",average)
    determine_grade(average)
        
main()


input("Press any Key to Exit")
