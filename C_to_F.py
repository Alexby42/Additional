def convert(grad):
    res = (grad * 1.8) + 32
    return res
cls = float(input('Введите значение температуры в градусах Цельсия: '))
fhr = convert(cls)
print(cls, 'градусов Цельсия эквивалентно', fhr.__round__(2), 'градусам Фаренгейта')