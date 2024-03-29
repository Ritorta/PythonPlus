# Решить задачи, которые не успели решить на семинаре, задача №3

# Напишите функцию, которая созраняет созданный в прошлом задании
# файл в формате CSV.

import csv
import json
from pathlib import Path

path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#8\\Task_1\\Result')


def json_to_csv(file: Path) -> None:
    with open(path / file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)

    list_rows = []
    for level, id_name_dict in data.items():
        for id, name in id_name_dict.items():
            list_rows.append({'level':int(level), 'id':id, 'name':name})
    
    with open(path / f'{file.stem}.csv', 'w', newline='', encoding='utf=8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(list_rows)


if __name__ == '__main__':
    json_to_csv(Path('users.json'))
    