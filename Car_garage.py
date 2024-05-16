class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
class Garage(Car):
    def __init__(self, model, year):
        self.list_ = [model, year]
    def info(self):
        print(self.list_)
    def add_auto(self, model, year):
        self.list_.append(model)
        self.list_.append(year)
        print(self.list_)
    def del_auto(self, model, year):
        self.list_.remove(model)
        self.list_.remove(year)
        print(self.list_)
car = Car
garage = Garage('ВАЗ', 1980)
garage.info()
garage.add_auto('ПАЗ', 1995)
garage.del_auto('ВАЗ', 1980)