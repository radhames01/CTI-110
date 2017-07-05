# Program that calculated the total of the numbers in a file.
# 05 July 2017
# CTI-110 M6LAB - Sum of Numbers
# Radhames Flete Perez



def main(): 
    z='numbers.txt'
    file = open(z,'r') 
    Sum=0 
    for line in file: 
      
        num=int(line) 
        Sum= Sum + num 
         
        

    print("") 
    print("The Total Sum of all numbers is:",Sum,"\n") 
    file.close()
  
 
main() 

 
input() 
