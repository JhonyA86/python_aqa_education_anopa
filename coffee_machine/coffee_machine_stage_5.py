# Stage 5 - adding "remaining" and "exit" actions, back to main menu and ingredients check
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


def coffee_preparing_text():
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


def state():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")


def buy():
    global water, milk, beans, disposable_cups, money
    while True:
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back: ")
        if choice == "1":
            if water >= water_for_one_cup_espresso and beans >= beans_for_one_cup_espresso:
                print("I have enough resources!")
                coffee_preparing_text()
                water -= water_for_one_cup_espresso
                beans -= beans_for_one_cup_espresso
                disposable_cups -= 1
                money += price_for_one_cup_espresso
            elif water < water_for_one_cup_espresso:
                print("Sorry, not enough water!")
                break
            elif beans < beans_for_one_cup_espresso:
                print("Sorry, not enough beans!")
                break
            elif disposable_cups == 0:
                print("Sorry, not enough disposable cups!")
                break
        elif choice == "2":
            if water >= water_for_one_cup_latte and milk >= milk_for_one_cup_latte and beans >= beans_for_one_cup_latte:
                print("I have enough resources!")
                coffee_preparing_text()
                water -= water_for_one_cup_latte
                milk -= milk_for_one_cup_latte
                beans -= beans_for_one_cup_latte
                disposable_cups -= 1
                money += price_for_one_cup_latte
            elif water < water_for_one_cup_latte:
                print("Sorry, not enough water!")
                break
            elif milk < milk_for_one_cup_latte:
                print("Sorry, not enough milk!")
                break
            elif beans < beans_for_one_cup_latte:
                print("Sorry, not enough beans!")
                break
            elif disposable_cups == 0:
                print("Sorry, not enough disposable cups!")
                break
        elif choice == "3":
            if water >= water_for_one_cup_cappuccino and milk >= milk_for_one_cup_cappuccino \
                    and beans >= beans_for_one_cup_cappuccino:
                print("I have enough resources!")
                coffee_preparing_text()
                water -= water_for_one_cup_cappuccino
                milk -= milk_for_one_cup_cappuccino
                beans -= beans_for_one_cup_cappuccino
                disposable_cups -= 1
                money += price_for_one_cup_cappuccino
            elif water < water_for_one_cup_cappuccino:
                print("Sorry, not enough water!")
                break
            elif milk < milk_for_one_cup_cappuccino:
                print("Sorry, not enough milk!")
                break
            elif beans < beans_for_one_cup_cappuccino:
                print("Sorry, not enough beans!")
                break
            elif disposable_cups == 0:
                print("Sorry, not enough disposable cups!")
                break
        elif choice == "back":
            print("Back to the main menu")
            return
        else:
            print("Incorrect input, please, try again")


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


while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        state()
    elif action == "exit":
        exit()
    else:
        print("Incorrect input, please, try again")
