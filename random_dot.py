import turtle
import random

board = turtle.Screen()
board.title("Turtle Yönlendirme")
board.bgcolor("white")
t = turtle.Turtle()

dot_colors = ["red", "orange", "yellow", "green","blue","pink"]


t.up()

for i in range(30):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    coor = (x,y)
    t.color(dot_colors[i%6])
    t.goto(coor)
    t.dot(25)

t.down()



board.mainloop()