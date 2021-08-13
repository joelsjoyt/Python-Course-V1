from calc.mod_1 import sum
from calc.mod_2 import diff
from calc.mod_3 import prod
from transaction.balance import Transaction


def main():
    print(f'Sum: {sum(10,20)}')
    print(f'Diff: {diff(10,20)}')
    print(f'Prod: {prod(10,20)}')

    transaction = Transaction(10000, 0, 0)
    transaction.debit = 2000
    transaction.update_balance()
    transaction.credit = 2000
    transaction.update_balance()


if __name__ == '__main__':
    print(f'__name__:{__name__}')
    main()

