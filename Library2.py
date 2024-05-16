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
        #super().__init__(self)
        self.lib_ = []
    def add_book(self):
        title = input('Введите название книги:')
        author = input('Введите автора:')
        self.lib_.append(title)
        self.lib_.append(author)
        return self.lib_
    def find(self):
        author = input('Введите автора:')
        if author in self.lib_:
            print('Автор найден в списке!')
        else:
            print('Автор отсутствует в списке!')
    def info(self):
        print(*self.lib_, sep='\n')
def main():
    lib = Library()
    choice = None
    while choice != '0':
        print("""
            Меню управления библиотекой:
            0 - выход
            1 - добавить книгу
            2 - текущий список книг
            3 - поиск книг
            """)
        choice = input('Ваш выбор:')
        print()
        if choice == '0':
            print('Работа закончена!')
        elif choice == '1':
            lib.add_book()
        elif choice == '2':
            lib.info()
        elif choice == '3':
            lib.find()
        else:
            print('Такого пункта нет!')
main()