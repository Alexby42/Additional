weight = int(input('Введите вес: '))
price = 50
if weight <=2:
    print('Стоимость в руб - ' + str(price))
elif 3 <= weight <=10:
        if weight == 3:
            price +=20
            print('Стоимость в руб - ' + str(price))
        if weight == 4:
            price +=40
            print('Стоимость в руб - ' + str(price))
        if weight == 5:
            price +=60
            print('Стоимость в руб - ' + str(price))
        if weight == 6:
            price +=80
            print('Стоимость в руб - ' + str(price))
        if weight == 7:
            price +=100
            print('Стоимость в руб - ' + str(price))
        if weight == 8:
            price +=120
            print('Стоимость в руб - ' + str(price))
        if weight == 9:
            price +=140
            print('Стоимость в руб - ' + str(price))
        if weight == 10:
            price += 160
            print('Стоимость в руб - ' + str(price))
else:
    price = 200
    print('Стоимость в руб - ' + str(price))
