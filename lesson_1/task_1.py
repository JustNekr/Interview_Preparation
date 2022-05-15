def multiplication(number):
    number = int(number)
    for my_factor in range(1, number + 1):
        for default_factor in range(1, 11):
            print(f'{my_factor} * {default_factor} = {my_factor * default_factor}')
        print('-----')


if __name__ == '__main__':
    multiplication(input('введите число: '))
