class ZhModel:
    def __init__(self, *, zh_year, zh_month, zh_day, year_tiandi, shengxiao):
        self.zh_year = zh_year
        self.zh_month = zh_month
        self.zh_day = zh_day
        self.year_tiandi = year_tiandi
        self.shengxiao = shengxiao

    def __str__(self):
        return f"{self.zh_year}{self.zh_month}{self.zh_day} {self.year_tiandi} ({self.shengxiao})"
