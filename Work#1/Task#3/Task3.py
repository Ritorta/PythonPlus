# Урок 1. Основы Python

# Условие
# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

CHEAK_NUM = '1234567890'
MIN_NUMBER = 0
MAX_NUMBER = 100000

num = input('Enter the number: ')
if any(i not in CHEAK_NUM for i in num):
    print('Error, please enter the number')
else:
    num = int(num)
    if num < MIN_NUMBER or num > MAX_NUMBER:
        print('Error, please enter the number in 1 for 100 000')
    else:    
        if num == 0 or num == 1:
            print('0 and 1 not simpel and multyplay numbers')
        else:    
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    print('The multiplay number')
                    break
            else:
                print('The simpel number')

