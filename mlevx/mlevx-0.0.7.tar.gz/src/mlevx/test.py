import pandas as pd
from regbot import signal, Regbot

df = pd.read_csv('../jupyter/mlevx_train.csv')

y_pred = []
def getSignal(open,close,utcdatetime,dir):
    return signal(open,close,utcdatetime,dir)




# select short profitable trades
df1 = df[df['close_profit_abs'] < 0]
df1 = df1[df1['is_short'] == 1]
print(df1.head())
# select long profitable trades
df2 = df[df['close_profit_abs'] < 0]
df2 = df2[df2['is_short'] == 0]
print(df2.head())


# Run all predictions
df1['enter_short_pred'] = df.apply(lambda row: getSignal(row['open'], row['close'], row['date'],'short'), axis=1)
df2['enter_long_pred'] = df.apply(lambda row: getSignal(row['open'], row['close'], row['date'],'long'), axis=1)


print(len(df1[df1['enter_short_pred'] == df1['is_short']]), len(df) )
print(len(df2[df2['enter_long_pred'] == df2['is_short']]), len(df) )

print(df1[df1['is_short']==1].head(15))
print(df2[df2['is_short']==0].head(15))