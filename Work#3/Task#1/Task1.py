# 1. Решить задачи, которые не успели решить на семинаре.

#-----------
# Задача №1
#-----------

# Вручную создайте список с целыми числамиЮ которые повторяются. 
# Получите новый спиисок, который сожержит уникальные (без повтора)
# элементы исходного списка.
# Подготовьте два решения, короткое и длинное которое не использует другие колекции помимо списков.

# # First

# my_list = [42, 73, 5, 42, 42, 2, 2, 5, 5, 2, 2, 3, 7, 73, 42]
# new_list = list(set(my_list))

# print(new_list)

# # Second

# my_list = [42, 73, 5, 42, 42, 2, 2, 5, 5, 2, 2, 3, 7, 73, 42]
# new_list = []

# for num in my_list:
#     if num not in new_list:
#         new_list.append(num)

# print(new_list)

#-----------
# Задача №2
#-----------

# Пользователь вводит данные. Сделать проверку данных и преобразуйте, 
# если возможно в один из вариантов:

# - Целое положительное число
# - Вещественное положительное или отрицательное число
# - строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква.
# - Строку в верхнем регистре в остальных случаях

# data = input('Enter the data: ')
# result = ''

# if data.isdigit():
#     result = int(data)
# elif data.count('.') == 1 and data.count('-') < 2 \
#       and data[1:].count('-') == 0 and data.replace('.', '').replace('-', ''):
#     result = float(data)
# elif not data.islower():
#     result = data.lower()
# else:
#     result = data.upper()

# print([result])

#-----------
# Задача №3
#-----------
 
# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ - тип элемента,
# значение - список элементов данного типа.

# data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
# my_dict = {}

# for item in data:
#     key = my_dict.setdefault(type(item), [])
#     key.append(item)
# print(my_dict)

#-----------
# Задача №4
#-----------

# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

# my_list = [42, 73, 5, 1, 42, 42, 2, 1, 2, 5, 3, 7, 1, 73, 42]
# COUNT = 2

# for item in set(my_list):
#     if my_list.count(item) == COUNT:
#         for _ in range(COUNT):
#             my_list.remove(item)

# print(my_list)

#-----------
# Задача №5
#-----------

# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами, нечётных элементов исходного списка.
# Нумерация должна начинатся с единицы.

# my_list = [42, 73, 5, 1, 42, 42, 2, 1, 2, 5, 3, 7, 1, 73, 42]
# new_list = []

# for n, item in enumerate(my_list, 1):
#     if item % 2 != 0:
#         new_list.append((n, item))

# print(f'{my_list}\n {new_list}')

#-----------
# Задача №6
#-----------

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# - Строки нумеруются начиная с единицы.
# - Слова выводятся отсортированными согласно кодировки Unicode.
# - Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки.

# data = sorted(input('Enter the string: ').split())

# max_len = 0

# for item in data:
#     if len(item) > max_len:
#         max_len = len(item)

# for n, word in enumerate(data, 1):
#     print(f'{n}.  {word:>{max_len}}')

#-----------
# Задача №7
#-----------

# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке
# без использования метода count и с ним.
# Результат сохраните в словаре, где ключ - символ,
# а значение - частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или несовпадают в ваших решениях.

# data = input('Enter the string: ')


# my_dict_count = {}

# for char in set(data):
#     my_dict_count[char] = data.count(char)
# print(my_dict_count)

# my_dict_dont_count = {}

# for char in data:
#     if char not in my_dict_dont_count:
#         my_dict_dont_count[char] = 1
#     else:
#         my_dict_dont_count[char] += 1

# print(my_dict_dont_count)

# my_dict_get = {}

# for char in data:
#     my_dict_get[char] = my_dict_get.get(char, 0) + 1

# print(my_dict_get)

#-----------
# Задача №8
#-----------

# Три друга вщяли вещи в поход. Сформируйте словарь, 
# где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того,
# у кого данная вещь отсуствует
# Для решения используйте операции с множествами. Код должен 
# расшираться на любое большие количество друзей.

hike = { 
    'Aaz' : ("спички", "спальник", "дрова", "топор"),
    'Skeeve' : ("спальник", "спички", "вода", "еда"),
    'Tananda' : ("вода", "спички", "косметичка", "топор"),
}

all_things = set()
for things in hike.values():
    # for thing in things:
    #     all_things.add(things)
    all_things.update(things)

print(f'List all things: {all_things}')

unique_things = {}

for master_friend, master_things in hike.items():
    for slave_friend, slave_things in hike.items():
        if master_friend != slave_friend:
            if master_friend not in unique_things:
                unique_things[master_friend] = set(master_things) - set(slave_things)
            else:
                unique_things[master_friend] -= set(slave_things)

print(f'List unique things: {unique_things}')

doublelicate_things = set(all_things)

for things in unique_things.values():
    doublelicate_things -= things

print(f'List duable things: {doublelicate_things}')

for friend, things in hike.items():
    print(f'{friend} dont things {doublelicate_things - set(things)}')
   # print(f' Second variation: {friend} dont things {(set(things) ^ doublelicate_things) - set(unique_things[friend])}')
