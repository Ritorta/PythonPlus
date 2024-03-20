# 4. Создайте функцию генератор чисел Фибоначчи

#-------------
# Вариант № 1
#-------------

a = 0
b = 1


def fib(a: int, b: int, num: int) -> int:
    for _ in range(num):
        yield a
        a, b = b, a + b


while True:
    try:
        num = int(input('Enter the number" '))
        print(list(fib(a, b, num)))
    except ValueError:
        print('Please, enter the number')
        continue 
    break

#-------------
# Вариант № 2
#-------------

# def fib():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         a, b = b, a + b


# fib_list = fib()

# print(f'1. {next(fib_list)}')
# print(f'2. {next(fib_list)}')
# print(f'3. {next(fib_list)}')
# print(f'4. {next(fib_list)}')
# print(f'5. {next(fib_list)}')
# print(f'6. {next(fib_list)}')
# print(f'7. {next(fib_list)}')
# print(f'8. {next(fib_list)}')
# print(f'9. {next(fib_list)}')
# print(f'10. {next(fib_list)}')
