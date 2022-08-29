machine_resources = {
    "Water": 5000,
    "Coffee": 600,
    "Milk": 2000,
    "Money": 0
}


drink_choices = [
    {
        "Name": "Espresso",
        "Water": 50,
        "Coffee": 18,
        "Milk": 0,
        "Price": 1.50
    },
    {
        "Name": "Latte",
        "Water": 200,
        "Coffee": 24,
        "Milk": 150,
        "Price": 2.50
    },
    {
        "Name": "Cappuccino",
        "Water": 250,
        "Coffee": 24,
        "Milk": 100,
        "Price": 3.00
    },
]


def menu():
    """ Display menu"""
    print("Welcome to coffee machine. What would you like?")
    i = 0
    for item in drink_choices:
        i += 1
        print(str(i) + ": " + item["Name"] + " $" + str(item["Price"]))
    user_input = input("Your choice is: ")
    return user_input


def deal_user_input(value):
    """ Check user input """
    try:
        option = int(value)
        if 0 <= option <= 3 or option == 999 or option == 777:
            return True
        else:
            print("Sorry, I only know how to make above drinks. Please try again")
            return False
    except ValueError:
        print("Sorry, I only know how to make above drinks. Please try again")
        return False


def is_resources_sufficient(chosen_drink):
    """ Check ingredients """
    if machine_resources["Water"] < chosen_drink["Water"]:
        print("Sorry there is not enough water")
        return False
    elif machine_resources["Coffee"] < chosen_drink["Coffee"]:
        print("Sorry there is not enough coffee")
        return False
    elif machine_resources["Milk"] < chosen_drink["Milk"]:
        print("Sorry there is not enough milk")
        return False
    else:
        return True


def make_drink(chosen_drink):
    """ reduce the amount of each ingredient"""
    machine_resources["Water"] -= chosen_drink["Water"]
    machine_resources["Coffee"] -= chosen_drink["Coffee"]
    machine_resources["Milk"] -= chosen_drink["Milk"]


def coins_operator():
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
    except ValueError:
        print("Sorry, only accept numbers. Money refunded.")
        return -1
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def report():
    print(f"Water: {machine_resources['Water']}ml")
    print(f"Coffee: {machine_resources['Coffee']}g")
    print(f"Milk: {machine_resources['Milk']}ml")
    print(f"Money: ${machine_resources['Money']}")


def refill_machine():
    print("Refill all ingredients.")
    machine_resources["Water"] = 5000
    machine_resources["Coffee"] = 600
    machine_resources["Milk"] = 2000
    print(f"Water: {machine_resources['Water']}ml")
    print(f"Coffee: {machine_resources['Coffee']}g")
    print(f"Milk: {machine_resources['Milk']}ml")


def withdraw_money():
    print("Withdraw money.")
    income = machine_resources["Money"]
    print(f"The total income is {income}")
    machine_resources["Money"] = 0


is_on = True

while is_on:
    user_input = menu()
    is_valid_option = deal_user_input(user_input)
    if is_valid_option:
        input_number = int(user_input)
        if input_number == 0:
            print("\nHere is the report:")
            report()
        elif input_number == 999:
            refill_machine()
        elif input_number == 777:
            withdraw_money()
        else:
            chosen_drink = drink_choices[input_number - 1]
            if is_resources_sufficient(chosen_drink):
                make_drink(chosen_drink)
                payment = coins_operator()
                if payment != -1:
                    change = round(payment - chosen_drink["Price"], 2)
                    if change >= 0:
                        machine_resources["Money"] += chosen_drink["Price"]
                        print(f"Here is ${change} in change.")
                        drink_item = chosen_drink["Name"]
                        print(f"Here is your {drink_item}. Enjoy!")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
    print()

