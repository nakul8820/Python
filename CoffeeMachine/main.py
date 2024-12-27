MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


rem_coffee = resources["coffee"]
rem_water = resources["water"]
rem_milk = resources["milk"]
profit = 0

def serve():
    global MENU
    global profit
    while True:
        print("☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
        drink = input("What would you like? (espresso/latte/cappuccino):")
        if drink == "off":
            print("Coffee Machine Turned Off")
            exit()
        if drink == "report":
            print(f"Water : {rem_water}ml \n Milk:{rem_milk}\n Coffee : {rem_coffee}\n Money:{profit}")

        if check_resource(drink):
            print("INSERT COINS")
            quarter = int(input("QUARTERS: "))
            dimes = int(input("DIMES: "))
            nickels = int(input("NICKELS: "))
            pennies = int(input("PENNIES: "))
            paid_amount = (quarter * 0.25 + dimes * 0.10 +  nickels * 0.05 + pennies * 0.01 )
            if paid_amount == MENU[drink]["cost"] or paid_amount > MENU[drink]["cost"]:
                change = round(paid_amount - MENU[drink]["cost"],2)
                deduct_resource(drink)
                print(f"Here is ${change} dollars in change ")
                profit = round(profit + (paid_amount - change),2)
                print(f"{drink} will be Dispensed. Thank U for Shopping. Enjoy Your {drink}")
                print("☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
            else:
                print("Sorry that's not enough money. Money refunded.")
                exit()




def check_resource(drink):
    global resources,MENU,rem_water,rem_milk,rem_coffee,profit

    if drink == "espresso":
        if rem_coffee < MENU["espresso"]["ingredients"]["coffee"] or rem_water <MENU["espresso"]["ingredients"]["milk"]:
            print("SORRY. There Is Not Enough resource")
            exit()
        return True

    if drink == "latte":
        if rem_coffee < MENU["latte"]["ingredients"]["coffee"] or rem_water <MENU["latte"]["ingredients"]["milk"] or rem_milk  <MENU["latte"]["ingredients"]["milk"]:
            print("SORRY. There Is Not Enough resource")
            exit()
        return  True

    if drink == "cappuccino":
        if rem_coffee < MENU["cappuccino"]["ingredients"]["coffee"] or rem_water <MENU["cappuccino"]["ingredients"]["milk"] or rem_milk  <MENU["cappuccino"]["ingredients"]["milk"]:
            print("SORRY. There Is Not Enough resource")
            exit()
        return True

def deduct_resource(drink):
    global rem_water,rem_milk,rem_coffee
    if drink == "espresso":
        rem_water = rem_water - MENU["espresso"]["ingredients"]["milk"]
        rem_coffee = rem_coffee - MENU["espresso"]["ingredients"]["coffee"]
    if drink == "latte":
        rem_water = rem_water - MENU["latte"]["ingredients"]["water"]
        rem_milk = rem_milk - MENU["latte"]["ingredients"]["milk"]
        rem_coffee = rem_coffee - MENU["latte"]["ingredients"]["coffee"]
    if drink == "cappuccino":
        rem_water = rem_water - MENU["cappuccino"]["ingredients"]["water"]
        rem_milk = rem_milk - MENU["cappuccino"]["ingredients"]["milk"]
        rem_coffee = rem_coffee - MENU["cappuccino"]["ingredients"]["coffee"]


serve()



