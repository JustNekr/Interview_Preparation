"""
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
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


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount: int):
        super().__init__()
        self.__discount = discount

    def __str__(self):
        print()
        return str(self.price - self.price / 100 * self.__discount)

    def get_parent_data(self):
        print(f"{self.name} {self.price}")


if __name__ == "__main__":
    my_parent = ItemDiscount()
    my_child = ItemDiscountReport(0.8)
    my_child.price = 100

    print(my_child)
