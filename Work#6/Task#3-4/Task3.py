# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8х8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа 
# получает на вхож восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют
# друг друга верните истину, а если бьют - ложь.

#-----------
# Вариант №1
#-----------


# def atack_queens(board: int) -> bool:
#     for i in range(len(board)):
#         for j in range(i + 1, len(board)):
#             if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
#                 return False
#     return True


# if __name__ == '__main__':

#     queens_positions = [(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1)]

#     board = [pos[1] for pos in queens_positions]

#     result = atack_queens(board)
#     print(result)

#-----------
# Вариант №2
#-----------


def check_attack(board: int, row: int, column: int) -> bool:

    n = len(board)

    for i in range(n):
        if board[i][column] == 1 or board[row][i] == 1:
            return True
        
    for i in range(1, n):
        if row - i >= 0 and column - i >= 0:
            if board[row - i][column - i] == 1:
                return True
        if row - i >= 0 and column + i < n:
            if board[row - i][column + i] == 1:
                return True
        if row + i < n and column - i >= 0:
            if board[row + i][column - i] == 1:
                return True
        if row + i < n and column + i < n:
            if board[row + i][column + i] == 1:
                return True
    return False


def place_queens(board: int, row: int = 0) -> bool:

    n = len(board)

    if row == n:
        return True, board
    for column in range(n):
        if not check_attack(board, row, column):
            board[row][column] = 1
            success, final_board = place_queens(board, row + 1)
            if success:
                return True, final_board
            board[row][column] = 0
    return False, board


def attack_queens(board: int) -> bool:
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True


def print_board(board: list) -> list:
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


if __name__ == '__main__':

    queens_positions = [(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1)]

    board = [[0] * 8 for _ in range(8)]
    for row, col in queens_positions:
        board[row - 1][col - 1] = 1

    success, final_board = place_queens(board)
    result = attack_queens([row.index(1) + 1 for row in final_board])
    print_board(board)

    if result:
        print(f'Successful, queens dont beat other = {result}')
    else:
        print(f'Fail, queens beat each other = {result}')
