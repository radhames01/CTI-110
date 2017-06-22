# Program that draw a SnowFlake
# 22 June 2017
# CTI-110 M4LAB - SnowFlake
# Radhames FLete Perez


import turtle
turtle.speed(0)

x=0
for i in range (8):
    
    for i in range (8):
   
        for i in range (8):
            turtle.penup()
            turtle.forward(5)
           
            turtle.left(120)
            turtle.pendown()
            turtle.penup()
            turtle.forward(5)
            turtle.left(120)
            turtle.pendown()
            turtle.forward(5)
            turtle.left(120)
            turtle.right(45)
            turtle.penup()
            turtle.forward(5)
            turtle.pendown()

        turtle.penup()
        turtle.left(45)
        turtle.forward(25)
        turtle.pendown()

    turtle.penup()
    turtle.left(45)
    turtle.forward(150)
    turtle.pendown()
    x=x+1
    if x == 1:
        turtle.pencolor("red")
        turtle.pensize(5)
    elif x == 2:
        turtle.pencolor("green")
        turtle.pensize(1)
    elif x == 3:
        turtle.pencolor("blue")
        turtle.pensize(5)
    elif x == 4:
        turtle.pencolor("black")
        turtle.pensize(1)
    elif x == 5:
          turtle.pencolor("red")
          turtle.pensize(5)
    elif x == 6:
        turtle.pencolor("green")
        turtle.pensize(1)
    elif x == 7:
        turtle.pencolor("blue")
        turtle.pensize(5)
    elif x == 8:
        turtle.pencolor("black")
     


turtle.exitonclick()
