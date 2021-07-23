"""
Day - 3 session on 
control statements and logical operators
"""

"""
    a -= 1 -> a = a - 1
    a += 1 -> a = a + 1

    Logical operators
    and, or, !(not)
"""

"""
    Syntax of if ..esle statements

    if control_statement:
        code to be done here
    elif control_statement:
        code to be done here
    else:
        code to be done here
"""

x = 1
y = 2
if x <= 1 and y > 1:
    print(f'Incremented X value is:{x+1}')
    # Nested IF..else statements
    if  x != 1:
        print(f'X value is:(Not equal){x}')
    else:
        print(f'X value is:(else){x}')
elif x > 1:
    print(f'Decremented X value is:{x-1}')
else:
    print(f' X value is:{x}')

acc_balance = 1000
apple = 500
orange = 6000


if (apple + orange) < acc_balance:
    acc_balance -= apple + orange
    # acc_balance = acc_balance - (apple + orange) 
    print(f'Transaction succesful --balance:{acc_balance}')
else:
    if apple >= acc_balance and orange >= acc_balance:
        print(f'Transaction failed --balance:{acc_balance}')
    elif apple >= acc_balance:
        acc_balance -= orange
        print(f'Cannot buy apple --balance:{acc_balance}')
    elif orange >= acc_balance:
        acc_balance -= apple
        print(f'Cannot buy orange --balance:{acc_balance}')

