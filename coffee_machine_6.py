class CoffeMachine:

    def __init__(self, stock):
        self.stock = stock

    def __str__(self):
        return f"The coffee machine has:\n" \
               f"{self.stock['water']} ml of water\n" \
               f"{self.stock['milk']} ml of milk\n" \
               f"{self.stock['beans']} g of coffee beans\n" \
               f"{self.stock['cups']} disposable cups\n" \
               f"${self.stock['money']} of money\n"

    def write_action(self, action):
        if action == 'fill':
            new_stock = self.fill_coffee(self.stock)
        elif action == 'take':
            new_stock = self.take_money(self.stock)
        elif action == 'buy':
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            try:
                coffee_type = int(input())
                new_stock = self.brew_coffee(coffee_type, self.stock)
            except:
                return self.stock     
        self.stock = new_stock
        return self.stock

    def fill_coffee(self, stock):
        print("Write how many ml of water you want to add:")
        stock['water'] += int(input())
        print("Write how many ml of milk you want to add:")
        stock['milk'] += int(input())
        print("Write how many grams of coffee beans you want to add:")
        stock['beans'] += int(input())
        print("Write how many disposable cups of coffee you want to add:")
        stock['cups'] += int(input())
        return stock

    def take_money(self, stock):
        print(f"I gave you {stock['money']}")
        stock['money'] = 0
        return stock

    def check_stock(self, stock, _water, _milk, _beans, _cups, _money):
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


    def brew_coffee(self, coffee_type, stock):
        new_stock = dict(stock)
        if coffee_type == 1:
            new_stock = self.check_stock(new_stock, 250, 0, 16, 1, 4)
        elif coffee_type == 2:
            new_stock = self.check_stock(new_stock, 350, 75, 20, 1, 7)
        elif coffee_type == 3:
            new_stock = self.check_stock(new_stock, 200, 100, 12, 1, 6)

        if type(new_stock) == str:
            print(new_stock)
            return stock
        return new_stock

    def run_coffee_machine(self):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'exit':
            return
        elif action == 'remaining':
            print(coffee_machine_1)
        else:
            coffee_machine_1.write_action(action)
        self.run_coffee_machine()

if __name__ == '__main__':
    coffee_machine_1 = CoffeMachine({'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550})
    coffee_machine_1.run_coffee_machine()



