import turtle

board = turtle.Screen()
boardTitle = turtle.title("Two Circle")
boardBgColor = turtle.bgcolor("gray")
turtle.speed(0)

turtle1 = turtle.Turtle()
circleColors = ["red", "orange", "yellow", "green"]

for i in range(10):
    turtle1.color(circleColors[i % 4])
    turtle1.circle(10 * i)
    turtle1.circle(-10 * i)
    turtle1.left(i)


turtle.mainloop()


