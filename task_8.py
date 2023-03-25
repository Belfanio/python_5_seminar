"""
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def pow_number(first_number, second_number, result = 1):
    if second_number == 0:
        print(f'Первое введенное число возведенное в степень {result}')
    else:
        result *= first_number
        second_number -= 1
        pow_number(first_number, second_number, result)


first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print('Одно или оба введенных значения являеться не числом')
else:
    pow_number(first_number, second_number)