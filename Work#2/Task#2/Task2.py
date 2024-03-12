# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

HEX = 16
hexD = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 
        'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',}

while True:
    try:
        num = int(input('Enter the number: '))

        res_str: str = ''
        temp_num = num

        while temp_num > 0:
            result = temp_num % HEX
            hex_dict = hexD[result]
            res_str = hex_dict + res_str
            res = '0x' + res_str
            temp_num = temp_num // HEX

        print(f'{type(res) = }, \n{res = }, \n{hex(num) = }')
        break
    except ValueError:
        print('Error, please enter the number.')
        continue

