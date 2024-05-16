class Animal:
    def __init__(self, type_, name):
        self.type_ = type_
        self.name = name
    def speak(self, sound):
        self.sound = sound
        print(f'{self.type_} по имени {self.name} издает звук {self.sound}')
animal = Animal('Собака', 'Шарик')
animal.speak('Гав')
animal = Animal('Кошка', 'Мурка')
animal.speak('Мяу')
animal = Animal('Утка', 'Колобок')
animal.speak('Кря-кря')
animal = Animal('Петух', 'Степан')
animal.speak('КУ-ка-ре-ку')