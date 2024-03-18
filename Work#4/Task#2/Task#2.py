# 2. Напишите функцию для транспонирования матрицы

#-------------
# Вариант № 1 - С использованием вложеного цикла
#-------------

# matrix = [[1, 10, 100], [2, 20, 200], [3, 30, 300]]

# result = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):    
#         result[j][i] = matrix[i][j]

# print(matrix)
# print(result)

#-------------
# Вариант № 2 - С использованием Numpy transpose() 
#-------------

# import numpy as np

# matrix = np.array([[1, 10, 100], [2, 20, 200], [3, 30, 300]])

# result = matrix.transpose()

# print(matrix)
# print(result)

#-------------
# Вариант № 3 - С использованием генератора списка
#-------------

# matrix = [[1, 10, 100], [2, 20, 200], [3, 30, 300]]

# result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# print(matrix)
# print(result)

#-------------
# Вариант № 4 - С использованием pymatrix
#-------------

# import pymatrix

# matrix = pymatrix.matrix([[1, 10, 100], [2, 20, 200], [3, 30, 300]])

# result = matrix.trans()

# print(matrix)
# print(result)

#-------------
# Вариант № 5 - С использованием metod zip
#-------------

matrix = [[1, 10, 100], [2, 20, 200], [3, 30, 300]]

matrix_zip = zip(*matrix)

result = [list(row) for row in matrix_zip]

print(matrix)
print(result)