# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions

f1 = fractions.Fraction(5, 5)
f2 = fractions.Fraction(5, 5)

print(f'Cheak Sum Fraction: {f1 + f2}')
print(f'Cheak Mulyplay Fraction: {f1 * f2}')

from math import gcd

while True:
    try:
        num1, den1 = map(int, input("Enter first fraction (use to split /): ").split('/'))
        num2, den2 = map(int, input("Enter second fraction (use to split /) ").split('/'))

        if den1 == den2:
            fraction_sum_num = num1 + num2
            fraction_sum_den = den1
            print(f'Fraction = {fraction_sum_num}/{fraction_sum_den}')
            value_gcd = gcd(fraction_sum_num, fraction_sum_den)
            sump_num = fraction_sum_num // value_gcd
            sump_den = fraction_sum_den // value_gcd
            if sump_num > sump_den:
                print(f'Sumple Fraction = {sump_num}')
            else:
                print(f'Sumple Fraction = {sump_num}/{sump_den}')
            
        else:
            fraction_sum_num = (num1 * den2) + (num2 * den1)
            fraction_sum_den = den1 * den2
            print(f'Fraction = {fraction_sum_num}/{fraction_sum_den}')
            value_gcd = gcd(fraction_sum_num, fraction_sum_den)
            sumple_sum_num = fraction_sum_num // value_gcd
            sumple_sum_den = fraction_sum_den // value_gcd
            if sumple_sum_num > sumple_sum_den:
                print(f'Sumple Fraction = {sumple_sum_num}')
            else:
                print(f'Sumple Fraction = {sumple_sum_num}/{sumple_sum_den}')
            
        fraction_mult_num = num1 * num2
        fraction_mult_del = den1 * den2
        print(f'Multyplay Fraction = {fraction_mult_num}/{fraction_mult_del}')
        value_gcd = gcd(fraction_mult_num, fraction_mult_del)
        sumple_multp_num = fraction_mult_num // value_gcd
        sumple_multp_del = fraction_mult_del // value_gcd
        if sumple_multp_num == sumple_multp_del:
            print(f'Sumple Multyplay Fraction = {sumple_multp_num}')
            break
        else:
            print(f'Sumple Multyplay Fraction = {sumple_multp_num}/{sumple_multp_del}')
            break

    except (ValueError, ZeroDivisionError) as e:
        print(f'Error {e}, please try again, enter the correct number or split "/" your faction.')
        continue


