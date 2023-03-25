"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

def check_equality(number, right_part, left_part = 0):
    if number == 0:
        if left_part == right_part:
            print('Равенство выполняеться')
        else:
            print('Равенство не выполняеться')
    else:
        left_part += number
        number -= 1
        (check_equality(number, right_part, left_part))


number = input('Введите натуральное число: ')
try:
    number = int(number)
except ValueError:
    print('Ввели не число')
else:
    right_part = number * (number + 1) / 2
    print(f'Правая часть = {right_part}')
    check_equality(number=number, right_part=right_part)
