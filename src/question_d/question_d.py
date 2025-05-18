#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    def get_symbol(self):
        return self.__symbol
    def get_company_name(self):
        return self.__company_name
    
def stock_purchase_history():
    aapl = Stock("AAPL", "Apple Inc")
    cat = Stock("CAT", "Caterpillar")
    ek = Stock("EK", "Eastman Kodak")
    goog = Stock("GOOG", "Google")
    msft = Stock("MSFT", "Microsoft")

    stock_dict = {
        aapl.get_symbol(): aapl,
        cat.get_symbol(): cat,
        ek.get_symbol(): ek, 
        goog.get_symbol(): goog, 
        msft.get_symbol(): msft
    }

    print("\nStock Purchase History:")
    print("-" * 30)

    for symbol in stock_dict:
        stock_object = stock_dict[symbol]
        print(f"{stock_object.get_symbol()} - {stock_object.get_company_name()}")
    print("-" * 30)
    