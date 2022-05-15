"""
Реализовать функцию print_directory_contents(path).
Функция принимает имя директории и выводит ее содержимое,
включая содержимое всех поддиректории (рекурсивно вызывая саму себя).
Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
"""
import os


def print_directory_contents(path, nesting_count=1):
    print(path.split('\\')[-1] + '\\')
    directory_items = os.listdir(path)
    nesting_directory = []
    while directory_items:
        if os.path.isfile(f'{path}\\{directory_items[0]}'):
            print(f'{"--" * nesting_count}{directory_items[0]}')
            directory_items.remove(directory_items[0])
        else:
            nesting_directory.append(directory_items[0])
            directory_items.remove(directory_items[0])

    for directory in nesting_directory:
        print_directory_contents(f"{path}\\{directory}", nesting_count=nesting_count + 1)


if __name__ == '__main__':
    folder = input('Если оставите поле пустым будет просканированна текущая папка данного файла. Введите путь к '
                   'папке: ')
    if folder:
        print_directory_contents(folder)
    else:
        print_directory_contents(os.getcwd())

