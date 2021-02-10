# Function Syntax
# def function_name(param1, parm2,...parmn):
#     stmt1
#     .....
#     stmtn
# def function_name():
#     stmt1
#     .....
#     stmtn    

# def sum(x, y): # x= 10, y =20
#     s = x + y  # s = 10 + 20 => 30
#     print(s)   # returns 30

# a = 10
# b = 20

# sum(a,b) # sum(10, 20) => 30

#3 to 10
# def first(x, y):
#     for i in range(x, y):
#         print(i)
# first(20, 31)
# first(12, 21)

# Class Syntax

# class class_name:
#     def __init__(self, param1, param2, ...,paramn):
#         stmt1
#         .....
#         stmt2
#     def user_function(param1, param2, ...,paramn)
#         stmt1
#         .....
#         stmt2

class car:
    def __init__(self, name = None, tyre=None, engine=None, hood=None, like = None):
        self.name = name 
        self.tyre = tyre
        self.engine = engine
        self.hood = hood
        self.like = like
    
    def isliked(self):
        if self.like > 3.5:
            print(self.name +" is Liked")
        else:
            print(self.name + " is not liked")

new_car = car('XYZ')
new_car.tyre = "30cm"
new_car.engine  = "V8"
new_car.hood = "Vented"
new_car.like = 2

print(new_car.name, new_car.tyre, new_car.engine, new_car.hood)
print(new_car.isliked())

next_car = car()
next_car.name = "PQY"
next_car.like = 4
print(next_car.isliked())

    



