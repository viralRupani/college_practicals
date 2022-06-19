# Draw a smiling face emoji and rainbow using Turtle.

# Python program to draw smile
# face emoji using turtle
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()


def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()


# face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

# eyes
pen.goto(-40, 120)
eye('white', 15)
pen.goto(-37, 125)
eye('black', 5)
pen.goto(40, 120)
eye('white', 15)
pen.goto(40, 125)
eye('black', 5)

# mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()

screen.exitonclick()