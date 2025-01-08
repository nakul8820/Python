"""
import colorgram

colors = colorgram.extract('hirst.jpg',30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
"""
import random
import turtle
from turtle import Turtle, Screen,penup
turtle_the_painter =Turtle()
turtle_the_painter.shape("arrow")
turtle_the_painter.speed("fastest")
turtle_the_painter.penup()
turtle_the_painter.hideturtle()
turtle.colormode(255)

color_list = [(145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

turtle_the_painter.setheading(225)
turtle_the_painter.forward(300)
turtle_the_painter.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    turtle_the_painter.dot(20,random.choice(color_list))
    turtle_the_painter.forward(50)

    if dot_count %10 == 0:
        turtle_the_painter.setheading(90)
        turtle_the_painter.forward(50)
        turtle_the_painter.setheading(180)
        turtle_the_painter.forward(500)
        turtle_the_painter.setheading(0)

screen = Screen()
screen.exitonclick()