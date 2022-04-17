class CoffeMachine:
    
    def __init__(self, water, milk, beans):
        self.water = water
        self.milk = milk
        self.beans = beans
        
    def get_coffee(self, cups):
        self.cups = cups
        self.water_supply = self.water // 200
        self.milk_supply = self.milk // 50
        self.beans_supply = self.beans // 15
        
        self.available_amount = min(self.water_supply, self.milk_supply, self.beans_supply)
        self.coffe_left = self.available_amount - self.cups 
        
        if self.cups > self.available_amount:
            print(f'No, I can make only {self.available_amount} cups of coffee')
        elif self.cups == self.available_amount:
            print(f'Yes, I can make that amount of coffee')
        elif self.cups < self.available_amount:
            print(f'Yes, I can make that amount of coffee (and even {self.coffe_left} more than that)')

print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")  
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")   
cups = int(input())

my_coffee = CoffeMachine(water, milk, beans)
my_coffee.get_coffee(cups)