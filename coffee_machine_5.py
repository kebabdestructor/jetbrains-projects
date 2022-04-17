initial_stock = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}

class CoffeMachine:

    def __init__(self, stock):
        self.stock = stock

    def get_stock(self):
        print("The coffee machine has:")
        print(f"{self.stock['water']} ml of water")
        print(f"{self.stock['milk']} ml of milk")
        print(f"{self.stock['beans']} g of coffee beans")
        print(f"{self.stock['cups']} disposable cups")
        print(f"{self.stock['money']} of money")


    def write_action(self, action):
        if action == 'fill':
            new_stock = fill_coffee(self.stock)
        elif action == 'take':
            new_stock = take_money(self.stock)
        elif action == 'buy':
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            try:
                coffee_type = int(input())
                new_stock = brew_coffee(coffee_type, self.stock)
            except:
                return self.stock     
        self.stock = new_stock
        return self.stock

coffee_machine_1 = CoffeMachine(initial_stock)


def fill_coffee(stock):
    print("Write how many ml of water you want to add:")
    stock['water'] += int(input())
    print("Write how many ml of milk you want to add:")
    stock['milk'] += int(input())
    print("Write how many grams of coffee beans you want to add:")
    stock['beans'] += int(input())
    print("Write how many disposable cups of coffee you want to add:")
    stock['cups'] += int(input())
    return stock

def take_money(stock):
    print(f"I gave you {stock['money']}")
    stock['money'] = 0
    return stock

def check_stock(stock, _water, _milk, _beans, _cups, _money):
    stock['water'] -= _water
    stock['milk'] -= _milk
    stock['beans'] -= _beans
    stock['cups']  -= _cups
    stock['money'] += _money
    for key, value in stock.items():
        if value < 0:
            return f"Sorry, not enough {key}!"
    print("I have enough resources, making you a coffee!")
    return stock


def brew_coffee(coffee_type, stock):
    new_stock = dict(stock)
    if coffee_type == 1:
        new_stock = check_stock(new_stock, 250, 0, 16, 1, 4)
    elif coffee_type == 2:
        new_stock = check_stock(new_stock, 350, 75, 20, 1, 7)
    elif coffee_type == 3:
        new_stock = check_stock(new_stock, 200, 100, 12, 1, 6)

    if type(new_stock) == str:
        print(new_stock)
        return stock
    return new_stock

def run_coffee_machine():
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == 'exit':
        return
    elif action == 'remaining':
        coffee_machine_1.get_stock()
    else:
        coffee_machine_1.write_action(action)
    return run_coffee_machine()

run_coffee_machine()
