3. # Напишите однострочный генератор словаря, 
# который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии 
# в качестве значения. Сумма рассчитывается как ставка умноженная на 
# процент премии 

string = ['Rita', 'Ira', "Luna"]
integer = [15000, 20000, 25000]
percent = ['1.45%', '5.85%', '10.25%']

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(string, integer, percent)})

result_dict = {name: rate * (1 + float(bonus.strip('%')) / 100) for name, rate, bonus in zip(string, integer, percent)}
print(result_dict)

result_dict = {string[i]: integer[i] + integer[i] * float(percent[i].strip('%')) / 100 for i in range(len(string))}
print(result_dict)
