import pandas_datareader.data as web
from pandas_datareader import wb
import pandas as pd
import requests
import math, decimal, datetime
import yfinance as yf

USER_AGENT = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/91.0.4472.124 Safari/537.36"
    )
}

class MoonPhase:
    def __init__(self) -> None:
        self.dec = decimal.Decimal
    
    def position(self, now=None):
        if now is None:
            now = datetime.datetime.now()
        else:
            now = datetime.datetime.strptime(now, '%m/%d/%y')

        diff = now - datetime.datetime(2001, 1, 1)
        days = self.dec(diff.days) + (self.dec(diff.seconds) / self.dec(86400))
        lunations = self.dec("0.20439731") + (days * self.dec("0.03386319269"))

        return lunations % self.dec(1)

    def phase(self, pos): 
        index = (pos * self.dec(8)) + self.dec("0.5")
        index = math.floor(index)
        return {
            0: "New Moon", 
            1: "Waxing Crescent", 
            2: "First Quarter", 
            3: "Waxing Gibbous", 
            4: "Full Moon", 
            5: "Waning Gibbous", 
            6: "Last Quarter", 
            7: "Waning Crescent"
        }[int(index) & 7]
    
    def calc_phase(self, now):
        pos = self.position(now)
        phasename = self.phase(pos)
        roundedpos = round(float(pos), 3)
        #print('{} {}'.format(phasename, roundedpos))
        return roundedpos


class FinData:
    def __init__(self):
        self.start = None
        self.end = None
        self.symbol = None
        self.indexes = None
        self.sesh = requests.Session()
        self.sesh.headers.update(USER_AGENT)
        pd.set_option("display.precision", 2)

    @staticmethod
    def _build_df(df):
        df["Date"] = pd.to_datetime(df["DATE"])
        df["Day"] = [i.day for i in df["Date"]]
        df["Month"] = [i.month for i in df["Date"]]
        df["Year"] = [i.year for i in df["Date"]]
        df.drop(["DATE"], axis=1, inplace=True)
        return df

    @staticmethod
    def _build_technical_df(df):
        """
        This static method computes some technical indicators based on the dataframe values
        8ema: 8 days exponential moving average
        21ema: 21 days exponential moving average
        20sma: 20 days moving average
        50sma: 50 days moving average
        100sma: 100 days moving average
        200sma: 200 days moving average
        rstd: TBD
        bollinger_upper_band: TBD
        bollinger_lower_band: TBD
        Daily Return: The % change from yesterday
        """
        df["8ema"] = df["Close"].ewm(span=8, adjust=False).mean()
        df["21ema"] = df["Close"].ewm(span=21, adjust=False).mean()
        df["20sma"] = df["Close"].rolling(window=20).mean()
        df["50sma"] = df["Close"].rolling(window=50).mean()
        df["100sma"] = df["Close"].rolling(window=100).mean()
        df["200sma"] = df["Close"].rolling(window=200).mean()
        df["rstd"] = df["Close"].rolling(window=20).std()
        df["bollinger_upper_band"] = df["20sma"] + 2 * df["rstd"]
        df["bollinger_lower_band"] = df["20sma"] - 2 * df["rstd"]
        df["Daily Return"] = df["Close"].pct_change(1) * 100
        return df

    def get_gdp(self, start, end):
        """
            Get US GDP Rate on a selected timeframe
        """
        df = web.DataReader("GDP", "fred", start=start, end=end).reset_index()
        df = self._build_df(df)
        return df

    def get_gdp_rate(self, country, start, end):
        df = (
            wb.download(
                indicator="NY.GDP.MKTP.KD.ZG", country=[country], start=start, end=end
            )
            .reset_index()
            .set_index("year")
        )
        return df

    def get_unemployment(self, start, end):
        """
            Get Unemployment rate
        """
        df = web.DataReader("UNRATE", "fred", start=start, end=end).reset_index()
        df = self._build_df(df)
        return df

    def get_currencies(self, start, end):
        """
            Get Currency rates compared the the US Dollar
        """
        indexes = ["DEXUSEU", "DEXJPUS", "DEXCHUS", "DEXINUS", "DEXUSUK", "DEXCAUS"]
        df = (
            web.DataReader(indexes, "fred", start=start, end=end)
            .fillna(method="bfill")
            .reset_index()
        )
        df = self._build_df(df)
        df = df.set_index("Date")
        df = df.rename(
            columns={"DEXUSEU": "USD/EU", "DEXJPUS": "USD/YEN", "DEXCHUS": "USD/YUAN",
                     "DEXINUS": "USD/RUPEE", "DEXUSUK": "USD/POUND", "DEXCAUS": "USD/CANADIAN"}
        )
        return df

    def get_finance_data(self, start, end):
        indexes = [
            "UNRATE",
            "GDP",
            "FPCPITOTLZGUSA",
            "CPALTT01USM657N",
            "RSAFS",
            "USSTHPI",
            "IEABC",
            "GFDEBTN",
            "FEDFUNDS",
            "PAYEMS",
            "DCOILWTICO",
            "PALLFNFINDEXQ",
        ]
        df = (
            web.DataReader(indexes, "fred", start=start, end=end)
            .fillna(0)
            .reset_index()
        )
        df = self._build_df(df)
        df = df.rename(
            columns={
                "FPCPITOTLZGUSA": "INFLATION",
                "CPALTT01USM657N": "CPI",
                "RSAFS": "AdvanceRetailSales",
                "USSTHPI": "HousePrices",
                "IEABC": "BalanceOnCurrentAccount",
                "GFDEBTN": "TotalPublicDebtInMillion",
                "FEDFUNDS": "EffectiveFederalFundsRate",
                "PAYEMS": "TotalNonfarm",
                "DCOILWTICO": "CrudeOil",
                "GOLDAMGBD228NLBM": "Gold",
                "PALLFNFINDEXQ": "CommoditiesIndex",
            }
        )
        return df

    def get_stock(self, symbol, start, end):
        moon = MoonPhase()
        # df = web.DataReader(
        #     symbol, "yahoo", start=start, end=end, session=self.sesh
        # ).reset_index()
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="max").reset_index()
        df["Day"] = [i.day for i in df["Date"]]
        df["Month"] = [i.month for i in df["Date"]]
        df["Year"] = [i.year for i in df["Date"]]
        df["MoonPhase"] = [moon.calc_phase(x.strftime('%m/%d/%y')) for x in df["Date"]]
        df = self._build_technical_df(df)
        df = df.set_index("Date")
        return df

    @staticmethod
    def get_war_index():
        """
        War Index is an index based on $ITA.
        iShares U.S. Aerospace & Defense ETF (ITA). This ETF price reflects
        the Index of all defense companies in US.
        """
        sesh = requests.Session()
        sesh.headers.update(USER_AGENT)
        #df = web.DataReader("ITA", "yahoo", start=start, end=end, session=sesh)
        ticker = yf.Ticker("ITA")
        df = ticker.history(period="max").reset_index()
        return df

    @staticmethod
    def get_covid_stat():
        data = "https://api.covidtracking.com/v1/us/daily.csv"
        df = pd.read_csv(data).reset_index(drop=True)
        df["Date"] = pd.to_datetime(df["date"], format="%Y%m%d")
        df = df.set_index("Date")
        return df

    @staticmethod
    def get_solar_cycle():
        data = "https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json"
        df = pd.read_json(data).reset_index(drop=True)
        df["Date"] = pd.to_datetime(df["time-tag"], format="%Y-%m")
        df = df.set_index("Date")
        return df
    
    @staticmethod
    def get_pi_cycles(dates):
        """
            input: dates = {'Date': ["2007-10-11", "2008-09-16", "2020-02-24"]}
            Each wave is built on 6 8.6 mini waves to complete 51.6 major wave
            ecm_dates = {"Date": ["07/20/98", "09/13/00", "11/08/02", "01/02/05",
                  "02/27/07", "04/23/09", "06/18/11", "08/12/13", "10/07/15",
                  "12/01/17", "01/26/20", "03/22/22", "05/16/24",
                  "07/11/26", "09/04/28", "09/04/28", "12/24/32"]}

        """
        df = pd.DataFrame(data=dates)
        df["Date"] = pd.to_datetime(df["Date"])
        df["2.15Years"] = df["Date"] + pd.DateOffset(days=785.2875)
        df["4.3Years"] = df["Date"] + pd.DateOffset(days=1570.575)
        df["8.6Years"] = df["Date"] + pd.DateOffset(days=3141.15)
        df["17.2Years"] = df["Date"] + pd.DateOffset(days=6282.3)
        df["34.4Years"] = df["Date"] + pd.DateOffset(days=12564.6)
        df["51.6Years"] = df["Date"] + pd.DateOffset(days=18846.9)
        return df