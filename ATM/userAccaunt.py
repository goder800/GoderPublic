import decimal
class account():
    def __init__(self, RUB:decimal, USD:decimal, EUR:decimal, USDT:decimal, BTC:decimal, name):
            self.name=name
            self.RUB= RUB
            self.USD =USD
            self.EUR =EUR
            self.USDT =USDT
            self.BTC =BTC
            self.list_of_balance = [self.RUB, self.USD, self.EUR, self.USDT, self.BTC]



    def get_balanceRUB(self):
        return self.RUB
    def get_balanceUSD(self):
        return self.USD
    def get_balanceEUR(self):
        return self.EUR
    def get_balanceUSDT(self):
        return self.USDT
    def get_balanceBTC(self):
        return self.BTC
    def get_balance(self, n):
        match n:
            case 1: return self.RUB
            case 2: return self.USD
            case 3: return self.EUR
            case 4: return self.USDT
            case 5: return self.BTC
    def change_balance(self, n, value):
        match n:
            case 1: self.RUB = value
            case 2: self.USD = value
            case 3: self.EUR = value
            case 4: self.USDT = value
            case 5: self.BTC = value



