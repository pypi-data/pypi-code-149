class Repurchase:
    def __init__(self, company, stock_symbol, repurchase_price, repurchase_quantity):
        self.company = company
        self.stock_symbol = stock_symbol
        self.repurchase_price = repurchase_price
        self.repurchase_quantity = repurchase_quantity
        self.total_cost = self.repurchase_price * self.repurchase_quantity
        self.method= None