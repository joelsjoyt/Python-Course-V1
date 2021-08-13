class Transaction:
    def __init__(self, balance=None, debit=None, credit=None):
        self.balance = balance
        self.debit = debit
        self.credit = credit
        self.mode = None
        self.update_balance()
    
    def check_mode(self):
        if self.credit > 0:
            return 1
        elif self.debit > 0:
            return 0
        elif self.debit <= 0 and self.credit <= 0 :
            return -1

    def update_balance(self):
        self.mode = self.check_mode()
        if self.mode == 1:
            self.balance += self.credit
            print(f'Transaction succesful, Balance:{self.balance}')
        elif self.mode == 0:
            self.balance -= self.debit
            print(f'Transaction succesful, Balance:{self.balance}')
        else:
            print(f'Transaction NULL, Balance:{self.balance}') 

def main():
    transaction = Transaction(1000, 0, 0)
    transaction.credit = 100
    transaction.update_balance()

if __name__ == '__main__':
    main()