"""
Inheritence

class A:
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        super().__init__()
        pass
"""

class CarA:
    def __init__(self, name=None, hp=None):
        self.name = name
        self.hp = hp        
    
    def display_car(self):
        print(f'Car name: {self.name}, Car HP: {self.hp}')

class C(CarA):
    def __init__(self, name, hp, year, milage):
        super().__init__(name, hp)# => xyz, 300
        self.year = year
        self.milage = milage

    def show_car(self):
        print(f"Car Name : {self.name} Car HP: {self.hp}\nCar Year :{self.year}Car Milage: {self.milage}") 

carc_1 = C("XYZ",400,2021,30)
carc_1.show_car()


Parent class Bank
name
acc no