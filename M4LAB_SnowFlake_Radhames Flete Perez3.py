# Program that draw a SnowFlake #3
# 22 June 2017
# CTI-110 M4LAB - SnowFlake
# Radhames FLete Perez


import turtle

turtle.shape("turtle")

turtle.speed(0)
turtle.penup()
turtle.forward(90)
turtle.left(45)
turtle.pendown()
turtle.pencolor("blue")
turtle.pensize(7)

def snowflake():
    x=0
    
    for i in range (3): 
        for i in range(3): 
            turtle.forward(300)
            turtle.backward(300)
            turtle.right(45)
    
            
        turtle.left(90)
        turtle.backward(30)
        turtle.left(45)
       
        x=x+1
        if x == 1:
            turtle.pencolor("red")
            
        elif x == 2:
            turtle.pencolor("green")
        elif x == 3:
            turtle.pencolor("blue")

        
    turtle.right(90)
    turtle.forward(90)


    # colors
    
           
for i in range (8):
    snowflake()
    turtle.left(45)

turtle.right(45)
turtle.pencolor("green")
turtle.backward(90)
turtle.color("white")
turtle.left(90)






turtle.exitonclick()
