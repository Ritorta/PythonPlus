# Урок 1. Основы Python

# Условие
# 1. Решить задачи, которые не успели решить на семинаре.


#-----------
# Задача №6
#-----------

# Напишите программу, которая запрашивает год и проверяет его на високостьность.
# РАспишите все возможности проверки в цепочки elif
# Откажитесь от машических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

# REFORM = 1582
# BIG_LEAP_YERA = 400
# SMALL_LEAP_YEAR = 4
# LARGE_NONE_LEAP_YEAR = 100
# MULTIPLE = 0

# year = int(input("Enter the year: "))
# if year < REFORM:
#     res = "Grigoria calendar dont enter"
# elif year % BIG_LEAP_YERA == MULTIPLE:
#     res = f'{year} - leap year'
# elif year % LARGE_NONE_LEAP_YEAR == MULTIPLE:
#     res = f'{year} - Dont leap year'
# elif year % SMALL_LEAP_YEAR == MULTIPLE:
#     res = f'{year} - leap year'
# else:
#     res = f'{year} - Dont leap year'
# print(res)

#-----------
# Задача №7
#-----------

# Пользователь вводит чисто от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двухзначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двухзначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25 (ноль в начале не учитывается)
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# LOWER_LIMIT = 1
# UPPER_LIMIT = 9999
# ONE = 1
# TEN = 10
# HUNDGRED = 100
# SQUARE = 2

# num = LOWER_LIMIT - ONE
# while num < LOWER_LIMIT or num > UPPER_LIMIT:
#     num = int(input(f'Enter number in {LOWER_LIMIT} to {UPPER_LIMIT}: '))
# if num < TEN:
#     res = f'Number {num} - sungele number and square = {num ** SQUARE}'
# elif num < HUNDGRED:
#     fist_num = num // TEN
#     second_num = num % TEN
#     res = f'Number {num} - dual number and multiplay = {fist_num * second_num}'
# else:
#     fist_num = num // HUNDGRED
#     second_num = num // TEN % TEN
#     third_num = num % TEN
#     mirror = third_num * HUNDGRED + second_num * TEN + fist_num
#     res = f'Number {num} - third number and mirror = {mirror}'
# print(res)

#-----------
# Задача №8
#-----------

# Написовать в консоли ёлку спросив у пользователя колличество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

# SPACE = ' '
# STAR = '*'
# ONE = 1
# TWO = 2

# rows = int(input('Enter the number rows: '))
# spaces = rows - ONE
# stars = ONE
# for i in range(rows):
#     print(spaces * SPACE + stars * STAR)
#     spaces -= ONE
#     stars += TWO

#-----------
#Задача №9
#-----------

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

LOWER_LIMIT = 2
UPPER_LIMET = 10
COLUMN = 4

for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN):
    for second_num in range(LOWER_LIMIT, UPPER_LIMET + 1):
        for first_num in range(i_main, i_main + COLUMN):
            print(f'{first_num : > 2} x {second_num : > 2} = {first_num * second_num : > 2}', end='\t')
        print()
    print()
