"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение (например example345). Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.
"""
import random
import string


def create_file(file_name):

    _letters = string.ascii_letters
    _digits = string.digits

    _asci_list = [''.join(random.choice(_letters) for _ in range(5)) for _ in range(5)]
    _digit_list = [''.join(random.choice(_digits) for _ in range(5)) for _ in range(5)]

    try:
        with open(file_name, 'x', encoding='UTF-8') as file:
            for text, nums in zip(_asci_list, _digit_list):
                file.write(text + nums + '\n')
    except FileExistsError:
        print("Файл уже существует")


def read_file(file_neme):
    with open(file_neme, 'r', encoding='UTF-8') as file:
        for line in file:
            print(line, end='')


if __name__ == '__main__':
    name = input('Введите название файла: ')
    create_file(name)
    read_file(name)
