# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8х8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа 
# получает на вхож восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют
# друг друга верните истину, а если бьют - ложь.



# def queens(board, row=0):
#     if row == len(board):
#         return True
#     for col in range(len(board)):
#         if not under_attack(board, row, col):
#             board[row][col] = 1
#             if queens(board, row+1):
#                 return True
#             board[row][col] = 0
        
#     return False


# def under_attack(board, row, col):
#     for x in range(row):
#         if board[x][col]:
#             return True
#     y = row
#     for x in range(col):
#         if board[y][x]:
#             return True
#     y = row
#     x = col
#     while x >= 0 and y >= 0:
#         if board[y][x]:
#             return True
#         x -= 1
#         y -= 1
#     y = row
#     x = col
#     while y >= 0 and x < len(board):
#         if board[y][x]:
#             return True
#         y -= 1
#         x += 1

#     return False

# board = [[0]*8 for i in range(8)]

# queens(board)

# for row in board:
#     print(row)


# def check_queens(queens):
#     for i in range(len(queens)):
#         for j in range(i + 1, len(queens)):
#             if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
#                 return False
#     return True

# # Ввод координат ферзей
# queens = []
# for _ in range(8):
#     queen = tuple(map(int, input().split()))
#     queens.append(queen)

# result = check_queens(queens)

# if result:
#     print("Ферзи не бьют друг друга.")
# else:
#     print("Ферзи бьют друг друга.")


#     def is_beating_queens(queens):
#     for i in range(len(queens)):
#         for j in range(i+1, len(queens)):
#             if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
#                 return False
#     return True

# queens = []
# for _ in range(8):
#     queens.append(tuple(map(int, input().split())))

# result = is_beating_queens(queens)
# print(result)

# def queens(board, row=0):
#     if row == len(board):
#         return True
#     for col in range(len(board)):
#         if not under_attack(board, row, col):
#             board[row][col] = 1
#             if queens(board, row+1):
#                 return True
#             board[row][col] = 0
        
#     return False


# def under_attack(board, row, col):
#     for x in range(row):
#         if board[x][col]:
#             return True
#     y = row
#     x = col
#     while y >= 0 and x >= 0:
#         if board[y][x]:
#             return True
#         y -= 1
#         x -= 1
#     y = row
#     x = col
#     while y >= 0 and x < len(board):
#         if board[y][x]:
#             return True
#         y -= 1
#         x += 1

#     return False

# board = [[0]*8 for i in range(8)]

# queens(board)

# for row in board:
#     print(row)

def is_beating_queens(board):
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

# Пример расстановки ферзей на доске
queens_positions = [(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1)]

# Преобразуем координаты ферзей в список доски
board = [pos[1] for pos in queens_positions]

result = is_beating_queens(board)
print(result)


