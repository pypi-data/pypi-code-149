import pandas as pd


def spinning_top(df, threshold=0.05):
    for i in range(len(df)):
        curr = df.iloc[i]
        if (curr['High'] - curr['Low']) > (threshold * (curr['Close'] - curr['Open'])):
            df.at[i, 'Spinning Top'] = True
        else:
            df.at[i, 'Spinning Top'] = False
    return df


def marubozu(df, threshold=0.05):
    for i in range(len(df)):
        curr = df.iloc[i]
        if (curr['High'] - curr['Open']) < (threshold * (curr['Close'] - curr['Open'])) and (curr['Close'] - curr['Low']) < (threshold * (curr['Close'] - curr['Open'])):
            if curr['Close'] > curr['Open']:
                df.at[i, 'Marubozu'] = 'Bullish'
            else:
                df.at[i, 'Marubozu'] = 'Bearish'
        else:
            df.at[i, 'Marubozu'] = False
    return df


def hammer(df, threshold=0.05):
    for i in range(len(df)):
        curr = df.iloc[i]
        if (curr['High'] - curr['Close']) < (threshold * (curr['Close'] - curr['Open'])) and (curr['Close'] - curr['Low']) >= 2 * (curr['Open'] - curr['Close']):
            df.at[i, 'Hammer'] = True
        else:
            df.at[i, 'Hammer'] = False
    return df


def inverted_hammer(df, threshold=0.05):
    for i in range(len(df)):
        curr = df.iloc[i]
        if (curr['High'] - curr['Close']) < (threshold * (curr['Close'] - curr['Open'])) and (curr['Close'] - curr['Low']) < (curr['Open'] - curr['Close']):
            df.at[i, 'Inverted Hammer'] = True
        else:
            df.at[i, 'Inverted Hammer'] = False
    return df


def doji(df, threshold=0.05):
    for i in range(len(df)):
        curr = df.iloc[i]
        if abs(curr['Close'] - curr['Open']) < threshold * (curr['High'] - curr['Low']):
            if curr['Close'] > curr['Open']:
                df.at[i, 'Doji'] = 'Gravestone Doji'
            elif curr['Close'] < curr['Open']:
                df.at[i, 'Doji'] = 'Dragonfly Doji'
            else:
                df.at[i, 'Doji'] = 'Long-Legged Doji'
        else:
            df.at[i, 'Doji'] = False
    return df


def hanging_man(df, threshold=0.05):
    for i in range(len(df)):
        curr = df.iloc[i]
        if (curr['Close'] - curr['Low']) < threshold * (curr['High'] - curr['Low']) and curr['Close'] > curr['Open']:
            df.at[i, 'Hanging Man'] = True
        else:
            df.at[i, 'Hanging Man'] = False
    return df


def shooting_star(df, threshold=0.05):
    for i in range(len(df)):
        curr = df.iloc[i]
        if (curr['High'] - curr['Close']) < threshold * (curr['High'] - curr['Low']) and curr['Close'] < curr['Open']:
            df.at[i, 'Shooting Star'] = True
        else:
            df.at[i, 'Shooting Star'] = False
    return df


def morning_star(df, threshold=0.05):
    for i in range(len(df) - 2):
        prev = df.iloc[i]
        curr = df.iloc[i+1]
        next = df.iloc[i+2]
        if prev['Close'] < prev['Open'] and curr['Close'] > curr['Open'] and next['Close'] > next['Open']:
            if (curr['Close'] - curr['Open']) / (curr['High'] - curr['Low']) > threshold and (next['Close'] - next['Open']) / (next['High'] - next['Low']) > threshold:
                if (next['Close'] - curr['Open']) / (next['Close'] - next['Open']) > threshold:
                    df.at[i+2, 'Morning Star'] = True
                else:
                    df.at[i+2, 'Morning Star'] = False
            else:
                df.at[i+2, 'Morning Star'] = False
        else:
            df.at[i+2, 'Morning Star'] = False
    return df


def evening_star(df, threshold=0.05):
    for i in range(len(df) - 2):
        prev = df.iloc[i]
        curr = df.iloc[i+1]
        next = df.iloc[i+2]
        if prev['Close'] > prev['Open'] and curr['Close'] < curr['Open'] and next['Close'] < next['Open']:
            if (curr['Close'] - curr['Open']) / (curr['High'] - curr['Low']) > threshold and (next['Close'] - next['Open']) / (next['High'] - next['Low']) > threshold:
                if (next['Open'] - curr['Close']) / (next['Close'] - next['Open']) > threshold:
                    df.at[i+2, 'Evening Star'] = True
                else:
                    df.at[i+2, 'Evening Star'] = False
            else:
                df.at[i+2, 'Evening Star'] = False
        else:
            df.at[i+2, 'Evening Star'] = False
    return df


def bullish_harami(df, threshold=0.05):
    for i in range(len(df) - 1):
        prev = df.iloc[i]
        curr = df.iloc[i+1]
        if prev['Close'] > prev['Open'] and curr['Close'] < curr['Open']:
            if (curr['Close'] - curr['Open']) / (prev['High'] - prev['Low']) < threshold:
                df.at[i+1, 'Bullish Harami'] = True
            else:
                df.at[i+1, 'Bullish Harami'] = False
        else:
            df.at[i+1, 'Bullish Harami'] = False
    return df


def bearish_harami(df, threshold=0.05):
    for i in range(len(df) - 1):
        prev = df.iloc[i]
        curr = df.iloc[i+1]
        if prev['Close'] < prev['Open'] and curr['Close'] > curr['Open']:
            if (curr['Close'] - curr['Open']) / (prev['High'] - prev['Low']) < threshold:
                df.at[i+1, 'Bearish Harami'] = True
            else:
                df.at[i+1, 'Bearish Harami'] = False
        else:
            df.at[i+1, 'Bearish Harami'] = False
    return df


def bullish_engulfing(df, threshold=0.05):
    for i in range(len(df) - 1):
        prev = df.iloc[i]
        curr = df.iloc[i+1]
        if prev['Close'] < prev['Open'] and curr['Close'] > curr['Open']:
            if (curr['Close'] - curr['Open']) / (curr['High'] - curr['Low']) > threshold and (curr['Close'] - prev['Open']) / (prev['Close'] - prev['Open']) > threshold:
                df.at[i+1, 'Bullish Engulfing'] = True
            else:
                df.at[i+1, 'Bullish Engulfing'] = False
        else:
            df.at[i+1, 'Bullish Engulfing'] = False
    return df


def bearish_engulfing(df, threshold=0.05):
    for i in range(len(df) - 1):
        prev = df.iloc[i]
        curr = df.iloc[i+1]
        if prev['Close'] > prev['Open'] and curr['Close'] < curr['Open']:
            if (prev['Close'] - prev['Open']) / (prev['High'] - prev['Low']) > threshold and (prev['Close'] - curr['Open']) / (curr['Close'] - curr['Open']) > threshold:
                df.at[i+1, 'Bearish Engulfing'] = True
            else:
                df.at[i+1, 'Bearish Engulfing'] = False
        else:
            df.at[i+1, 'Bearish Engulfing'] = False
    return df


def all_patterns(df, threshold=0.05, single=False):
    if single:
        df_single = df.copy()
    df = doji(df, threshold)
    df = morning_star(df, threshold)
    df = evening_star(df, threshold)
    df = bullish_harami(df, threshold)
    df = bearish_harami(df, threshold)
    df = bullish_engulfing(df, threshold)
    df = bearish_engulfing(df, threshold)
    # replace NaN with empty string
    df = df.fillna('')

    if single:
        df_single['Patterns'] = df.apply(
            lambda x: [col for col in df.columns if x[col] == True], axis=1)
        df_single['Patterns'] = df_single['Patterns'].apply(
            lambda x: ', '.join(x))
        return df_single
    df['Patterns'] = df.apply(
        lambda x: [col for col in df.columns if x[col] == True], axis=1)
    df['Patterns'] = df['Patterns'].apply(lambda x: ', '.join(x))
    return df
    # for each row in dataframe, create a list of all patterns that are true


df = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
      'Open': [100, 101, 102, 99, 100],
      'High': [105, 106, 104, 102, 101],
      'Low': [99, 100, 99, 97, 99],
      'Close': [102, 103, 101, 100, 101],
      'Volume': [100, 200, 300, 400, 500], }
df = pd.DataFrame(df)
df = all_patterns(df, single=True)
print(df)
