import turtle

board = turtle.Screen()
boardTitle = turtle.title("Square")
boardBgColor = turtle.bgcolor("red")


turtle1 = turtle.Turtle()
turtle1.pencolor("white")
turtle1.pensize(10)


for i in range(4):
    turtle1.right(90)
    turtle1.forward(100)

turtle.done()