#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    def get_symbol(self):
        return self.__symbol
    def get_company_name(self):
        return self.__company_name
    
def get_stock_list():
    stock_list = []
    stock1 = Stock('AAPL', 'Apple Inc')
    stock2 = Stock('CAT', 'Caterpillar')
    stock3 = Stock('EK', 'Eastman Kodak')
    stock4 = Stock('GOOG', 'Google')
    stock5 = Stock('MSFT', 'Microsoft')

    stock_list.append(stock1)
    stock_list.append(stock2)
    stock_list.append(stock3)
    stock_list.append(stock4)
    stock_list.append(stock5)

    return stock_list

def display_stock_list(stocks):
    print('\nStock Report')
    print('Company    Symbol')
    print('-----------------')

    for stock in stocks:
        print(f'{stock.get_company_name():<15} {stock.get_symbol()}')