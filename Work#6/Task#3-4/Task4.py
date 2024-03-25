# Напишите функцию в шахматный модуль. Используйте 
# генератор случайнеых чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различные случайные варианты и
# выведите 4 успешных расстановки.

#-----------
# Вариант №1
#-----------

# from Task3 import atack_queens as aq

# import random

# successful_arrangements = 0

# while successful_arrangements < 4:
    
#     queens_positions = [(i + 1, random.randint(1, 8)) for i in range(8)]
    
#     board = [pos[1] for pos in queens_positions]

#     result = aq(board)
    
#     if result:
#         print("Successful arrangement:", queens_positions)
#         successful_arrangements += 1

#-----------
# Вариант №2
#-----------
        
from Task3 import atack_queens as aq
#from Task3 import print_board as pb

import random

successful_arrangements = 0

while successful_arrangements < 4:
    queens_positions = [(i + 1, random.randint(1, 8)) for i in range(8)]

    board = [pos[1] for pos in queens_positions]

    result = aq(board)

    if result:
        print("Successful arrangement:", queens_positions)
        result_list = queens_positions
        successful_arrangements += 1
        
        
