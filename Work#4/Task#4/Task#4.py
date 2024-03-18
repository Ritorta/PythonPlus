# 4. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е
# Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богаство 10% перед каждой операцией, 
# даже ошибочной
# Любое действие выводит сумму денег

import decimal

decimal.getcontext().prec = 10

CMD_DEPOSIT = 'p'
CMD_WITHDRAW = 'c'
CMD_EXIT = 'e'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = decimal.Decimal(50)
MAX_REMOVAL = decimal.Decimal(600)
MIN_REMOVAL = decimal.Decimal(30)
COUNT_OPEN = decimal.Decimal(3)

account_balance = decimal.Decimal(0)
amount = decimal.Decimal(0)
count = 0
list_operations = []


def add_money():
    global account_balance
    global amount
    global count
    global list_operations
    cheack_ruch()
    bonus_prochent()
    while True:
        amount = int(input(f'Enter sum, equals {MULTIPLICITY}: '))
        if amount % 50 == 0:
            break
    account_balance += amount        
    count += 1
    list_operations.append((f'Account replenishment - {amount}'))
    print(f'Credit card replenishment {amount},\n'
            f'Total left on the credit card {account_balance} y.e')
    return 0


def take_money():
    global account_balance
    global amount
    global count
    global list_operations
    cheack_ruch()
    bonus_prochent()
    while True:
        amount = int(input(f'Enter sum, equals {MULTIPLICITY}: '))
        if amount % 50 == 0:
            break
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL 
                    else MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
    
    if account_balance >= amount + withdraw_tax:
        count += 1
        account_balance -= (amount + withdraw_tax)
        list_operations.append((f'Account withdrawal - {amount}'))
        print(f'Credit card withdrawal {amount} y.e\n'
                f'commission for withdrawal {withdraw_tax} y.e\n'
                f'There is still money left on the credit card {account_balance} y.e')
    else:
        print(f'Insufficient funds on the credit card\n'
                f'The requested amount {amount + withdraw_tax} y.e, the commission was {withdraw_tax}%\n'
                f'Balance credit card {account_balance} y.e')
    return 0


def cheack_ruch():
    global account_balance
    if account_balance > RICHNESS_SUM:
            percent = account_balance * RICHNESS_TAX
            account_balance -= percent
            print(f'Wealth tax withheld {RICHNESS_TAX}% in size {percent} y.e \n'
                  f'Total left on the credit card {account_balance} y.e')
    return 0


def bonus_prochent():
    global account_balance
    global count
    if count and count % COUNT_OPEN == 0:
        bonus_percent = account_balance * ADD_PERCENT
        account_balance += bonus_percent
        print(f'About credited {ADD_PERCENT}% for {bonus_percent} y.e\n'
              f'Balance credit card {account_balance} y.e')
    return 0


def show_list_operations():
    print(f'List operations: {list_operations}')
    return 0


def main():
    while True:
        num = int(input('Bancomat menu:\n'
            '1 - Add cash on a bank card\n'
            '2 - Take off cash from a bank card\n'
            '3 - Exit\n'
            'Chose your operation: '))
        
        if num == 1:
            add_money()
        elif num == 2:
            take_money()
        elif num == 3:
            print(f'Please, take your credit cart, your balance {account_balance} y.e, Good bye!')
            return exit(0)
        elif num == 4:
            show_list_operations() 
    
main()
