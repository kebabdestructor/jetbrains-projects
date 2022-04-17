from traceback import print_tb

class CoffeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.stock = [self.water, self.milk, self.beans, self.cups, self.money]
        
    def get_stock(self):
        print(f"""The coffee machine has:
            {self.water} ml of water
            {self.milk} ml of milk
            {self.beans} g of coffee beans
            {self.cups} disposable cups
            {self.money} of money""")
    
    def write_action(self):
        print("Write action (buy, fill, take):")
        action = input()
        if action == 'fill':
            stock = fill_coffee(self.stock)
            self.water, self.milk, self.beans, self.cups, self.money = stock
        elif action == 'take':
            stock = take_money(self.stock)
            self.water, self.milk, self.beans, self.cups, self.money = stock
        elif action == 'buy':
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            coffee_type = int(input())
            stock = brew_coffee(coffee_type, self.stock)
            self.water, self.milk, self.beans, self.cups, self.money = stock

def brew_coffee(coffee_type, stock):
    water, milk, beans, cups, money = stock
    if coffee_type == 1:
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
    elif coffee_type == 2:
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
    elif coffee_type == 3:
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
    return [water, milk, beans, cups, money]

def fill_coffee(stock):
    water, milk, beans, cups, money = stock
    print("Write how many ml of water you want to add:")
    water += int(input())
    print("Write how many ml of milk you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    beans += int(input())
    print("Write how many disposable cups of coffee you want to add:")
    cups += int(input())
    return [water, milk, beans, cups, money]

def take_money(stock):
    water, milk, beans, cups, money = stock
    print(f"I gave you {money}")
    money = 0
    return [water, milk, beans, cups, money]

water = 400
milk = 540
beans = 120
cups = 9
money = 550

my_coffee = CoffeMachine(water, milk, beans, cups, money)
my_coffee.get_stock()
my_coffee.write_action()
my_coffee.get_stock()