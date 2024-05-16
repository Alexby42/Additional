class Customer:
    def __init__(self):
        self.name = 'Иван'
        self.fone_number = '+79875555555'
    def __str__(self):
        return f'Покупатель: {self.name}, Номер телефона: {self.fone_number}'
class ShoppingCart(Customer):
    def __init__(self):
        self.shop = {'хлеб': 30, 'молоко': 60, 'яйцо': 130}
        self.shopping_cart = {}
    def info(self):
        for items in self.shopping_cart:
            print('Корзина:', items, '-', self.shopping_cart[items])
        for items in self.shop:
            print('Магазин:', items, '-', self.shop[items])
    def purchase(self, prod, price):
        self.shopping_cart[prod] = price
        print("{0} добавлено в корзину".format(prod, price))
        del self.shop[prod]
    def reject(self, prod, price):
        del self.shopping_cart[prod]
        print("{0} удалено из корзины".format(prod, price))
        self.shop[prod] = price
    def sumCart(self):
        sum = 0
        for i in self.shopping_cart:
            sum = sum + self.shopping_cart[i]
        return sum
cust = Customer()
print(cust)
shop = ShoppingCart()
print()
shop.purchase('хлеб', 30)
shop.purchase('яйцо', 130)
print('Итоговая сумма:', shop.sumCart())
print()
shop.info()
print()
shop.reject('хлеб', 30)
print()
shop.info()
print()
print('Итоговая сумма:', shop.sumCart())