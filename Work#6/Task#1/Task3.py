# Улучшаем задачу 2.
# Добавьте возможность запуска функции "угадайки" из модуля 
# в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры 
# вызова функции.
# Для преобразования строковых аргументов командной строки
# в числовые параметры используйте генераторное выражение.

from sys import argv as av
from Task2 import *
    
if __name__ == '__main__':
    print(av)