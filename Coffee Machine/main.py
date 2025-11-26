MACHINE_ON = True
# Money_inserted = 0.0
# change = 0


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

resources["money"] = 0

def check_resources (m_resources, menu, drink):
    if drink == "espresso":
        if m_resources["water"] < menu["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        if m_resources["coffee"] < menu["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

    if drink == "latte":
        if m_resources["water"] < menu["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        if m_resources["coffee"] < menu["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        if m_resources["milk"] < menu["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True

    if drink == "cappuccino":
        if m_resources["water"] < menu["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        if m_resources["coffee"] < menu["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        if m_resources["milk"] < menu["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True

def calculate_coins(cquarters, cdimes, cnickles, cpennies):
    money = 0.25*cquarters + 0.1*cdimes + 0.05*cnickles + 0.01*cpennies
    return money

def check_money_is_enough (money, menu, select, resource, change):
    if money < menu[select]['cost']:
        print("Sorry, that's not enough money. Money refunded")
        return False

    elif money == menu[select]['cost']:
        change = money - menu[select]['cost']
        resource["money"] += menu[select]['cost']
        return change

    elif money > menu[select]['cost']:
        change = money - menu[select]['cost']
        resource["money"] += menu[select]['cost']
        return change

def calculate_resources (m_resources, menu, drink):
    if drink == "espresso":
        m_resources["water"] = m_resources["water"]-menu["espresso"]["ingredients"]["water"]
        m_resources["coffee"] = m_resources["coffee"]-menu["espresso"]["ingredients"]["coffee"]
    elif drink == "latte":
        m_resources["water"] = m_resources["water"] - menu["latte"]["ingredients"]["water"]
        m_resources["coffee"] = m_resources["coffee"] - menu["latte"]["ingredients"]["coffee"]
        m_resources["milk"] = m_resources["milk"] - menu["latte"]["ingredients"]["milk"]
    elif drink == "cappuccino":
        m_resources["water"] = m_resources["water"] - menu["cappuccino"]["ingredients"]["water"]
        m_resources["coffee"] = m_resources["coffee"] - menu["cappuccino"]["ingredients"]["coffee"]
        m_resources["milk"] = m_resources["milk"] - menu["cappuccino"]["ingredients"]["milk"]

while MACHINE_ON:

    Money_inserted = 0.0
    change = 0
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif selection == "off":
        MACHINE_ON = False
    elif selection == "espresso":

        if check_resources(resources, MENU, selection):
            print("Insert coins (quarters, dimes, nickles and pennies):")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            Money_inserted = float(calculate_coins(quarters, dimes, nickles, pennies))
            change = float(check_money_is_enough(Money_inserted, MENU, selection, resources, change))
            if change > 0:
                print(f"Here is {change} dollars in change.")
            calculate_resources(resources, MENU, selection)
            print(f"Here is your {selection}. Enjoy!")

    elif selection == "latte":
        if check_resources(resources, MENU, selection):
            print("Insert coins (quarters, dimes, nickles and pennies):")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            Money_inserted = float(calculate_coins(quarters, dimes, nickles, pennies))
            change = float(check_money_is_enough(Money_inserted, MENU, selection, resources, change))
            if change > 0:
                print(f"Here is {change} dollars in change.")
            calculate_resources(resources, MENU, selection)
            print(f"Here is your {selection}. Enjoy!")

    elif selection == "cappuccino":
        if check_resources(resources, MENU, selection):
            print("Insert coins (quarters, dimes, nickles and pennies):")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            Money_inserted = float(calculate_coins(quarters, dimes, nickles, pennies))
            change = float(check_money_is_enough(Money_inserted, MENU, selection, resources, change))
            if change > 0:
                print(f"Here is {change} dollars in change.")
            calculate_resources(resources, MENU, selection)
            print(f"Here is your {selection}. Enjoy!")

