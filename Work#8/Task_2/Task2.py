# 2. Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех 
# вложенных файлов и директорий.

# import json
# import csv
# import pickle
# import os


# def get_directory_size(directory):
#     total_size = 0
#     for dirpath, _, filenames in os.walk(directory):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#     return total_size


# def traverse_directory(directory):
#     data = []
#     for dirpath, dirnames, filenames in os.walk(directory):
#         current_dir_info = {
#             'name': dirpath,
#             'type': 'directory',
#             'size': get_directory_size(dirpath)
#         }
#         data.append(current_dir_info)

#         for file in filenames:
#             file_path = os.path.join(dirpath, file)
#             file_info = {
#                 'name': file_path,
#                 'type': 'file',
#                 'size': os.path.getsize(file_path),
#                 'parent_directory': dirpath
#             }
#             data.append(file_info)

#     return data


# directory = "path_to_your_directory"

# data = traverse_directory(directory)

# # Save as JSON
# with open('directory_info.json', 'w') as json_file:
#     json.dump(data, json_file, indent=2)

# # Save as CSV
# csv_columns = ['name', 'type', 'size', 'parent_directory']
# csv_filename = "directory_info.csv"
# with open(csv_filename, 'w') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# # Save as Pickle
# pickle_filename = "directory_info.pickle"
# with open(pickle_filename, 'wb') as pickle_file:
#     pickle.dump(data, pickle_file)


import json
import csv
import pickle
from pathlib import Path


def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    data = []
    for dirpath, dirnames, filenames in os.walk(directory):
        current_dir_info = {
            'name': dirpath,
            'type': 'directory',
            'size': get_directory_size(dirpath)
        }
        data.append(current_dir_info)

        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_info = {
                'name': file_path,
                'type': 'file',
                'size': os.path.getsize(file_path),
                'parent_directory': dirpath
            }
            data.append(file_info)

    return data


directory = "path_to_your_directory"

data = traverse_directory(directory)

with open('directory_info.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

csv_columns = ['name', 'type', 'size', 'parent_directory']
csv_filename = "directory_info.csv"
with open(csv_filename, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

pickle_filename = "directory_info.pickle"
with open(pickle_filename, 'wb') as pickle_file:
    pickle.dump(data, pickle_file)
