"""
Реализовать возможность переустановки значения цены товара в родительском классе.
Проверить, распечатать информацию о товаре.
"""


class ItemDiscount:
    __name = 'name'
    __price = 'price'

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

    def get_parent_data(self):
        print(f"{self.name} {self.price}")


if __name__ == "__main__":
    my_parent = ItemDiscount()
    my_child = ItemDiscountReport()

    my_child.get_parent_data()

    my_child.name = 'техника Apple'
    my_child.price = 'неоправданно дорого'

    my_child.get_parent_data()
