class Stock:
    def __init__(self, name, pieces, buy_price, sell_price):
        self.name = name
        self.pieces = pieces
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.profit = sell_price * pieces - buy_price * pieces

    def add_product(self):
        return f"You add {self.pieces} pieces of {self.name}. PROFIT = {self.profit}"
    
product_name = input("Enter the name of product ")
product_pieces = int(input("How many pieces ? "))
product_price = int(input("What is the price / piece ? "))
proruct_sellP = int(input("What is the sell price ? "))

cola = Stock(product_name, product_pieces, product_price, proruct_sellP)

print(cola.add_product())