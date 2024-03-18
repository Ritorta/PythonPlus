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

RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = decimal.Decimal(50)
MAX_REMOVAL = decimal.Decimal(600)
MIN_REMOVAL = decimal.Decimal(30)
COUNT_OPEN = decimal.Decimal(3)
ACCOUNT_BALANCE = decimal.Decimal(0)
AMOUNT = decimal.Decimal(0)
COUNT = 0

list_operations = []

# The function of adding money to a bank account
def add_money():
    global ACCOUNT_BALANCE
    global AMOUNT
    global COUNT
    global list_operations
    cheack_ruch()
    bonus_prochent()
    while True:
        AMOUNT = int(input(f'Enter sum, equals {MULTIPLICITY}: '))
        if AMOUNT % 50 == 0:
            break
    ACCOUNT_BALANCE += AMOUNT        
    COUNT += 1
    list_operations.append((f'Account replenishment - {AMOUNT}'))
    print(f'Credit card replenishment {AMOUNT},\n'
            f'Total left on the credit card {ACCOUNT_BALANCE} y.e')
    return 0

# The function of withdrawing money from a bank account
def take_money():
    global ACCOUNT_BALANCE
    global AMOUNT
    global COUNT
    global list_operations
    cheack_ruch()
    bonus_prochent()
    while True:
        AMOUNT = int(input(f'Enter sum, equals {MULTIPLICITY}: '))
        if AMOUNT % 50 == 0:
            break
    withdraw_tax = AMOUNT * WITHDRAW_PERCENT
    withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL 
                    else MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
    
    if ACCOUNT_BALANCE >= AMOUNT + withdraw_tax:
        COUNT += 1
        ACCOUNT_BALANCE -= (AMOUNT + withdraw_tax)
        list_operations.append((f'Account withdrawal - {AMOUNT}'))
        print(f'Credit card withdrawal {AMOUNT} y.e\n'
                f'commission for withdrawal {withdraw_tax} y.e\n'
                f'There is still money left on the credit card {ACCOUNT_BALANCE} y.e')
    else:
        print(f'Insufficient funds on the credit card\n'
                f'The requested amount {AMOUNT + withdraw_tax} y.e, the commission was {withdraw_tax}%\n'
                f'Balance credit card {ACCOUNT_BALANCE} y.e')
    return 0

# The function of checking for wealth, for tax calculation
def cheack_ruch():
    global ACCOUNT_BALANCE
    if ACCOUNT_BALANCE > RICHNESS_SUM:
            percent = ACCOUNT_BALANCE * RICHNESS_TAX
            ACCOUNT_BALANCE -= percent
            print(f'Wealth tax withheld {RICHNESS_TAX}% in size {percent} y.e \n'
                  f'Total left on the credit card {ACCOUNT_BALANCE} y.e')
    return 0

# The function of calculating a percentage of the number of transactions
def bonus_prochent():
    global ACCOUNT_BALANCE
    global COUNT
    if COUNT and COUNT % COUNT_OPEN == 0:
        bonus_percent = ACCOUNT_BALANCE * ADD_PERCENT
        ACCOUNT_BALANCE += bonus_percent
        print(f'About credited {ADD_PERCENT}% for {bonus_percent} y.e\n'
              f'Balance credit card {ACCOUNT_BALANCE} y.e')
    return 0

# The function shows a list of operations
def show_list_operations():
    if list_operations:
        for index, operation in enumerate(list_operations, start = 1):
            print(f'Operation №: {index}. {operation} y.e')
    else:
        print('No transactions were made with the account')
    return 0

# The function menu
def main():
    while True:
        try:
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
                print(f'Please, take your credit cart, your balance {ACCOUNT_BALANCE} y.e, Good bye!')
                return exit(0)
            elif num == 9:
                show_list_operations()
            else:
                print('Please enter the correct number menu')
        except ValueError:
            print('Please enter the menu number')
            continue 
    
main()
