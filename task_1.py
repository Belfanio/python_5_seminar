"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def arithmetic_operation():
    operation = input('Введите арифметическую операцию: ')
    if operation in ['+', '-', '/', '*', '0']:
        if operation == '0':
            print('Завершаем работу')
        else:
            first_number = input('Введите первое число: ')
            second_number = input('Введите второе число: ')
            try:
                first_number = int(first_number)
                second_number = int(second_number)
            except ValueError:
                print('Одно или оба введенных значения не являються числом')
                arithmetic_operation()
            else:
                    if operation == '+':
                        summ_of_number = first_number + second_number
                        print(f'Сумма двух чисел = {summ_of_number}')
                        arithmetic_operation()
                    elif operation == '-':
                        subtraction = first_number - second_number
                        print(f'Разность двух чисел = {subtraction}')
                        arithmetic_operation()
                    elif operation == '*':
                        multiplication = first_number * second_number
                        print(f'Результат умножения двух чисел = {multiplication}')
                        arithmetic_operation()
                    elif operation == '/':
                        try:
                            division = first_number / second_number
                        except ZeroDivisionError:
                            print('На ноль делить нельзя, введите другие значения')
                            arithmetic_operation()
                        else:
                            print(f'Результат деление двух чисел = {division}')
                            arithmetic_operation()
    else:
        print('Ввели неверную операцию, попробуйте снова')
        arithmetic_operation()

arithmetic_operation()