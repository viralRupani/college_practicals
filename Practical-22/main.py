# Draw color-filled shapes (square, rectangle, and circle) using Turtle.
import turtle
from turtle import Screen

def square():
    turtle.setpos(-300, 0)
    turtle.pendown()
    for _ in range(0, 4):
        turtle.forward(100)
        turtle.left(90)
    turtle.penup()


def rectangle():
    turtle.setpos(-100, 0)
    turtle.pendown()
    for _ in [200, 100, 200, 100]:
        turtle.forward(_)
        turtle.left(90)
    turtle.penup()


def circle():
    turtle.setpos(200, 0)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()

screen = Screen()
screen.title('Turtle')
turtle = turtle.Turtle()
turtle.penup()

turtle.fillcolor('#00FF00')
turtle.begin_fill()
square()
rectangle()
circle()
turtle.end_fill()

screen.exitonclick()
