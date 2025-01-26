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
    "Money": 0,
}


def availiblity(coffee):
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return False
    if coffee != "espresso":
        if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            return False
    if resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough Coffee")
        return False
    return True


def process_coins(coffee):
    print(f"The {coffee} costs {MENU[coffee]["cost"]}")
    coins = int(input("Enter no of dollars: "))
    if coins < MENU[coffee]["cost"]:
        coins += int(input("Enter no of quarters: ")) * 0.25
    if coins < MENU[coffee]["cost"]:
        coins += int(input("Enter no of dimes: ")) * 0.10
    if coins < MENU[coffee]["cost"]:
        coins += int(input("Enter no of nickles: ")) * 0.05
    if coins < MENU[coffee]["cost"]:
        coins += int(input("Enter no of pennies: ")) * 0.01
    if coins < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif coins >= MENU[coffee]["cost"]:
        if coins > MENU[coffee]["cost"]:
            print(f"Here is the change ${coins - MENU[coffee]["cost"]}")
        return True


def dispense_coffee(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    if coffee != "espresso":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    print("Coffee dispensed")


dispense = True
while dispense:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == 'off':
        dispense = False
    elif coffee_type == 'report':
        print('Available resources: ')
        for ing in resources:
            print(ing + " : " + str(resources[ing]))
    elif coffee_type in MENU:
        if availiblity(coffee_type):
            if process_coins(coffee_type):
                resources["Money"] += MENU[coffee_type]["cost"]
                dispense_coffee(coffee_type)
    else:
        print("wrong input")
