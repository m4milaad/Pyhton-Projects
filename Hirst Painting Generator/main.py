from turtle import Turtle, Screen
import turtle
import random


def init_turtle():
    timmy.penup()
    turtle.colormode(255)
    timmy.shape("turtle")
    timmy.color("green")
    timmy.setheading(225)
    timmy.fd(50 * 5)
    timmy.setheading(0)


def draw_dot():
    timmy.pendown()
    timmy.dot(20, random.choice(colour_list))
    timmy.penup()


def change_line():
    timmy.back(50 * 10)
    timmy.left(90)
    timmy.fd(50)
    timmy.rt(90)


def draw_line():
    for i in range(10):
        draw_dot()
        timmy.fd(50)


colour_list = [(249, 248, 248), (238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17),
               (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39)]

timmy = Turtle()
init_turtle()
for i in range(10):
    draw_line()
    change_line()

scr = Screen()
scr.exitonclick()
