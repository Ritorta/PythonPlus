# 1. Решить задачи, которые не успели решить на семинаре.

#-----------
#Задача №1
#-----------

# Создайте несколько переменных рахных типов.
# Проверьте к какому типу относятся созжанные переменные.

# a = 12
# b = 'Test'
# c = 3.14
# d = True

# print(f'{type (a) = }')
# print(f'{type (d) = }')
# print(f'{type (c) = }')
# print(f'{type (d) = }') 

#-----------
#Задача №2
#-----------

# Создайте в переменной data список значений разных типов
# перечислив их через запятую внутри квадратных скобок.
# Для кадого элемента в цикле выведите:
# - порядковый номер начиная с единицы
# - значение
# - адрес в памяти
# - размер в памяти
# - хэш объекта
# - результат проверки на целое число только если он положительный
# - результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты. 

# import sys

# data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет мир!']

# for nn, value in enumerate(data, 1):
#     cheak_int = 'Is in instanse Number' if isinstance(value, int) else ''
#     cheak_str = 'Is in instanse String'if isinstance(value, str) else ''
#     print(f'№ {nn}, Object: {value};' 
#             f'\nAdress in memory: {id(value)}, Sizee in memory: {sys.getsizeof(value)}'
#             f'\nHash object: {hash(value)}, Cheak: {cheak_int}{cheak_str}')

#-----------
#Задача №3
#-----------
    
# Напишите программу, которая получает целое число и возвращает его двоичное, 
# восьмеричное строковое представление.
# Функция bin и ost используйте для проверки своего результата, а не для решения.
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления.
# Избегайте магических чисел.
# Добавьте аннотацию типов где это возможно

# BIN = 2
# OCT = 8

# num = int(input('Enter the nubmer: '))

# for div in (BIN, OCT):
#     res: str = ''
#     temp_num: int = num 
#     while temp_num > 0:
#         res = str(temp_num % div) + res
#         temp_num = temp_num // div
#     print(f'{div = } {res = }')
# print(f'Bin cheak: {bin(num)}, Oct cheak: {oct(num)}')

#-----------
#Задача №4
#-----------

# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не привышает 1000 у.е
# Точность вычсления должна состовлять не менее 42 знаков после запятой.

# import math
# import decimal

# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)

# d = decimal.Decimal(input('Enter diametr circule: '))
# while d > 1000:
#     print('Icoret number')
#     d = decimal.Decimal(input('Enter diameter circle: '))

# print(f'Area circle: {PI * (d / 2) ** 2}; \nLingth diameter {PI * d}')

#-----------
#Задача №5
#-----------

# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

# a = float(input('Enter ratio a: '))
# b = float(input('Enter ratio b: '))
# c = float(input('Enter ratio c: '))

# d = b ** 2 - 4 * a * c

# if d > 0:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     res = f'The equation has two roots: \nx1 = {round(x1.real, 2)}, \nx2 = {round(x2.real, 2)}'
# elif d == 0:
#     x = - b / (2 * a)
#     res = f'The equation has one roots: \n{x = }'
# else:
#     d = complex(d, 0)
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     res = (f'The equation has two complex roots: \nx1 = {round(x1.real, 2) + round(x1.imag, 2) * 1j},' 
#         f'\nx2 = {round(x2.real, 2) + round(x2.imag, 2) * 1j}')
# print(res)

#-----------
#Задача №6
#-----------

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е
# Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богаство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

