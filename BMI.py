def body_mass_index(mass, height):
    res = mass / (height * height)
    return res
mass = float(input('Ваш вес в кг: '))
height = float(input('Ваш рост в м: '))
bmi = body_mass_index(mass, height)
if (20 < bmi <25):
    print('Ваш индекс массы тела составляет:', bmi.__round__(2),'\nИдеальный вес. Вы здоровы!')
elif (26 < bmi <30):
    print('Ваш индекс массы тела составляет:', bmi.__round__(2),'\nНе критичное наличие лишнего веса')
elif (31 < bmi <35):
    print('Ваш индекс массы тела составляет:', bmi.__round__(2),'\nПервая стадия ожирения. Есть риск для здоровья!')
else:
    print('Ваш индекс массы тела составляет:', bmi.__round__(2),'\nПродвинутое ожирение. Необходимо обратиться к врачу!')