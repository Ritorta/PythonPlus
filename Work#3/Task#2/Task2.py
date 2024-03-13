# 2. Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

#-------------
# Вариант № 1
#-------------

# dublecate_list = [42, 1, 73, 5, 42, 42, 1, 2, 2, 5, 5, 2, 1, 2, 3, 7, 1, 73, 42]
# result_list = []

# for i in dublecate_list:
#     if i not in result_list:
#         result_list.append(i)

# print(f'Dublicate list = {dublecate_list}\nResult list = {result_list}')

#-------------
# Вариант № 2
#-------------

# dublecate_list = [42, 1, 73, 5, 42, 42, 1, 2, 2, 5, 5, 2, 1, 2, 3, 7, 1, 73, 42]
# result_list = list(set(dublecate_list))

# print(f'Dublicate list = {dublecate_list}\nResult list = {result_list}')

#-------------
# Вариант № 3
#-------------

dublecate_list = [42, 1, 73, 5, 42, 42, 1, 2, 2, 5, 5, 2, 1, 2, 3, 7, 1, 73, 42]
result_list = list(dict.fromkeys(dublecate_list))

print(f'Dublicate list = {dublecate_list}\nResult list = {result_list}')
