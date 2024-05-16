class BankAccount:
    def __init__(self):
        self.balance = 0
        print('Ваш баланс равен нулю!')
    def deposit(self):
        summa = int(input('Внесите средства на Ваш счет:'))
        self.balance += summa
        print('Ваш баланс:', summa)
    def withdraw(self):
        summa = int(input('Введите сумму для снятия:'))
        if self.balance >= summa:
            self.balance -= summa
            print('Вы снимаете:', summa)
        else:
            print('Недостаточно средств!')
    def balance_(self):
        print('Остаток на счете:', self.balance)
my_account = BankAccount()
my_account.deposit()
my_account.withdraw()
my_account.balance_()