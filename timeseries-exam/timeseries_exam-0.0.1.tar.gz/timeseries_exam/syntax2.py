def syntax2():
    print('''
from statsmodels.tsa.statespace.sarimax import SARIMAX
import math
import pylab
import scipy.stats as sci
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_model import ARIMA
from scipy.stats.distributions import chi2
from math import sqrt
import seaborn as sns
sns.set()
warnings.filterwarnings('ignore')

# Pre processing
raw_csv_data = pd.read_csv(r"Weekly.csv")
df = raw_csv_data.copy()
df.date = pd.to_datetime(df.date, dayfirst=True)  # dd/mm/yyy format
df.set_index('date', inplace=True)  # set date as the index
df.isna().sum()
# Filling NA
df.spx = df.spx.fillna(method="ffill")  # Forward fill
df.ftse = df.ftse.fillna(method="bfill")  # Back fill
df.dax = df.dax.fillna(value=df.dax.mean())  # Mean
df.nikkei = df.nikkei.fillna(method="bfill")
# Dropping NA
df.dropna(inplace=True)

# df['first_order']=df['Sales']-df['Sales'].shift(1) - Shift by 1 - 1 lag


df_nipharm = df.copy()
df_nipharm['market_value'] = df['price']

df_nipharm.market_value.plot(figsize=(25, 5), title="NIPHARM")
plt.show()
df_nipharm.drop(df.columns[1], axis=1, inplace=True)

# EDA
df_nipharm.head()
df_nipharm.tail()

# Checking how the data is distributed
# In other words, about 96% of the throughput time series data follows a normal distribution. The other 4% are scattered outliers at both ends.
# Sci.probplot Generates a probability plot of sample data against the quantiles of a specified theoretical distribution (the normal distribution by default).

sci.probplot(df_nipharm.market_value, plot=pylab)
pylab.show()

# FUNCTIONS


def LLR_test(mod_1, mod_2, DF=1):
    L1 = mod_1.fit().llf
    L2 = mod_2.fit().llf
    LR = (2*(L2-L1))
    p = chi2.sf(LR, DF).round(3)
    return p

# Custom Return fucntion


def returns(df, lags):
    df['returns'] = df.market_value.pct_change(lags).mul(100)
    df_new = df.iloc[lags:]
    df_ret = df.returns.iloc[lags:]
    return df_ret, df_new

# Custom ADF test


def adfuller_test(sales):
    result = sts.adfuller(sales)
    labels = ['ADF test: ', 'p-value: ', 'Lags Used: ']
    for value, label in zip(result, labels):
        print(label + ":"+str(value))

    if result[1] <= .05:
        print("reject null hypothesis (h0)\nUnit root does not exist\nSeries is stationary")
    else:
        print(
            "fail to reject null hypothesis(h0)\nUnit root exists\nSeriesis not sationary")

# Custom normalization function


def norm(df):
    benchmark = df.returns.iloc[0]
    df_norm = df.returns.div(benchmark).mul(100)
    df['norm'] = df.returns.div(benchmark).mul(100)


# Plot df
df.ftse.plot(figsize=(25, 5), title="FTSE 100 - UK")
plt.show()


# Stationarity
adfuller_test(df_nipharm_ret.returns)


# To separate the trend and the seasonality from a time series,
# we can decompose the series using the following code.
result = seasonal_decompose(df_close, model='multiplicative', period=7)
fig = plt.figure()
fig = result.plot()
fig.set_size_inches(16, 9)


# ACF
sgt.plot_acf(df_nipharm_ret.norm, zero=False, lags=40)
plt.title("ACF for Returns FTSE", size=24)
plt.show()

# PACF
sgt.plot_pacf(df_nipharm_ret.norm, zero=False, lags=40)
plt.title("PACF for Returns FTSE", size=24)
plt.show()


# MA
model_ret_ma1 = ARMA(df_nipharm_ret.norm, order=(0, 1))
results_ret_ma1 = model_ret_ma1.fit()

# Using the ACF graph we can determine that the 4th lag is significant
model_ret_ma4 = ARMA(df_nipharm_ret.norm, order=(0, 4))
results_ret_ma4 = model_ret_ma4.fit()
print(results_ret_ma4.summary())

print("\nLLR test p-value = " + str(LLR_test(model_ret_ma1, model_ret_ma4)))

# Residual analysis
df_nipharm_ret['res_ret_ma4'] = results_ret_ma4.resid
print(f"Mean: {df_nipharm_ret.res_ret_ma4.mean()}")
print(f"Variance: {df_nipharm_ret.res_ret_ma4.var()}")
print(
    f"Standard Deviation: {round(math.sqrt(df_nipharm_ret.res_ret_ma4.var()), 4)}")

df_nipharm_ret.res_ret_ma4.plot(figsize=(25, 5))
plt.title("Residuals of Normalised Returns", size=24)
plt.show()

# Checking for stationarity of residuals
adfuller_test(df_nipharm_ret.res_ret_ma4)

# Residual ACF
sgt.plot_acf(df_nipharm_ret.res_ret_ma4, zero=False, lags=40)
plt.title("ACF for Residuals Nipharm MA(4)", size=24)
plt.show()

# AR

model_ret_ar1 = ARMA(df_nipharm_ret.norm, order=(1, 0))
results_ret_ar1 = model_ret_ar1.fit()

# Using PACF we see that 4th lag is significant
model_ret_ar4 = ARMA(df_nipharm_ret.norm, order=(4, 0))
results_ret_ar4 = model_ret_ar4.fit()
print(results_ret_ar4.summary())
print("\nLLR test p-value = " + str(LLR_test(model_ret_ar1, model_ret_ar4)))

# Print aic LLR
print("ARMA(3,3): \tLL = ", results_ret_ar3_ma3.llf,
      "\tAIC = ", results_ret_ar3_ma3.aic)


# Predictions
start_date = "2020-06-28"
end_date = "2022-12-06"
model_ar1_ma3 = ARIMA(df_nipharm_ret.price, order=(1, 0, 3))
results_ar1_ma3 = model_ar1_ma3.fit()

df_nipharm_ret['predicted'] = results_ar1_ma3.predict(start=491, end=610)
df_nipharm_ret[['price', 'predicted']].plot(figsize=(25, 5))

# New Data for prediction
prediction_index = pd.date_range(
    start='2022-12-06', periods=49, freq='W', name='datetime_utc')
prediction_index

# Sarimax

SARIMAXmodel = SARIMAX(df_nipharm_ret.price, order=(1, 0, 3), seasonal_order=(
    0, 2, 2, 12), enforce_stationarity=False, enforce_invertibility=False)
SARIMAXmodel = SARIMAXmodel.fit()
SARIMAXmodel.bic

SARIMAXmodel_Trend = SARIMAX(df_nipharm_ret.price, order=(
    1, 0, 3), enforce_stationarity=False, enforce_invertibility=False)
SARIMAXmodel_Trend = SARIMAXmodel_Trend.fit()

y_pred = SARIMAXmodel.get_forecast(len(prediction_index))
y_pred_df = y_pred.conf_int(alpha=0.05)
y_pred_df["Predictions"] = SARIMAXmodel.predict(
    start=y_pred_df.index[0], end=y_pred_df.index[-1])
y_pred_df.index = prediction_index
y_pred_out = y_pred_df["Predictions"]

y_pred_2 = SARIMAXmodel_Trend.get_forecast(len(prediction_index))
y_pred_df_2 = y_pred_2.conf_int(alpha=0.05)
y_pred_df_2["TrendLine"] = SARIMAXmodel_Trend.predict(
    start=y_pred_df_2.index[0], end=y_pred_df_2.index[-1])
y_pred_df_2.index = prediction_index
y_pred_out_2 = y_pred_df_2["TrendLine"]


plt.figure(figsize=(20, 5))

plt.plot(df_nipharm_ret.price, color='blue', label='data')
plt.plot(y_pred_out, color='red', label='SARIMA prediction')
plt.plot(y_pred_out_2, color='green', label='Trendline')

plt.legend()
plt.show()

    ''')

syntax2()