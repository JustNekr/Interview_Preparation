"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
"""


class ItemDiscount:

    def __init__(self):
        self.__name = 'name'
        self.__price = 'price'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport1(ItemDiscount):

    def get_info(self):
        print(f"{self.name}")


class ItemDiscountReport2(ItemDiscount):

    def get_info(self):
        print(f"{self.price}")


if __name__ == "__main__":
    first_class = ItemDiscountReport1()
    second_class = ItemDiscountReport2()

    for obj in (first_class, second_class):
        obj.get_info()