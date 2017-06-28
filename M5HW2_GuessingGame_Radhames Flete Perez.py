# Program that Guess a number and ask to match it
# 28 Jun 2017
# CTI-110 M5HW2 - Random Number Guessing Game
# Radhames Flete Perez



from random import randint

def low():
    print("Too low, try again.")
    
def high():
    print("Too high,try again.")

def game():
    Selection=0
    Rnum = randint(1,100)
    x=0
    print ("Guess the number.")
    while Selection != Rnum:
        
        Selection = int(input(""))

        if Selection < Rnum :
            low()
            
        if Selection > Rnum :
            high()
            
        if Selection == Rnum:
            print("Congratulations!!, the correct numbers is:",Rnum,"\n")
            
        x=x+1
    if x>1:
        print("You tried",x,"times.\n")
    else:
        print("You tried",x,"time.\n")



                  
def main():
    
    game()
    print("Play again? Y/N ")
    Ans = input("")
    if Ans =='y' or Ans =='Y':
        main()
    else:
        print("Good Bye")
        input()
        
main()
