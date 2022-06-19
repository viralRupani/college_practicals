# Draw square, rectangle, and circle using Turtle.
import turtle


def square():
    turtle.setpos(-300, 0)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.penup()


def rectangle():
    turtle.setpos(-100, 0)
    turtle.pendown()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.penup()


def circle():
    turtle.setpos(200, 0)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()


turtle = turtle.Turtle()
turtle.penup()
square()
rectangle()
circle()
