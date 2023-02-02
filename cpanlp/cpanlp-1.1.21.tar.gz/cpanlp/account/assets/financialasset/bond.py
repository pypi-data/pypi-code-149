from cpanlp.account.assets.financialasset.financialasset import *

class Bond(FinancialAsset):
    accounts = []
    def __init__(self, account, debit,date,parties, consideration, obligations,value, rate):
        super().__init__(account, debit,date,parties, consideration, obligations,value)
        self.rate = rate
        Bond.accounts.append(self)