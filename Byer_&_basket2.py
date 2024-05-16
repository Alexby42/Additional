class Customer:
    def __init__(self):
        self.login = 'Иван'
        self.password = '123456'
    def entry(self):
        error = ('Неверный логин или пароль')
        login = input('Введите Ваш Логин:')
        if login == self.login:
            password = input('Введите Ваш Пароль:')
            if password == self.password:
                print('Вы успешно авторизированы!')
            if password != self.password:
                print('Неверный Пароль!')
                exit()
        if login != self.login:
            print('Неверный Логин!')
            exit()
class ShoppingCart(Customer):
    def __init__(self):
        self.shop = {'хлеб': 30, 'молоко': 60, 'яйцо': 130}
        self.shopping_cart = {}
    def info(self):
        for items in self.shopping_cart:
            print('Корзина:', items, '-', self.shopping_cart[items])
        for items in self.shop:
            print('Магазин:', items, '-', self.shop[items])
    def purchase(self):
        prod = input('Приобретаемый продукт:')
        price = int(input('Его стоимость:'))
        self.shopping_cart[prod] = price
        print("{0} добавлено в корзину".format(prod))
        del self.shop[prod]
    def reject(self):
        prod = input('Возвращаемый продукт:')
        price = int(input('Его стоимость:'))
        del self.shopping_cart[prod]
        print("{0} удалено из корзины".format(prod))
        self.shop[prod] = price
    def sumCart(self):
        summa = 0
        summa = sum(self.shopping_cart.values())
        print('Итоговая сумма:', summa)
def main():
    cust = Customer()
    # cust.entry()
    shop = ShoppingCart()
    choice = None
    while choice != '0':
        print("""
            Меню магазина
            0 - выход
            1 - добавить продукт
            2 - удалить продукт
            3 - сумма покупок
            4 - содержимое корзины
            """)
        choice = input('Ваш выбор:')
        print()
        if choice == '0':
            print('Вы покидаете магазин!')
        elif choice == '1':
            shop.purchase()
        elif choice == '2':
            shop.reject()
        elif choice == '3':
            shop.sumCart()
        elif choice == '4':
            shop.info()
        else:
            print('Такого пункта нет!')
main()