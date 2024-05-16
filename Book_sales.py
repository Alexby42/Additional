class Book:
    def __init__(self, title, author, style, price):
        self.title = title
        self.author = author
        self.style = style
        self.price = price
    def display(self):
        print(f'Название: {self.title}, Автор: {self.author}, Жанр: {self.style}, Цена: {self.price}')
    def discount(self):
        self.res = self.price - (self.price * 0.1)
        print('Цена с учетом скидки 10%:', self.res)
book = Book('Библия', 'Коллектив', 'Религия', 1000)
book.display()
book.discount()
book1 = Book('Маленький принц', 'Антуан де Сент-Экзюпери', 'Повесть', 800)
book1.display()
book1.discount()
book2 = Book('Дон Кихот', 'Мигель де Сервантес', 'Роман', 750)
book2.display()
book2.discount()
book3 = Book('Повесть о двух городах', 'Чарльз Диккенс', 'Роман', 600)
book3.display()
book3.discount()
book4 = Book('Властелин колец', 'Джон Рональд Роуэл Толкин', 'Фэнтези', 500)
book4.display()
book4.discount()