sumall = 0
# определяем функцию для вычисления суммы цифр в числе
def digit_sum(n):
    return sum(int(d) for d in str(n))

# определяем список с количеством дней в каждом месяце
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# определяем функцию для подсчета суммы цифр всех дат для каждого месяца
def month_digit_sums(year):
    # проверяем, является ли год високосным
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    # если год високосный, то меняем количество дней в феврале
    if is_leap_year:
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

    # создаем список с суммами цифр для каждого месяца
    month_sums = [0] * 12

    # перебираем все дни в году и добавляем сумму цифр в соответствующий месяц
    for month, days in enumerate(days_in_month):
        for day in range(1, days + 1):
            month_sums[month] += digit_sum(day)

    return month_sums

# запрашиваем у пользователя год
year = int(input("Введите год: "))

# вызываем функцию и выводим результаты
digit_sums = month_digit_sums(year)
month_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
for i, sum in enumerate(digit_sums):
    print(f"{month_names[i]}: {sum}")
    sumall+=sum
print("Сумма всех месяцев -",sumall)
