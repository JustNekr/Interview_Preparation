"""
Написать программу «Банковский депозит».
Клиент банка делает депозит на определенный срок.

В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).

Проценты начисляются на депозит в конце каждого месяца.
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада (в месяцах),
а на выходе возвращать сумму вклада на конец срока.

Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.

"""


def calculation(main_sum, months, bonus, percent):
    for month in range(months):
        if month != 0 and month != months - 1:
            main_sum += (main_sum / 100 * percent) / 12 + bonus
        else:
            main_sum += (main_sum / 100 * percent) / 12
    return f'{main_sum:.2f}'


def bank_deposit(main_sum, months, bonus):
    main_sum = int(main_sum)
    months = int(months)
    bonus = int(bonus)
    if months < 6:
        return 'incorrect months number'

    if main_sum < 1000:
        return 'you so poor'
    elif main_sum < 10000:
        if 12 <= months < 24:
            return calculation(main_sum, months, bonus, 6)
        else:
            return calculation(main_sum, months, bonus, 5)
    elif main_sum < 100000:
        if months < 12:
            return calculation(main_sum, months, bonus, 6)
        elif months < 24:
            return calculation(main_sum, months, bonus, 7)
        else:
            return calculation(main_sum, months, bonus, 6.5)
    elif main_sum < 1000000:
        if months < 12:
            return calculation(main_sum, months, bonus, 7)
        elif months < 24:
            return calculation(main_sum, months, bonus, 8)
        else:
            return calculation(main_sum, months, bonus, 7.5)


if __name__ == '__main__':
    main_sum = input('введите основную сумму: ')
    months = input('введите количество месяцев: ')
    bonus = input('введите дополнительную сумму: ')

    print(bank_deposit(main_sum, months, bonus))
