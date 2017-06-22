# Program that draw triangles and square
# 22 June 2017
# CTI-110 M4LAB - Turtle Graphics
# Radhames FLete Perez



import turtle

z=0
a=0
x=int(input("how many Triangles?"))
y=int(input("how many Square?"))

turtle.shape("turtle")

turtle.pencolor("green")
turtle.penup()
turtle.backward(300)
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.pendown()

while z < x:
    turtle.pendown()
    turtle.color("blue")
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)

    turtle.penup()
    turtle.left(30)   
    turtle.forward(90)
    turtle.left(90)
    

   
    z=z+1


while a < y:

    turtle.pendown()
    turtle.pencolor("black")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)


    turtle.penup()
    turtle.backward(110)
    turtle.right(90)
    a=a+1

turtle.right(90) 
turtle.forward(40)
turtle.left(90)

turtle.pendown()

turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.left(90)
turtle.forward(35)
turtle.right(180)
turtle.forward(35)
turtle.right(125)
turtle.forward(40)
turtle.right(55)
turtle.forward(15)
turtle.left (90)
turtle.penup()

turtle.penup()
turtle.forward(20)
turtle.pendown()

turtle.left(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(35)
turtle.right(180)
turtle.forward(35)
turtle.left(90)
turtle.forward(35)
turtle.left(90)
turtle.forward(35)

turtle.penup()
turtle.forward(20)
turtle.right(90)
turtle.forward(35)
turtle.pendown()

turtle.right(180)
turtle.forward(70)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.color("white")


turtle.exitonclick()
