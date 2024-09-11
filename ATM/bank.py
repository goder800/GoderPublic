from userAccaunt import account
from rates import rates
import sys
import os
def menu():
    os.system('cls')
    print('Current pairs:')
    print('  RUB / USD')
    print('  RUB / EUR')
    print('  USD / EUR')
    print('  USD / USDT')
    print('  USD / BTC')
    print('(MENU)Choose a command:')
    print('  1 - Check balance')
    print('  2 - Check bank balance')
    print('  3 - Trade')
    print('  4 - Back')
    print('  5 - Exit')
'''
def check_balance(accaunt):
    while True:
        print_balance(accaunt)
        print('  5 - Back')
        print('  6 - Exit')
        check_option = 0
        try:
            check_option = int(input())
        except:
            print('invalid option')
        if check_option==5:
           menu()
        elif check_option==6:
            break
        else: check_option=0'''

def trade_window():
    while True:
        print('Choose a command:')
        print('  1 - Check balance')
        print('  2 - Check bank balance')
        print('  3 - Check exchange rates')
        print('  4 - Choose currency')
        print('  5 - Back')
        print('  6 - Exit')
        trade_window_option=0
        try:
            trade_window_option= int(input())
        except:
            print('invalid option')
        os.system('cls')
        if trade_window_option==1:
            print_balance(user)
        elif trade_window_option==2:
            print_balance(atm)
        elif trade_window_option==3:
            rate.print_rates()
        elif trade_window_option==4:
            trade(choose_currency())
        elif trade_window_option==5:
            menu()
            break
        elif trade_window_option==6:
            sys.exit()
        else: trade_window_option=0
def choose_currency():
    while True:
        print('Choose a command:')
        print('  1 - RUB / USD')
        print('  2 - RUB / EUR')
        print('  3 - USD / EUR')
        print('  4 - USD / USDT')
        print('  5 - USD / BTC')
        print('  6 - Back')
        print('  7 - Exit')
        choose_currency_option=0
        while True:
            try:
                choose_currency_option= int(input())
            except:
                print('invalid option')
            os.system('cls')
            if 0<choose_currency_option<6:
                return choose_currency_option
            elif choose_currency_option==6:
                trade_window()
            elif choose_currency_option==7:
                sys.exit()
            else: choose_currency_option=0
def trade(currency):
        exchange_rate=rate.get_rate(currency)
        name1=rate.get_pair(currency)[0]
        name2=rate.get_pair(currency)[1]
        index1=rate.get_indexes(currency)[0]
        index2=rate.get_indexes(currency)[1]
        print(f'{name1} / {name2} rate is {exchange_rate}')
        print('your ballance:')
        print(f'{name1}: {user.get_balance(index1)}')
        print(f'{name2}: {user.get_balance(index2)}')
        print('ATM ballance:')
        print(f'{name1}: {atm.get_balance(index1)}')
        print(f'{name2}: {atm.get_balance(index2)}')
        try:
            choice = str(input(f'Buy {name1} or Sell {name1}? (buy/sell)'))
        except:
            os.system('cls')
            print('Error: invalid choice')
        if choice == 'sell':
            try:
                amount = float(input(f'How much {name1} do you want to sell?'))
            except:
                print('Error: invalid amount')
            if amount > user.get_balance(index1):
                print(f'Error: not enough {name1} on your account')
            elif amount / exchange_rate > atm.get_balance(index2):
                print(f'Error: not enough {name2} in the atm')
            elif amount < 0:
                print('Error: invalid amount')
            else:
                user.change_balance(index1, user.get_balance(index1) - amount)
                atm.change_balance(index1, atm.get_balance(index1) + amount)
                user.change_balance (index2, user.get_balance(index2) + amount / exchange_rate)
                atm.change_balance(index2, atm.get_balance(index2) - amount / exchange_rate)
                rate.change_rate()
                print('Done!')

        elif choice == 'buy':
            try:
                amount = float(input(f'How much {name1} do you want to buy?'))
            except:
                print('Error: invalid amount')
            if amount > atm.get_balance(index1):
                print(f'Error: not enough {name1} in the atm')
            elif amount / exchange_rate > user.get_balance(index2):
                print(f'Error: not enough {name2} on your account')
            elif amount < 0:
                print('Error: invalid amount')
            else:
                user.change_balance(index1, user.get_balance(index1) + amount)
                atm.change_balance(index1, atm.get_balance(index1) - amount)
                user.change_balance (index2, user.get_balance(index2) - amount / exchange_rate)
                atm.change_balance(index2, atm.get_balance(index2) + amount / exchange_rate)
                rate.change_rate()
                print('Done!')

def print_balance(self):
        '''balance_option=0'''
        os.system('cls')
        print(f'{"=" * 20} {self.name} balance {"=" * 20}')
        print(f'RUB: {self.RUB}')
        print(f'USD: {self.USD}')
        print(f'EUR: {self.EUR}')
        print(f'USDT: {self.USDT}')
        print(f'BTC: {self.BTC}')
        print('  4 - Back')
        print('  5 - Exit')
        '''try:
            balance_option= int(input())
        except:
            print('invalid option')
        if balance_option==4:
           break
        elif balance_option==5:
            sys.exit()
        else:balance_option=0'''

if __name__ == '__main__':
    user = account(1000000.0 , 0 , 0 , 0 , 0 , 'user')
    atm = account(10000.0 ,1000.0 ,1000.0 ,1000.0 ,1.5,'ATM')
    rate = rates(73.84 , 83.78 , 1.137 , 1.0 , 3851.51)
    print('welcome!')
    option=0
    menu()
    while True:

        try:
            option= int(input())
        except:
            print('invalid option')
        os.system('cls')
        if option==1:
            print_balance(user)
        elif option==2:
            print_balance(atm)
        elif option==3:
            trade_window()
        elif option==4:
            menu()
        elif option==5:
            sys.exit()
        else:option=0


