"""
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно) заменить на значения типа 345example
(в обратном порядке, число и строка).
Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.
Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
"""
import random
import re
import string


def create_file(file_name):
    _letters = string.ascii_letters
    _digits = string.digits

    _asci_list = [''.join(random.choice(_letters) for _ in range(5)) for _ in range(5)]
    _digit_list = [''.join(random.choice(_digits) for _ in range(5)) for _ in range(5)]

    try:
        with open(file_name, 'x', encoding='UTF-8') as file:
            for text, nums in zip(_asci_list, _digit_list):
                if random.random() < 0.5:
                    file.write(text + nums + '\n')
                else:
                    file.write(nums + text + '\n')
    except FileExistsError:
        print("Файл уже существует")


def read_file_simple(file_neme):
    with open(file_neme, 'r', encoding='UTF-8') as file:
        for line in file:
            print(line, end='')


def cleaned_file(file_name):
    cleaned_data = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            if re.match(r'\d+\D+\n', line):
                cleaned_data.append(line[re.match(r'\d+', line).end():-1] + re.match(r'\d+', line).group(0) + line[-1:])
            else:
                cleaned_data.append(line)

    with open(file_name, 'w', encoding='UTF-8') as file:
        for line in cleaned_data:
            file.write(line)


if __name__ == '__main__':
    name = input('Введите название файла: ')
    create_file(name)
    read_file_simple(name)
    print('*' * 10)
    cleaned_file(name)
    read_file_simple(name)
