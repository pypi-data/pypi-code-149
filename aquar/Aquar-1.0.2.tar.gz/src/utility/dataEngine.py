
from . import utils
from subDataEngine import dataLoaderDaily
# from subDataEngine import dataLoader1Min
# from subDataEngine import dataLoaderStockDaily

class dataEngine():
    def init(self):
        self.data_type = utils.globalConfig['backtest'].get('dataType','DAILY')
        if self.data_type == 'DAILY':
            self.sub_engine = dataLoaderDaily.dataEngine()
        # elif self.data_type == '1Min':
        #     self.sub_engine = dataLoader1Min.dataEngine()
        # elif self.data_type == 'STOCK_DAILY':
        #     self.sub_engine = dataLoaderStockDaily.dataEngine()
        self.sub_engine.init()

    def pop_data(self):
        self.sub_engine.pop_data()    

            
            

