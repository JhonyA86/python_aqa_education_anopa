class CoffeeMachine:

    # espresso
    WATER_FOR_ESPRESSO = 250
    BEANS_FOR_ESPRESSO = 16
    PRICE_FOR_ESPRESSO = 4

    # latte
    WATER_FOR_LATTE = 350
    MILK_FOR_LATTE = 75
    BEANS_FOR_LATTE = 20
    PRICE_FOR_LATTE = 7

    # cappuccino
    WATER_FOR_CAPPUCCINO = 200
    MILK_FOR_CAPPUCCINO = 100
    BEANS_FOR_CAPPUCCINO = 12
    PRICE_FOR_CAPPUCCINO = 6

    def __init__(self, water, milk, beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable_cups = disposable_cups
        self.money = money

    @staticmethod
    def coffee_preparing_text():
        messages = """
        Starting to make a coffee
        Grinding coffee self.beans
        Boiling water
        Mixing boiled water with crushed coffee self.beans
        Pouring coffee into the cup
        Pouring some milk into the cup
        Coffee is ready!
        """
        print(messages)

    def state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self):
        while True:
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back: ")
            if choice == "1":
                if self.water >= CoffeeMachine.WATER_FOR_ESPRESSO and self.beans >= CoffeeMachine.BEANS_FOR_ESPRESSO:
                    print("I have enough resources!")
                    CoffeeMachine.coffee_preparing_text()
                    self.water -= CoffeeMachine.WATER_FOR_ESPRESSO
                    self.beans -= CoffeeMachine.BEANS_FOR_ESPRESSO
                    self.disposable_cups -= 1
                    self.money += CoffeeMachine.PRICE_FOR_ESPRESSO
                elif self.water < CoffeeMachine.WATER_FOR_ESPRESSO:
                    print("Sorry, not enough water!")
                    break
                elif self.beans < CoffeeMachine.BEANS_FOR_ESPRESSO:
                    print("Sorry, not enough beans!")
                    break
                elif self.disposable_cups == 0:
                    print("Sorry, not enough disposable cups!")
                    break
            elif choice == "2":
                if self.water >= CoffeeMachine.WATER_FOR_LATTE \
                        and self.milk >= CoffeeMachine.MILK_FOR_LATTE and \
                        self.beans >= CoffeeMachine.BEANS_FOR_LATTE:
                    print("I have enough resources!")
                    CoffeeMachine.coffee_preparing_text()
                    self.water -= CoffeeMachine.WATER_FOR_LATTE
                    self.milk -= CoffeeMachine.MILK_FOR_LATTE
                    self.beans -= CoffeeMachine.BEANS_FOR_LATTE
                    self.disposable_cups -= 1
                    self.money += CoffeeMachine.PRICE_FOR_LATTE
                elif self.water < CoffeeMachine.WATER_FOR_LATTE:
                    print("Sorry, not enough water!")
                    break
                elif self.milk < CoffeeMachine.MILK_FOR_LATTE:
                    print("Sorry, not enough milk!")
                    break
                elif self.beans < CoffeeMachine.BEANS_FOR_LATTE:
                    print("Sorry, not enough beans!")
                    break
                elif self.disposable_cups == 0:
                    print("Sorry, not enough disposable cups!")
                    break
            elif choice == "3":
                if self.water >= CoffeeMachine.WATER_FOR_CAPPUCCINO \
                        and self.milk >= CoffeeMachine.MILK_FOR_CAPPUCCINO \
                        and self.beans >= CoffeeMachine.BEANS_FOR_CAPPUCCINO:
                    print("I have enough resources!")
                    CoffeeMachine.coffee_preparing_text()
                    self.water -= CoffeeMachine.WATER_FOR_CAPPUCCINO
                    self.milk -= CoffeeMachine.MILK_FOR_CAPPUCCINO
                    self.beans -= CoffeeMachine.BEANS_FOR_CAPPUCCINO
                    self.disposable_cups -= 1
                    self.money += CoffeeMachine.PRICE_FOR_CAPPUCCINO
                elif self.water < CoffeeMachine.WATER_FOR_CAPPUCCINO:
                    print("Sorry, not enough water!")
                    break
                elif self.milk < CoffeeMachine.MILK_FOR_CAPPUCCINO:
                    print("Sorry, not enough milk!")
                    break
                elif self.beans < CoffeeMachine.BEANS_FOR_CAPPUCCINO:
                    print("Sorry, not enough beans!")
                    break
                elif self.disposable_cups == 0:
                    print("Sorry, not enough disposable cups!")
                    break
            elif choice == "back":
                print("Back to the main menu")
                return
            else:
                print("Incorrect input, please, try again")

    def fill(self):
        water_to_fill = int(input("Write how many ml of water do you want to add: "))
        milk_to_fill = int(input("Write how many ml of milk do you want to add: "))
        beans_to_fill = int(input("Write how many grams of coffee beans do you want to add: "))
        disposable_cups_to_fill = int(input("Write how many disposable cups of coffee do you want to add: "))

        self.water += water_to_fill
        self.milk += milk_to_fill
        self.beans += beans_to_fill
        self.disposable_cups += disposable_cups_to_fill

    def take(self):
        print(f"I gave you  {self.money} грн")
        self.money = 0

    def action(self, user_input):
        if user_input == "buy":
            return self.buy()
        elif user_input == "fill":
            return self.fill()
        elif user_input == "take":
            return self.take()
        elif user_input == "remaining":
            return self.state()
        elif user_input == "exit":
            exit()
        else:
            print("Incorrect input, please, try again")


response = "Write action (buy, fill, take, remaining, exit): "
cm = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    inp = input(response)
    cm.action(inp)
