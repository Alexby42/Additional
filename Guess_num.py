import random
a = random.randint(1, 100)
b = 0
print('Угадайте число от 1 до 100!')
while(b != a):
    b = int(input('Введите число:'))
    if (b > a):
        print('Введите меньшее число:')
    elif (b != a):
        print('Введите большее число:')
print('Вы угадали!!!')