import turtle

board = turtle.Screen()
boardTitle = turtle.title("Star")
boardBgColor = turtle.bgcolor("red")

turtle1 = turtle.Turtle()
turtle1.pencolor("white")
turtle1.pensize(5)

for i in range(5):
    turtle1.left(144)
    turtle1.forward(100)


turtle.done()