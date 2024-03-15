# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

#-------------
# Вариант № 1 - Без задания с звёздочкой
#-------------

# camping_stuff = {'спички': 0.1, 'спальник': 2, 'топор': 1, 'косметичка': 0.5, 'нож': 0.3, 
#                  'фляга с водой': 0.8, 'еда': 5, 'походная посуда': 4,}

# MAX_CAPACITY = 5

# backpack = {}
# maximum_weight = 0

# for item, weight in camping_stuff.items():
#     if maximum_weight + weight <= MAX_CAPACITY:
#         backpack[item] = weight
#         maximum_weight += weight

# print(f'Backpack stuff: {backpack}\nWeight = {maximum_weight}')

#-------------
# Вариант № 2
#-------------

# camping_stuff = {'спички': 0.1, 'спальник': 2, 'топор': 1, 'косметичка': 0.5, 'нож': 0.3, 
#                  'фляга с водой': 0.8, 'еда': 5, 'походная посуда': 4,}

# MAX_CAPACITY = 5

# backpack = {}
# maximum_weight = 0

# for item, weight in camping_stuff.items():
#     if maximum_weight + weight <= MAX_CAPACITY:
#         backpack[item] = weight
#         maximum_weight += weight
#         print(f'Backpack stuff: {backpack}\nWeight = {maximum_weight}')

#-------------
# Вариант № 3
#-------------

import itertools

camping_stuff = {'спички': 0.1, 'спальник': 2, 'топор': 1, 'косметичка': 0.5, 'нож': 0.3, 
                 'фляга с водой': 0.8, 'еда': 5, 'походная посуда': 4,}

MAX_CAPACITY = 5

backpack = {}
maximum_weight = 0

for i in range(1, len(camping_stuff) + 1):
    for items in itertools.combinations(camping_stuff.items(), i):
        maximum_weight = sum(weight for item, weight in items)
        if maximum_weight <= MAX_CAPACITY:
            print(dict(items).keys(), f'\nWeight = {maximum_weight}')
