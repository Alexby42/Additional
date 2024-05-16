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
television = Television()
television.start()
television.info()
television.ins_chanel()
television.ins_sound_up()
television.ins_sound_down()