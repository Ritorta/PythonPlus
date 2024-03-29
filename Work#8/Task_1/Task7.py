# Решить задачи, которые не успели решить на семинаре, задача №6

# Прочитайте созданный в прошлом задании csv файл 
# без использования csv.DictReader
# Распечатайте его как pickle строку.

import pickle
import csv
from pathlib import Path

path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#8\\Task_1\\Result')


def csv_to_pickle(file: Path) -> None:
    
    pickle_list = []

    with open(path / file, 'r', newline='', encoding='utf-8') as f_read:
        csv_file = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            if i == 0:
                pickle_keys = line
            else:
                picle_dict = {key: value for key, value in zip(pickle_keys, line)}
                pickle_list.append(picle_dict)
    print(pickle.dumps(pickle_list))

if __name__ == '__main__':
    csv_to_pickle(Path('new_users.csv'))
