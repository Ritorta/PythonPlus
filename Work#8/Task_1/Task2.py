# Решить задачи, которые не успели решить на семинаре, задача №2

# Напишите фукцию, которая в бесконечном цикле запрашивает имя, 
# личный индетификатор и уровень доступа (от 1 до 7)
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от увроня
# доступа.
# При перезапуске функции уже записанные в файл данные должны
# сохраняться.

#-----------
# Вариант №1 - id могу дублироваться если расположены в разных уровнях и могут перезаписывать имена в рамках своего уровня доступа.
#-----------

import json
from pathlib import Path

path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#8\\Task_1\\Result')


def set_users(file: Path) -> None:
    uids = set()

    if not file.is_file():
        data = {str(i): {} for i in range(1, 7 + 1)}
    else:
        with open(file, 'r', encoding='utf=8') as f_read:
            data = json.load(f_read)
        for value in data.values():
            uids.update(value.keys())
    
    while True:
        name = input('Enter the name: ')
        if not name:
            break
        id = input('Enter the id: ')
        lvl = input('Enter the level in 1 to 7: ')
        if ~ (id in uids and data[lvl].get(id) is None):
            data[lvl].update({id: name})
            with open(file, 'w', encoding='utf-8') as f_write:
                json.dump(data, f_write, indent=2, ensure_ascii=False)

if __name__ == '__main__':    
    set_users(Path(path / 'users.json'))

#-----------
# Вариант №2 - id уникальны и не могут повторяться, имена не перезаписываются.
#-----------

# import json
# import os

# path = 'C:/Users/Esdesu/Documents/Материалы по обучению/Обучение Ai/PythonPlus/Work#8/Task_1/Result'

# def set_users(file_path: str) -> None:
#     uids = set()
    
#     if not os.path.isfile(file_path):
#         data = {str(i): {} for i in range(1, 7 + 1)}
#     else:
#         with open(file_path, 'r', encoding='utf-8') as f_read:
#             data = json.load(f_read)
#         for value in data.values():
#             uids.update(value.keys())
    
#     while True:
#         name = input('Enter the name: ')
#         if not name:
#             break
#         id = input('Enter the id: ')
#         lvl = input('Enter the level in 1 to 7: ')
#         if id not in uids and data[lvl].get(id) is None:
#             data[lvl].update({id: name})
#             with open(file_path, 'w', encoding='utf-8') as f_write:
#                 json.dump(data, f_write, indent=2, ensure_ascii=False)
#                 uids.add(id)

# if __name__ == '__main__':
#     set_users(os.path.join(path, 'users.json'))
