"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
целых неотрицательных чисел. Из всех арифметических операций допускаются только
+1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""

def sum_of_digit(first_number, second_number):
    if second_number == 0:
        print(f'Сумма введенных чисел = {first_number}')
    else:
        first_number += 1
        second_number -= 1
        sum_of_digit(first_number, second_number)

first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print('Одно или оба введенных значения являеться не числом')
else:
    sum_of_digit(first_number, second_number)