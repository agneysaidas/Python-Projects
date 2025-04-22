# Coffee Machine Program

# Menu of available drinks with ingredients and cost
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

# Available ingredients in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Track profit earned
profit = 0

# Check if the machine has enough resources to make the drink
def check_resource(flavour):
    for item in MENU[flavour]["ingredients"]:
        if MENU[flavour]["ingredients"][item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Ask the user to insert coins and calculate total value
def money():
    total = 0
    print("Please insert coins.")
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Check if transaction is successful and update profit
def is_transaction_successful(user_input, cost):
    global profit
    if user_input >= cost:
        change = round(user_input - cost, 2)
        print(f"Here is ${change} in change.")
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Deduct the used ingredients and serve the coffee
def make_coffee(flavour, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {flavour} ☕️. Enjoy!")

# Main loop to run the coffee machine
machine_on = True

while machine_on:
    flavour = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if flavour == "off":
        machine_on = False
    elif flavour == "report":
        for item, amount in resources.items():
            print(f"{item.capitalize()}: {amount}ml" if item != "coffee" else f"{item.capitalize()}: {amount}g")
        print(f"Money: ${profit}")
    elif flavour in MENU:
        if check_resource(flavour):
            payment = money()
            if is_transaction_successful(payment, MENU[flavour]["cost"]):
                make_coffee(flavour, MENU[flavour]["ingredients"])
    else:
        print("Invalid input. Please choose a valid option.")
