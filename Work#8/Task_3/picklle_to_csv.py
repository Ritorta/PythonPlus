# Решить задачи, которые не успели решить на семинаре, задача №6

# Напишите функцию, которая преобразует pickle файл хранящий
# список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из
# задачи 4-того семинара.
# Функция должна извлекать ключи словаря для заголовков столбца
# из преданного файла.

#-----------
# Вариант №1
#-----------

import pickle
import csv
from pathlib import Path

__all__ = ['pickl_to_csv']

path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#8\\Task_1\\Result')


def pickl_to_csv(picl_file: Path) -> None:
    with (open(path / picl_file, 'rb') as f_read,
        open(path / f'{picl_file.stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = pickle.load(f_read)
        headers_list = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=headers_list,\
                                   dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    pickl_to_csv(Path('new_users.pickle'))

#-----------
# Вариант №2
#-----------

# import pickle
# import csv
# from pathlib import Path

# path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#8\\Task_1\\Result\\new_users.pickle')


# def pickle_to_csv(picl_file: Path) -> None:
#     with open(picl_file, 'rb') as f_read:
#         data = pickle.load(f_read)

#     csv_file = picl_file.with_suffix('.csv')
#     headers_list = list(data[0].keys())

#     with open(csv_file, 'w', newline='', encoding='utf-8') as f_write:
#         csv_writer = csv.DictWriter(f_write, fieldnames=headers_list, dialect='excel')
#         csv_writer.writeheader()
#         for row in data:
#             csv_writer.writerow(row)

# if __name__ == '__main__':
#     pickle_to_csv(path)
