# Напишите функцию в шахматный модуль. Используйте 
# генератор случайнеых чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различные случайные варианты и
# выведите 4 успешных расстановки.

#-----------
# Вариант №1
#-----------

# from Task3 import atack_queens as aq

# import random


# def random_cordinat_queens():
    
#     count = 0
#     result = []

#     while count < 4:
        
#         queens_positions = [(i + 1, random.randint(1, 8)) for i in range(8)]
        
#         board = [pos[1] for pos in queens_positions]
#         cheak_board = aq(board)
        
#         if cheak_board:
#             result.append(queens_positions)
#             count += 1
            
#     return result


# if __name__ == '__main__':
#     result = random_cordinat_queens()
#     for nn, value in enumerate(result, start=1):
#         print(f'Successful arrangement № {nn}: {value}')

#-----------
# Вариант №2
#-----------

from Task3 import attack_queens as aq
from Task3 import print_board as pb

import random


def random_coordinate_queens():
    
    count = 0
    result = []

    while count < 4:
        
        queens_positions = [(i + 1, random.randint(1, 8)) for i in range(8)]
        
        board = [pos[1] for pos in queens_positions]
        check_board = aq(board)
        
        if check_board:
            result.append(queens_positions)
            count += 1
            
    return result


if __name__ == '__main__':
    result = random_coordinate_queens()
    
    for nn, value in enumerate(result, start=1):
        board = [[0]*8 for _ in range(8)]
        for row, col in value:
            board[row - 1][col - 1] = 1
        pb(board)
        print(f'Successful arrangement № {nn}: {value}')
        