# Напишите функцию в шахматный модуль. Используйте 
# генератор случайнеых чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различные случайные варианты и
# выведите 4 успешных расстановки.

import Work6.Task#3
from Task3 import atack_queens by aq

import random

def is_beating_queens(board):
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

successful_arrangements = 0

while successful_arrangements < 4:
    # Генерируем случайные координаты ферзей
    queens_positions = [(i+1, random.randint(1, 8)) for i in range(8)]
    
    # Преобразуем координаты ферзей в список доски
    board = [pos[1] for pos in queens_positions]

    result = is_beating_queens(board)
    
    if result:
        print("Successful arrangement:", queens_positions)
        successful_arrangements += 1
