# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:41:10 2022

@author: ScottStation
"""


import qesdk2
from datetime import datetime,timedelta
#qesdk.auth('quantease','$1$$k7yjPQKv8AJuZERDA.eQX.')
#df = qesdk.get_price('AG2212.SFE','2022-10-01','2022-11-01','daily')
#print(df)
qesdk2.auth('quantease','$1$$k7yjPQKv8AJuZERDA.eQX.')

print(qesdk2.get_broker_info('cjqh3'))
print(qesdk2.get_valid_instID('si9w'))#
#print(qesdk2.is_valid_instID('IC2309.SFE'))
#print(qesdk2.is_valid_trade_time('IC2306.SFE',datetime.now()+timedelta(hours=5)))
#df = qesdk.get_realtime_minute_prices(['AU2212_SFE','AG2301.SFE'])
#print(df)
'''
testdf = qesdk.get_bar_data(['AU2212.SFE'],'2022-12-06')
for i in testdf['AU2212.SFE'].index:
    print(testdf['AU2212.SFE'].loc[i,'time'],testdf['AU2212.SFE'].loc[i, 'close'])
testdf['AU2212.SFE']['close'].plot()    
'''