# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и вехнию
# границу и количество попыток.
# Внутри генирируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.

from random import randint as rand


def guess(lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    num = rand(lower, upper)
    for nn in range(1, count + 1):
        answer = int(input(f'Trying: №{nn}, enter the number between {lower} in {upper}: '))
        if answer > num:
            print(f'You number > enimatic number')
        elif answer < num:
            print(f'You number < enimatic number')
        else:
            return True
    return False
    
if __name__ == '__main__':
    print(guess())
