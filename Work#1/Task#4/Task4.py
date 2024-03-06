# Урок 1. Основы Python

# Условие
# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


#------------
# Вариант №1
#------------

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
RANDOM_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
COUNT_TRY = 10
COUNT_CURENT = 0

while COUNT_CURENT < COUNT_TRY:
    COUNT_CURENT += 1
    USER_NUMBER = int(input('Enter the pass number, you have ten try: ')) 
    if RANDOM_NUMBER > USER_NUMBER:
        print(f'You number is small, try № {COUNT_CURENT}')
        continue
    elif RANDOM_NUMBER < USER_NUMBER:
        print(f'You number is bigger, try № {COUNT_CURENT}')
        continue
    else:
        print(f'Congratulations, you number pass correct = {RANDOM_NUMBER}')
        break

else:
    print('Sorry but your number pass is incorrect, try again')

#------------
# Вариант №2 - PC отгадывает абсолютно рандомно
#------------

# from random import randint

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# RANDOM_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
# COUNT_TRY = 10
# COUNT_CURENT = 0

# while COUNT_CURENT < COUNT_TRY:
#     COUNT_CURENT += 1
#     PC_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
#     if RANDOM_NUMBER > PC_NUMBER:
#         print(f'PC number is small, try № {COUNT_CURENT}')
#         continue
#     elif RANDOM_NUMBER < PC_NUMBER:
#         print(f'PC number is bigger, try № {COUNT_CURENT}')
#         continue
#     else:
#         print(f'Congratulations, you number pass correct = {RANDOM_NUMBER}')
#         break

# else:
#     print('Sorry but PC number pass is incorrect, try again')

#------------
# Вариант №3 - PC имеет 90% на разгадку
#------------

# from random import randint

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# RANDOM_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
# COUNT_TRY = 10
# COUNT_CURENT = 0

# min_number = LOWER_LIMIT
# max_number = UPPER_LIMIT

# def make_guess():
#     return (min_number + max_number) // 2

# while COUNT_CURENT < COUNT_TRY:
#     COUNT_CURENT += 1
#     PC_NUMBER = make_guess()
    
#     if RANDOM_NUMBER > PC_NUMBER:
#         print(f'PC number is small, try № {COUNT_CURENT} - {RANDOM_NUMBER} - {PC_NUMBER}')
#         min_number = PC_NUMBER + 1
#     elif RANDOM_NUMBER < PC_NUMBER:
#         print(f'PC number is bigger, try № {COUNT_CURENT} - {RANDOM_NUMBER} - {PC_NUMBER}')
#         max_number = PC_NUMBER - 1
#     else:
#         print(f'Congratulations, you number pass correct = {RANDOM_NUMBER}')
#         break

# else:
#     print('Sorry but PC number pass is incorrect, try again')
