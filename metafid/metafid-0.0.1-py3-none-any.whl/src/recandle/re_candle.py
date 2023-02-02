import pandas as pd
import numpy as np
from scipy import stats


class ReCandle:

    def heikin_ashi(self, df: pd.DataFrame):
        """
        Heikin-Ashi Candlestick.
        :param df: pandas data-frame with [open, high, low, close] columns name.
        :return: Heikin-Ashi close-open-high-low.
        """
        df.columns = df.columns = df.columns.str.lower()
        df = df.assign(ha_close=lambda x: np.mean([x.open, x.high, x.low, x.close], axis=0))
        df = df.assign(ha_open=lambda x: np.mean([x.open, x.ha_close], axis=0))
        for row in range(1, len(df) - 1):
            df.loc[row, "ha_open"] = np.mean([df.loc[row - 1, "ha_open"], df.loc[row - 1, "ha_close"]])
        df = df.assign(ha_high=lambda x: np.max([x.high, x.ha_open, x.ha_close], axis=0))
        df = df.assign(ha_low=lambda x: np.min([x.low, x.ha_open, x.ha_close], axis=0))
        return df

    def linear_regression(self, df: pd.DataFrame, length: int):
        """
        Linear_Regression Candlestick.
        :param df: pandas data-frame with [open, high, low, close] columns name;
        :param length: int
            Number of previous data to fit on LR

        :return: Liner Regression open-high-low-close;
        """
        df = df.assign(lr_open=np.nan,
                       lr_high=np.nan,
                       lr_low=np.nan,
                       lr_close=np.nan)
        x = np.array(range(length + 1))
        columns = ["open", "high", "low", "close"]
        for i in range(len(df) - length):
            for col in columns:
                y = df.loc[i:i + length, col].values
                slope, intercept, r, p, std_err = stats.linregress(x, y)
                df.loc[i + length, f"lr_{col}"] = intercept + slope * (length - 1)
        return df

