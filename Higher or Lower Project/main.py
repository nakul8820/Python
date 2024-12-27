import random

from game_data import data
from art import logo
from art import vs


choice1 = {}
choice2 = {}
score = 0
ans = ''

def start():
    global choice1
    global choice2

    num1 = random.randint(0, 49)
    choice1 = data[num1]

    num2 = random.randint(0, 49)
    if num2 == num1:
        num2 = random.randint(0, 49)
    choice2 = data[num2]
    print_detail(choice1,choice2)

def user_input():
    global ans
    ans = input("Who has more followers? Type 'A' or 'B': ")
    return ans

def print_detail(c1,c2):
    name_1 = c1["name"]
    desc_1 = c1["description"]
    country_1 = c1["country"]

    name_2 = c2["name"]
    desc_2 = c2["description"]
    country_2 = c2["country"]

    print(logo)
    print(f"Compare A: {name_1} , {desc_1} , {country_1}.")
    print(vs)
    print(f"Compare B: {name_2} , {desc_2} , {country_2}")

def new_round():
    global ans
    global choice2,choice1
    print_detail(choice1,choice2)
    ans = user_input()
    check_ans(ans)

def check_ans(a):
    global choice1, choice2
    if a == 'b':
        if choice2["follower_count"] > choice1["follower_count"]:
            global score
            score = score + 1
            print(f"You're right! Current score: {score}.")
            choice1 = choice2
            choice2 = data[random.randint(0, 49)]
            new_round()
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
    elif a == 'a':
        if choice2["follower_count"] < choice1["follower_count"]:
            score = score + 1
            print(f"You're right! Current score: {score}.")
            choice2 = data[random.randint(0,49)]
            new_round()
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")


start()
ans =user_input()
check_ans(ans)