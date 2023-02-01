# -*- coding: utf-8 -*-
# @Time        : 2022/4/13 9:53
# @Author      : Matrix
# @FileName    : risk_control_indicators.py
# @Software    : PyCharm

import pandas as pd
import numpy as np
import joblib
import toad
import warnings
warnings.filterwarnings("ignore")

class RiskControlIndicators():
    def __init__(self):
        super(RiskControlIndicators, self).__init__()

    def cal_ks(self, df, score_col, target):
        """
        :param df: 数据集
        :param score_col: 分数
        :param target: 标签
        :return: KS值
        """
        total_bad = df[target].sum()
        total_good = df[target].count() - total_bad
        score_list = list(df[score_col])
        target_list = list(df[target])
        items = sorted(zip(score_list, target_list), key=lambda x: x[0])
        step = (max(score_list) - min(score_list)) / 200

        score_bin = []
        good_rate = []
        bad_rate = []
        ks_list = []
        for i in range(1, 201):
            idx = min(score_list) + i * step
            score_bin.append(idx)
            target_bin = [x[1] for x in items if x[0] < idx]
            bad_num = sum(target_bin)
            good_num = len(target_bin) - bad_num
            goodrate = good_num / total_good
            badrate = bad_num / total_bad
            ks = abs(goodrate - badrate)
            good_rate.append(goodrate)
            bad_rate.append(badrate)
            ks_list.append(ks)
        ks_max = max(ks_list)
        return ks_max


    def cale_combi_badrate(self, data=None, col=None, targ='tar', cut=True, original_col=None, bins=10, sort=True,show_all=False):
        """
        将 original_col 分箱，计算KS,IV,WOE等模型评估指标
        :param data: 数据集
        :param col: original_col 分箱后的字段名
        :param targ: 标签
        :param cut: 是否切分
        :param original_col:
        :param bins: 分箱数
        :param sort: 按 col 排序
        :param show_all: 显示所有列
        :return: DataFrame
        """
        if cut:
            data = data.copy()
            col = f"{original_col}_range"
            data[col] = pd.qcut(data[original_col], bins)
        group = data.groupby([col])[targ].agg([("totle_cnt", "count"), ("bad_cnt", "sum"), ("bad_rate", "mean")])
        group["good_cnt"] = group["totle_cnt"] - group["bad_cnt"]
        if sort:
            group = group.reset_index().sort_values(by=col, ascending=False)
        group["totle_cnt_cum"] = group["totle_cnt"].cumsum()
        group["bad_cnt_cum"] = group["bad_cnt"].cumsum()
        group["good_cnt_cum"] = group["good_cnt"].cumsum()
        group["bad_rate_cum"] = group["bad_cnt_cum"] / group["totle_cnt_cum"]
        bad_total = sum(group["bad_cnt"])
        group["bad_pcnt"] = group["bad_cnt"] / bad_total
        # group["good"]=group["count"]-group["bad"]
        group["good_rate"] = 1 - group["bad_rate"]
        good_total = sum(group["good_cnt"])
        group["good_pcnt"] = group["good_cnt"] / good_total
        group["count_distr"] = group["totle_cnt"] / data.shape[0]
        group["woe"] = np.log(group["good_pcnt"] / group["bad_pcnt"])
        group["iv"] = (group["good_pcnt"] - group["bad_pcnt"]) * np.log(group["good_pcnt"] / group["bad_pcnt"])
        group["iv_sum"] = sum(group["iv"])
        group["lift"] = group["bad_rate"] / data[targ].mean()
        group['cumsum_good'] = 1.0 * group.good_cnt.cumsum() / sum(group.good_cnt)
        group['cumsum_bad'] = 1.0 * group.bad_cnt.cumsum() / sum(group.bad_cnt)
        group["ks"] = np.abs(group["cumsum_good"] - group["cumsum_bad"])
        group["ks_max"] = max(group["ks"])
        group = group.reset_index()
        group["count_distr_cum"] = group["count_distr"].cumsum()
        if show_all:
            return group
        else:
            return group[[
                col, 'totle_cnt', 'totle_cnt_cum', 'bad_rate', 'bad_rate_cum', 'count_distr',
                'count_distr_cum', 'woe', 'iv_sum', 'lift', 'ks', 'ks_max'
            ]]


    def cale_woe(self, df1, var, target):
        """
        模型评估指标的计算
        :param df1: 数据集
        :param var: 特征
        :param target: 标签
        :return: 包含 WOE 值的 DataFrame
        """
        df = df1.copy()
        # df[var]=df[var].fillna("missing")
        # data = df.groupby([var])[target].agg({"count": "count", "bad": "sum", "bad_rate": "mean"}).reset_index()
        data = df.groupby([var])[target].agg([("count", "count"), ("bad", "sum"), ("bad_rate", "mean")]).reset_index()
        bad_total = sum(data["bad"])
        data["bad_pcnt"] = data["bad"] / bad_total
        data["good"] = data["count"] - data["bad"]
        data["good_rate"] = 1 - data["bad_rate"]
        good_total = sum(data["good"])
        data["good_pcnt"] = data["good"] / good_total
        data["count_distr"] = data["count"] / df.shape[0]
        data["woe"] = np.log(data["good_pcnt"] / data["bad_pcnt"])
        data["iv"] = (data["good_pcnt"] - data["bad_pcnt"]) * np.log(data["good_pcnt"] / data["bad_pcnt"])
        data["iv_sum"] = sum(data["iv"])
        data["lift"] = data["bad_rate"] / df[target].mean()
        data["variable"] = var
        print("{}等于'{}'时最大提升度为{:.2f}".format(
            var, str(data[data["lift"] == data["lift"].max()][var].values[0]), data["lift"].max()
        ))
        data = data[[
            "variable", var, 'count', 'bad', 'bad_rate', 'good', 'good_rate',
            'count_distr', 'woe', 'iv', 'iv_sum', 'lift'
        ]]
        return data


    def woe_values(self, df, col, tar):
        """
        WOE 值计算
        :param df: 数据集
        :param col: 特征
        :param tar: 标签
        :return: 转换成WOE值的字典
        """
        woe_data = self.cale_woe(df, col, tar)
        woe_dict = {x: y for x, y in zip(woe_data[col], woe_data["woe"])}
        return woe_dict


    def woe_mapping(self, df, tar, woe_col=[], None_target=True, woe_dict_name="woe_dict"):
        """
        WOE值映射
        :param df: 数据集
        :param tar: 标签
        :param woe_col: 需要做 WOE 编码的特征列表
        :param None_target: 为True，则加载 WOE字典，将woe_col中的特征做WOE值映射；为False，则生成WOE字典
        :param woe_dict_name:
        :return:WOE转换后的数据集
        """
        if None_target:
            # dump_model(woe_dict,file_name="woe_dict.pkl")
            woe_dict_loan = joblib.load(f"{woe_dict_name}.pmml")
            for col in woe_dict_loan.keys():
                df[col] = df[col].map(woe_dict_loan[col])
        else:
            woe_dict = {}
            for col in woe_col:
                woe_dict[col] = self.woe_values(df, col, tar)
            for col in woe_dict.keys():
                df[col] = df[col].map(woe_dict[col])
            joblib.dump(woe_dict, f"{woe_dict_name}.pmml")
        return df


    def clac_feature_psi(self, train_data=None, oot_data=None, most_importance=None, quant=10):
        """
        train_data: 训练集
        oot_data: 测试集
        most_importance: 特征
        tar: Y值(标签)
        """
        combiner = toad.transform.Combiner()
        combiner.fit(train_data[most_importance], train_data.tar, n_bins=quant, method='quantile', empty_separate=True)
        psi_values = toad.metrics.PSI(train_data[most_importance], oot_data[most_importance], combiner=combiner)
        feat_psi = pd.DataFrame()
        feat_psi["feature"] = most_importance
        feat_psi["psi_value"] = psi_values.values
        return feat_psi.sort_values(by="psi_value", ascending=False)  # 添加排序

    # 查看缺失值
    def check_missing_ratio(self, df):
        total = df.isnull().sum().sort_values(ascending=False)
        percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
        return missing_data

    # 查iv
    def cale_iv(self, data=None,featurs=[],target=None):
        """
        :param data:  数据集
        :param featurs:  计算iv的featurs
        :param target: Y 标签名
        :return:
        """
        df_iv = toad.stats.quality(data[featurs],target=target)
        return df_iv
