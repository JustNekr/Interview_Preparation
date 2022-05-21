"""
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Если есть  значения, которым не хватило ключей, их необходимо отбросить.
"""


def dict_creator(keys: list, values: list) -> dict:
    if len(keys) > len(values):
        for _ in range(len(keys) - len(values)):
            values.append(None)
    return {f'{key}': value for key, value in zip(keys, values)}


if __name__ == '__main__':
    keys_list = [f'key_{num}' for num in range(int(input('ввкдите количество ключей: ')))]
    values_list = [num for num in range(int(input('ввкдите количество значений: ')))]
    print(dict_creator(keys_list, values_list))


