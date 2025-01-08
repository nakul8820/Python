import random
import turtle
from turtle import Turtle, Screen
turtle_the_painter =Turtle()
turtle_the_painter.shape("arrow")

#turtle_the_painter.pensize(15)
#turtle_the_painter.speed("fastest")
#turtle_the_painter.shapesize(1.2,1.2,1.2)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#directions = [0,90,180,270]
#turtle.colormode(255)

'''for _ in range(15):
    turtle_the_painter.forward(5)
    turtle_the_painter.penup()
    turtle_the_painter.forward(5)
    turtle_the_painter.pendown()




for _ i
def triangle():
    change_color()
    for _ in range(3):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(120)

def square():
    change_color()
    for _ in range(4):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(90)

def pentagon():
    change_color()
    for _ in range(5):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(72)

def hexagon():
    change_color()
    for _ in range(6):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(60)

def heptagon():
    change_color()
    for _ in range(7):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(51.43)

def octagon():
    change_color()
    for _ in range(8):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(45)

def nonagon():
    change_color()
    for _ in range(9):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(40)

def decagon():
    change_color()
    for _ in range(10):
        turtle_the_painter.forward(100)
        turtle_the_painter.right(36)


change_color()
triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()


def random_walk():
    while True:
        change_color()
        direction = randint(1,4)
        '1 for straight 2 for right 3 for backward 4 for left'
        if direction == 1:
            turtle_the_painter.forward(30)
        elif direction == 2:
            turtle_the_painter.right(90)
            turtle_the_painter.forward(30)
        elif direction == 3:
            turtle_the_painter.right(180)
            turtle_the_painter.forward(30)
        elif direction == 4:
            turtle_the_painter.left(90)
            turtle_the_painter.forward(30)


for _ in range(200):
    turtle_the_painter.pencolor(random.choice(colours))
    turtle_the_painter.forward(30)
    turtle_the_painter.setheading(random.choice(directions))
'''

def change_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def spirograph(size_of_gap):
    turtle_the_painter.speed("fastest")
    for _ in range(int(360/5)):
        turtle_the_painter.color(random.choice(colours))
        turtle_the_painter.circle(100)
        turtle_the_painter.setheading( turtle_the_painter.heading() + size_of_gap)


spirograph(5)
screen = Screen()
screen.exitonclick()

