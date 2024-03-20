# 3. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

#-------------
# Вариант № 1
#-------------


# def argument_dict(**kwargs) -> dict[str]:
#     result = {}
#     for key, value in kwargs.items():
#         if isinstance(value, dict):
#             value = tuple(value.items())
#         if isinstance(value, list):
#             value = tuple(value)  # 
#         if hasattr(key, '__hash__'):
#             result[value] = key
#         else:
#             result[str(value)] = key
#     return result

# print(argument_dict(name = 'Rita', b = 'Pony', months = ['January', 'February', 'March'], courses = {'python' : 'ver 3.12', 'c#' : 'ver 2.5'}, c = [1, 2, 3], d = (4, 5), e = 3.14))

#-------------
# Вариант № 2
#-------------


def argument_dict(**kwargs) -> dict[str]:
    result = {}
    for key, value in kwargs.items():
        try:
            hash(key)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

print(argument_dict(name = 'Rita', b = 'Pony', months = ['January', 'February', 'March'], courses = {'python' : 'ver 3.12', 'c#' : 'ver 2.5'}, c = [1, 2, 3], d = (4, 5), e = 3.14))
