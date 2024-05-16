class Book:
    def __init__(self):
        self.list1 = ['Библия', 'Коллектив', 'Религия', 1000,
                      'Дон Кихот', 'Мигель де Сервантес', 'Роман', 750,
                      'Властелин колец', 'Джон Рональд Роуэл Толкин', 'Фэнтези', 500]
        self.list2 = self.list1.copy()
    def display(self):
        keys1 = ['Название', 'Автор', 'Жанр', 'Цена']
        values1 = self.list1
        res1 = {i: j for (i, j) in zip(keys1, values1)}
        print(res1)
        del self.list1[0:4]
        keys2 = ['Название', 'Автор', 'Жанр', 'Цена']
        values2 = self.list1
        res2 = {i: j for (i, j) in zip(keys2, values2)}
        print(res2)
        del self.list1[0:4]
        keys3 = ['Название', 'Автор', 'Жанр', 'Цена']
        values3 = self.list1
        res3 = {i: j for (i, j) in zip(keys3, values3)}
        print(res3)
        price1 = res1.get('Цена')
        price2 = res2.get('Цена')
        price3 = res3.get('Цена')
        summa = price1 + price2 + price3
        print('Общая стоимость:', summa)
    def discount(self):
        num_list = [i for i in self.list2 if isinstance(i, int)]
        result = sum(num_list) - (sum(num_list) * 0.1)
        print('Цена с учетом скидки 10%:', result)
def main():
    book = Book()
    choice = None
    while choice != '0':
        print("""
            Меню магазина книг
            0 - выход
            1 - информация о покупке
            2 - применить скидку
            """)
        choice = input('Ваш выбор:')
        print()
        if choice == '0':
            print('Выход!')
        elif choice == '1':
            book.display()
        elif choice == '2':
            book.discount()
        else:
            print('Такого пункта нет!')
main()