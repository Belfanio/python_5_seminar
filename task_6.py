"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random

def guess_number(random_number, count_of_try = 1):
    check_number = input('Введите ваш вариант числа: ')
    try:
        check_number = int(check_number)
    except ValueError:
        print('Ввели не число, поробуйте снова')
        guess_number(random_number, count_of_try)
    else:
        if check_number == random_number:
            print(f'Верно, загаданное число было {random_number}')
        elif count_of_try == 10:
            print(f'К сожалению Вы не угадали, было загадано число {random_number}')
        else:
            if check_number < random_number:
                print('Введенное Вами число меньше загаданного')
                count_of_try += 1
                guess_number(random_number, count_of_try)
            else:
                print('Введенное Вами число больше загаданного')
                count_of_try += 1
                guess_number(random_number, count_of_try)


random_number = random.randint(0, 100)
print(f'Рандомное число {random_number}')
guess_number(random_number)