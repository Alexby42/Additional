class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
class Garage(Car):
    def __init__(self, model, year):
        self.list_ = [model, year]
    def info(self):
        print(self.list_)
    def add_auto(self):
        model = str(input('Введите модель:'))
        year = int(input('Введите год выпуска:'))
        self.list_.append(model)
        self.list_.append(year)
        return self.list_
    def del_auto(self):
        model = str(input('Введите модель:'))
        year = int(input('Введите год выпуска:'))
        self.list_.remove(model)
        self.list_.remove(year)
        return self.list_
def main():
    garage = Garage('ВАЗ', 1980)
    choice = None
    while choice != '0':
        print("""
            Меню управления гаражом
            0 - выход
            1 - добавить позицию
            2 - удалить позицию
            3 - текущий перечень
            """)
        choice = input('Ваш выбор:')
        print()
        if choice == '0':
            print('Работа закончена!')
        elif choice == '1':
            garage.add_auto()
        elif choice == '2':
            garage.del_auto()
        elif choice == '3':
            garage.info()
        else:
            print('Такого пункта нет!')
main()