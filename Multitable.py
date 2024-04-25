num = int(input('Введите число: '))
print('Таблица умножения для', num, ':')
for i in range(1, 11):
    res = num * i
    print(num, 'x', i, '=', res)