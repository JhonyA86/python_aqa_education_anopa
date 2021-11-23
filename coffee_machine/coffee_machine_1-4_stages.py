# Stage 1 - messages that correspond to the stages of  coffee preparation
messages = """
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
"""
print(messages)

# Stage 2 - count the amount of ingredients

water_for_one_cup = 200
milk_for_one_cup = 50
beans_for_one_cup = 15


def count_ingredients():
    cups = int(input("Write how many cups of coffee you will need:"))
    water_needed = cups * water_for_one_cup
    milk_needed = cups * milk_for_one_cup
    beans_needed = cups * beans_for_one_cup
    print(f"For {cups} cups of coffee you will need:")
    print(f"{water_needed} ml of water")
    print(f"{milk_needed} ml of milk")
    print(f"{beans_needed} g of coffee beans")


count_ingredients()

# Stage 3 - check the amount of ingredients in the coffee machine and available number of cups


def cups_available():
    water_has = int(input("Write how many ml of water the coffee machine has:"))
    milk_has = int(input("Write how many ml of milk the coffee machine has:"))
    beans_has = int(input("Write how many grams of coffee beans the coffee machine has:"))
    cups = int(input("Write how many cups of coffee you will need:"))
    possible_cups = \
        min((water_has // water_for_one_cup), (milk_has // milk_for_one_cup), (beans_has // beans_for_one_cup))
    max_cups = max((water_has // water_for_one_cup), (milk_has // milk_for_one_cup), (beans_has // beans_for_one_cup))
    n = possible_cups - cups
    if cups > water_has // water_for_one_cup or cups > milk_has // milk_for_one_cup \
            or cups > beans_has // beans_for_one_cup:
        print(f"No, I can make only {possible_cups} cups of coffee")
    elif cups == possible_cups:
        print("Yes, I can make that amount of coffee")
    elif cups < max_cups:
        print(f"Yes, I can make that amount of coffee (and even {n} more than that)")


cups_available()

# Stage 4 - main coffee machine flow. Buy, fill, take and state functions.

# machine has
water = 400
milk = 540
beans = 120
disposable_cups = 9
money = 550

# espresso
water_for_one_cup_espresso = 250
beans_for_one_cup_espresso = 16
price_for_one_cup_espresso = 4

# latte
water_for_one_cup_latte = 350
milk_for_one_cup_latte = 75
beans_for_one_cup_latte = 20
price_for_one_cup_latte = 7

# cappuccino
water_for_one_cup_cappuccino = 200
milk_for_one_cup_cappuccino = 100
beans_for_one_cup_cappuccino = 12
price_for_one_cup_cappuccino = 6


def state():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")


def buy():
    global water, milk, beans, disposable_cups, money
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if choice == "1":
        water -= water_for_one_cup_espresso
        beans -= beans_for_one_cup_espresso
        disposable_cups -= 1
        money += price_for_one_cup_espresso
    elif choice == "2":
        water -= water_for_one_cup_latte
        milk -= milk_for_one_cup_latte
        beans -= beans_for_one_cup_latte
        disposable_cups -= 1
        money += price_for_one_cup_latte
    elif choice == "3":
        water -= water_for_one_cup_cappuccino
        milk -= milk_for_one_cup_cappuccino
        beans -= beans_for_one_cup_cappuccino
        disposable_cups -= 1
        money += price_for_one_cup_cappuccino


def fill():
    global water, milk, beans, disposable_cups, money
    water_to_fill = int(input("Write how many ml of water do you want to add: "))
    milk_to_fill = int(input("Write how many ml of milk do you want to add: "))
    beans_to_fill = int(input("Write how many grams of coffee beans do you want to add: "))
    disposable_cups_to_fill = int(input("Write how many disposable cups of coffee do you want to add: "))

    water += water_to_fill
    milk += milk_to_fill
    beans += beans_to_fill
    disposable_cups += disposable_cups_to_fill


def take():
    global water, milk, beans, disposable_cups, money
    print(f"I gave you  {money} грн")
    money = 0


state()
action = input("Write action (buy, fill, take): ")
if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take()
state()
