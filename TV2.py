class Television:
    def __init__(self):
        self.chanel = 1
        self.sound = 0
    def start(self):
        print('Телевизор включен!')
    def info(self):
        print(f'Текущий канал: {self.chanel} Уровень громкости: {self.sound}')
    def ins_chanel(self):
        repl = int(input('Введите номер канала:'))
        if repl < 0 > 200:
            print('Канала с таким номером не существует')
        else:
            self.chanel = repl
            print('Текущий номер канала:', self.chanel)
    def ins_sound_up(self):
        sound_up = int(input('Добавляем громкость:'))
        self.sound += sound_up
        if self.sound > 100:
            self.sound = 100
        print('Текущий уровень громкости:', self.sound)
    def ins_sound_down(self):
        sound_down = int(input('Убавляем громкость:'))
        self.sound -= sound_down
        if self.sound < 0:
            self.sound = 0
        print('Текущий уровень громкости:', self.sound)
def main():
    television = Television()
    television.start()
    choice = None
    while choice != '0':
        print("""
            Меню управления TV
            0 - выход
            1 - выбрать канал
            2 - добавить громкость
            3 - убавить громкость
            4 - текущий канал
            """
            )
        choice = input('Ваш выбор:')
        print()
        if choice == '0':
            print('Телевизор выключен!')
        elif choice == '1':
            television.ins_chanel()
        elif choice == '2':
            television.ins_sound_up()
        elif choice == '3':
            television.ins_sound_down()
        elif choice == '4':
            television.info()
        else:
            print('Такого пункта нет!')
main()