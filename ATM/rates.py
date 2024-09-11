import random
import decimal


'''RUB = 1
USD = 2
EUR = 3
USDT = 4
BTC = 5'''


class rates():
    def __init__(self, RUB_USD: decimal, RUB_EUR:decimal, USD_EUR:decimal, USD_USDT:decimal, USD_BTC:decimal):
        self.RUB_USD = RUB_USD
        self.RUB_EUR = RUB_EUR
        self.USD_EUR = USD_EUR
        self.USD_USDT = USD_USDT
        self.USD_BTC = USD_BTC
        self.list_of_rates = [self.RUB_USD, self.RUB_EUR, self.USD_EUR, self.USD_USDT, self.USD_BTC]
        self.list_of_pairs = [['RUB', 'USD'], ['RUB', 'EUR'], ['USD', 'EUR'], ['USD', 'USDT'], ['USD', 'BTC']]
        self.list_of_indexes = [[1,2], [1,3],[2,3],[2,4],[2,5]]

    def get_RUB_USD(self):
        return self.RUB_USD
    def get_RUB_EUR(self):
        return self.RUB_EUR
    def get_USD_EUR(self):
        return self.USD_EUR
    def get_USD_USDT(self):
        return self.USD_USDT
    def get_USD_BTC(self):
        return self.USD_BTC
    def get_rate(self, n):
        return self.list_of_rates[n-1]
    def get_pair(self,n):
        return self.list_of_pairs[n-1]
    def get_indexes(self,n):
        return self.list_of_indexes[n-1]


    def print_rates(self):
        print(f'RUB / USD = {self.RUB_USD}')
        print(f'RUB / EUR = {self.RUB_EUR}')
        print(f'USD / EUR = {self.USD_EUR}')
        print(f'USD / USDT = {self.USD_USDT}')
        print(f'USD /  BTC = {self.USD_BTC}')
        print('6 - Back')
        print('7 - Exit')

    def change_rate(self):
        self.RUB_USD = self.get_RUB_USD() * (1+ random.uniform(-0.05, 0.05))
        self.RUB_EUR = self.get_RUB_EUR() * (1+ random.uniform(-0.05, 0.05))
        self.USD_EUR = self.get_USD_EUR() * (1+ random.uniform(-0.05, 0.05))
        self.USD_USDT = self.get_USD_USDT() * (1+ random.uniform(-0.05, 0.05))
        self.USD_BTC = self.get_USD_BTC() * (1+ random.uniform(-0.05, 0.05))
