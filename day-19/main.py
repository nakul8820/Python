import random
from turtle import Turtle, Screen

screen = Screen()

"""

def mov_forward():
    turtle.forward(10)

def mov_backward():
    turtle.backward(10)

def counter_clockwise():
    turtle.left(5)

def clockwise():
    turtle.right(5)

def clear():
    turtle.home()
    turtle.penup()
    turtle.clear()
    turtle.pendown()

screen.listen()
screen.onkey(key="w", fun= mov_forward)
screen.onkey(key="s", fun= mov_backward)
screen.onkey(key="a", fun= counter_clockwise)
screen.onkey(key="d", fun= clockwise)
screen.onkey(key="c", fun= clear)

"""

# Turtle Race

screen.setup(500,400)
colors = ["red","orange","yellow","green","blue","purple"]
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color:")
is_race_on = False

racing_turtles = []
i = 0
for color in colors:
    T= Turtle(shape="turtle")
    T.color(color)
    racing_turtles.append(T)
    T.penup()
    T.goto(-230,i)
    i = i +30

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in racing_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won ! Winning Turtle is {winning_color}")
            else:
                print(f"You have lost! Winning Turtle is {winning_color} ")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()