class Book:
    def __init__(self, title, author, style, price):
        self.title = title
        self.author = author
        self.style = style
        self.price = price
    def display(self):
        print(f'Название: {self.title}, Автор: {self.author}, Жанр: {self.style}, Цена: {self.price}')
class Library(Book):
    def __init__(self):
        self.lib_ = []
    def add_book(self, title, author):
        self.lib_.append(title)
        self.lib_.append(author)
        return self.lib_
    def find(self, author):
        if author in self.lib_:
            print('Автор найден в списке!')
        else:
            print('Автор отсутствует в списке!')
    def info(self):
        print(*self.lib_, sep='\n')
lib = Library()
lib.add_book('Библия', 'Коллектив')
lib.add_book('Маленький принц', 'Антуан де Сент-Экзюпери')
lib.add_book('Повесть о двух городах', 'Чарльз Диккенс')
lib.add_book('Властелин колец', 'Джон Рональд Роуэл Толкин')
lib.add_book('Дон Кихот', 'Мигель де Сервантес')
lib.info()
print()
lib.find('Мигель де Сервантес')
lib.find('Кант')