"""
Explains the basics of functions

Syntax:
    def function_name(parms):
        code
"""


def sum1(a, b):
    res = a + b
    return res

def sum2(a, b):
    res = a + b
    print(res)

def sum3(a, b):
    res= a + b
    return res

print( sum1(10,20) )
print( sum1(50,50) )

sum2(30,40)

x = sum3(100,200)
print(x)

"""
Looping statements

1. While loop
    Syntax:
        while condition:
            code

2. For Loop
    Syntax:
        for i in range(startval, endval, step):
            code

"""

# While loop
i = 1
while i <= 5:
    print(i)
    i  += 1 

# For loop

for i in range(1,6,2): # 0,1,2,3,4,5
    print(i)

"""
Indexing
last negative index  -1
start index  0
nth index    n
"""

for i in range(6,-1,-2): # 0,1,2,3,4,5 
    print(i)

for i in range(1,-1,-1):
    print(i)


# Forward 50 100 while and for

# Bckward 150 100 for