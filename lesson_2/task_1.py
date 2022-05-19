"""
Создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре:
название и цену.
Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке вида (“{название товара} {цена товара}”).
Создать экземпляры родительского класса и дочернего. Распечатать информацию о товаре.
"""


class ItemDiscount:
    name = 'name'
    price = 'price'


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f"{self.name} {self.price}")


if __name__ == "__main__":
    my_parent = ItemDiscount()
    my_child = ItemDiscountReport()

    my_child.get_parent_data()
