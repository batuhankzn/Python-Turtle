import turtle

board = turtle.Screen()
boardTitle = turtle.title("Polygon")
boardBgColor = turtle.bgcolor("red")

turtle1 = turtle.Turtle()
turtle1.pencolor("white")
turtle1.pensize(5)

num_side = 9
angle = 360 / num_side
side_lenght = 100

for i in range(num_side):
    turtle1.left(angle)
    turtle1.forward(side_lenght)




turtle.done()