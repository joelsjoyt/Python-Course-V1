"""
This file contains the basics of Class

Syntax:
    class ClassName:
        def __init__(self):
            pass

        def next_function(self):
            pass
"""

class CarA:
    def __init__(self, name=None, hp=None):
        self.name = name
        self.hp = hp        
    
    def display_car(self):
        print(f'Car name: {self.name}, Car HP: {self.hp}')

cara_1 = CarA('1','300')
cara_2 = CarA('2','500')
cara_1.display_car()
cara_2.display_car()

class CarB:
    def __init__(self):
        self.name = None
        self.hp = None      
    
    def display_car(self):
        print(f'Car name: {self.name}, Car HP: {self.hp}')

carb_1 = CarB()
carb_1.name = 'XYZ'
carb_1.hp = 400
carb_1.display_car()


class UserTransaction:
    def __init__(self, balance = None, price = None):
        self.balance = balance
        self.price = price
        # method 1 for calling instance function
        self.calculate_balance() 
            
    def calculate_balance(self):
        if self.price > self.balance:
            print("Transaction Failed")
        else:
            print("Transaction Succesful")
            self.balance -= self.price
        self.show_balance()
    
    def show_balance(self):
        print(f'Remaining balance: {self.balance}')

transaction1 = UserTransaction(1000,200)
# method 2 for calling instance function
# transaction1.calculate_balance()
# transaction1.show_balance()

