class BankAccount:
    def __init__(self):
        self.balance = [0]
        print('Ваш баланс равен нулю!')
    def deposit(self):
        summa = int(input('Внесите средства на Ваш счет:'))
        self.balance.append(summa)
    def withdraw(self):
        summa = int(input('Введите сумму для снятия:'))
        if sum(self.balance) >= summa:
            s = sum(self.balance) - summa
            print('Вы снимаете:', summa)
        else:
            print('Недостаточно средств для снятия!')
            return summa
        self.balance.clear()
        self.balance.append(s)
    def balance_(self):
        print('Остаток на счете:', sum(self.balance))
def main():
    my_account = BankAccount()
    choice = None
    while choice != '0':
        print("""
            Меню управления счетом
            0 - выход
            1 - внесение средств
            2 - снятие средств
            3 - текущий баланс
            """)
        choice = input('Ваш выбор:')
        print()
        if choice == '0':
            print('Работа со счетом закончена!')
        elif choice == '1':
            my_account.deposit()
        elif choice == '2':
            my_account.withdraw()
        elif choice == '3':
            my_account.balance_()
        else:
            print('Такого пункта нет!')
main()