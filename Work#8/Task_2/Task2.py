# 2. Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех 
# вложенных файлов и директорий.

import os
import json
import csv
import pickle
from pathlib import Path

path = Path('C:\\Users\\Esdesu\\Documents\\Материалы по обучению\\Обучение Ai\\PythonPlus\\Work#8\\Task_1\\Result')


def get_size(fille: Path) -> list:
    total = 0
    for dirpath, dirnames, filenames in os.walk(fille):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total


def directory_walker(fille: Path) -> list:
    results = []
    for dirpath, dirnames, files in os.walk(fille):
        for name in files:
            full_path = os.path.join(dirpath, name)
            results.append({"parent_directory": dirpath, 
                            "is_file": True,
                            "name": name,
                            "size_in_bytes": os.path.getsize(full_path)})

        for name in dirnames:
            full_path = os.path.join(dirpath, name)
            results.append({"parent_directory": dirpath, 
                            "is_file": False,
                            "name": name,
                            "size_in_bytes": get_size(full_path)})
    return results


def save_to_json(data: list) -> None:
    with open(path / 'directory_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)


def save_to_csv(data: list) -> None:
    csv_columns = ['name', 'is_file', 'size_in_bytes', 'parent_directory']
    csv_filename = "directory_info.csv"
    with open(path / csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns, dialect='excel-tab')
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data: list) -> None:
    pickle_filename = "directory_info.pickle"
    with open(path / pickle_filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


if  __name__ == '__main__':
    data = directory_walker(path)
    save_to_json(data)
    save_to_csv(data)
    save_to_pickle(data)
