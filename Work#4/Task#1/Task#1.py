# 1. Решить задачи, которые не успели решить на семинаре.

#-----------
# Задача №1
#-----------

# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самогодлинного
# слова был один пробел между ним и номером строки.


# def print_words(text: str) -> None: 
#     words_list = sorted(text.split())
#     max_len = len(max(words_list, key = len))

#     for nn, word in enumerate(words_list, 1):
#         print(f'{nn} {word:>{max_len}}')


# print_words('Съешь ещё этих вкусных сладких булок')

#-----------
# Задача №2
#-----------

# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


# def uni_list(text: str) -> list[int]:
#     result = []
#     for symbol in set(text):
#         result.append(ord(symbol))
#     return sorted(result, reverse = True)


# print(uni_list('Съешь ещё этих вкусных сладких булок'))

#-----------
# Задача №3
#-----------

# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode,
# а значением - целое число.
# Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


# def range_unicode(text: str) -> dict[str, int]:
#     first, second = map(int, text.split())
#     result = {}
#     for number in range(min(first, second), max(first, second) + 1):
#         result[chr(number)] = number    
#     return result


# print(range_unicode('42332 42551'))

#-----------
# Задача №4
#-----------

# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.


# def sort_list(my_list: list[int]):
#     count = 1
#     while count < len(my_list):
#         is_sorted = True
#         for i in range(len(my_list) - count):
#             if my_list[i] > my_list[i + 1]:
#                 is_sorted = False
#                 my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#         count += 1

        
# data_list = [8, 15, 42, 4, 23, 16, 500, 1, 3, 2, 999]

# sort_list(data_list)
# print(data_list)

# # C Использование флага
# def sort_list(my_list: list[int]):
#     not_sorted = True
#     while not_sorted:
#         not_sorted = False
#         for i in range(len(my_list) - 1):
#             if my_list[i] > my_list[i + 1]:
#                 my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#                 not_sorted = True
           
                
# data_list = [8, 15, 42, 4, 23, 16, 500, 1, 3, 2, 999]

# sort_list(data_list)
# print(data_list)

#-----------
# Задача №5
#-----------

# Функция принимает на вход три списка одинаковой длины:
# - имена str
# - вставка int
# - вставка  str с указанием процентов вида "10.25%""
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

# import decimal

# def list_bonus(name: list[str], best: list[int], reward: list[str])\
#       -> dict[str, decimal.Decimal]:
#     result = {}
#     for name, best, reward in zip(name, best, reward):
#         result[name] = best * decimal.Decimal(reward[:-1]) / 100
#     return result


# n = ['Rita', 'Ira', 'Luna']
# b = [20000, 10000, 30000]
# r = ['5.5%', '10.25%', '3.14%']

# print(list_bonus(n, b, r))

# Через range
# import decimal

# def list_bonus(name: list[str], best: list[int], rewards: list[str])\
#       -> dict[str, decimal.Decimal]:
#     result = {}
#     for i in range(len(name)):
#         result[name[i]] = best[i] * decimal.Decimal(rewards[i][:-1]) / 100
#     return result


# n = ['Rita', 'Ira', 'Luna']
# b = [20000, 10000, 30000]
# r = ['5.5%', '10.25%', '3.14%']

# print(list_bonus(n, b, r))

#-----------
# Задача №6
#-----------

# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


# def sum_number_index(my_list: list[int | float], i_1: int, i_2: int)\
#       -> int | float:
#     i_max = max(i_1, i_2)
#     i_max_plus_1 = i_max if i_max < len(my_list) else len(my_list)
#     i_min = min(i_1, i_2)
#     i_min_plus_1 = i_min if i_min >= 0 else 0
#     return sum(my_list[i_min_plus_1:i_max_plus_1])


# i_1 = 10
# i_2 = 2
# num = [4, 8, 15, 16, 23, 42]

# print(sum_number_index(num, i_1, i_2))

#-----------
# Задача №7
#-----------

# Функция получает на вход словать с названием компани
# в качестве ключа и списком с доходами и расходами (3-10 чисел)
# в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину,
# а если хотябы одна убыточная ложь.

# lambda and map
# def final_income(my_dict: dict[str, list[int | float]]) -> bool:
#     return all(map(lambda x: sum(x) > 0, my_dict.values()))


# data = {
#     'Horn': [42, -73, 12, 85, -15, 2],
#     'Hoves': [45, 25, -100, 22, 1],
#     'Tail': [-500, 123, 52, 45, 93]
# }

# print(final_income(data))

# for generator
# def final_income(my_dict: dict[str, list[int | float]]) -> bool:
#     return all(sum(cur_list) > 0 for cur_list in my_dict.values())


# data = {
#     'Horn': [42, -73, 12, 85, -15, 2],
#     'Hoves': [45, 25, -100, 22, 1],
#     'Tail': [-500, 123, 52, 45, 93]
# }

# print(final_income(data))

#-----------
# Задача №8
#-----------

# Создайте несколько переменных заканчивающихся и не оканчивающихся на "s",
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчиваюзихся на "s" (кроме переменной из одной буквы "s") на None.
# Значения не удаляются, а помещаются в одномёрнные переменные без "s" на конце.


def value_changer():
    globals_variables = globals()
    new_dict = {}
    for key, values in globals_variables.items():
        if key.endswith('s') and key != 's':
            new_dict[key[:-1]] = values
            globals_variables[key] = None
    for key, values in new_dict.items():
        globals_variables[key] = values


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

value_changer()
print(globals())
