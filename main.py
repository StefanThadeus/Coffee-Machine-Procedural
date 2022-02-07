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

# Constant variables
QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNY = 0.01

# Global variable money, indicating the total profit of the machine during operation
Profit = 0
# Global variable, indicating when the machine is turned on or off
isWorking = True


# TODO: 1. Print a report of all coffee machine resources
def print_machine_resources():
    """ Prints the current state of the resources and money in the machine """

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${Profit}")


# TODO: 2. Ask for user input for beverage
def get_input_beverage():
    """ Returns a string input containing information regarding the beverage choice """
    return input("What would you like? (espresso/latte/cappuccino): ")


# TODO: 3. Check if enough resources are available
def check_resources(beverage):
    """ Checks if there are sufficient resources to make the ordered drink, returns false and prints a message if not,
    or just returns true if there are enough necessary resources """

    for ingredient in MENU[beverage]["ingredients"]:
        if resources[ingredient] < MENU[beverage]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}!")
            return False

    return True


# TODO: 4. Process coins
def get_coins():
    """ Returns a float number of the total amount of money that user put into the machine """
    print("Please insert coins.")

    money_total = QUARTER * int(input("How many quarters?: "))
    money_total += DIME * int(input("How many dimes?: "))
    money_total += NICKLE * int(input("How many nickles?: "))
    money_total += PENNY * int(input("How many pennies?: "))

    return money_total


# TODO: 5. Check if transaction is successful
def check_transaction(inserted_money, beverage):
    """ Returns a float number of the difference between the inserted value of coins and item price. Result is
    positive or zero if user can afford the item, and negative if not enough money is inserted into the machine """
    return inserted_money - MENU[beverage]["cost"]


# TODO: 6. Perform order by updating the machine stats
def perform_order(beverage):
    """ Carries out the order by updating the status of the machine resources and money """
    # update machine resources
    global resources
    for resource in MENU[beverage]["ingredients"]:
        resources[resource] -= MENU[beverage]["ingredients"][resource]

    # update profit
    global Profit
    Profit += MENU[beverage]["cost"]


while isWorking:
    beverageResponse = get_input_beverage()
    beverageResponse = beverageResponse.lower()

    if beverageResponse == "off":
        isWorking = False

    elif beverageResponse == "report":
        print_machine_resources()

    elif beverageResponse not in MENU:
        print("Item not available in the menu.")

    else:
        hasResources = check_resources(beverageResponse)

        if hasResources:
            insertedCoins = get_coins()

            moneyChange = check_transaction(insertedCoins, beverageResponse)

            if moneyChange < 0:
                print("Sorry, that's not enough money. Money refunded.")

            else:
                if moneyChange > 0:
                    print(f"Here is ${round(moneyChange,2)} in change.")

                perform_order(beverageResponse)

                print(f"Here is your {beverageResponse} ☕. Enjoy!")
