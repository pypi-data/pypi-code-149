#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:Alexander
# File:modelTools.py
# Create Time:2023-02-01 10:50:34

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold
import lightgbm as lgb
import xgboost as xgb
import numpy as np
import pandas as pd
import joblib


def load_model(path):
    return joblib.load(path)


def dump_model(clf, file_name='lgb.model'):
    # lr是一个LogisticRegression模型
    # path='/Users/qianfeng1/Desktop/products/product/model_flask/'
    joblib.dump(clf, file_name)


# def split_data(df_final, target, LR_type=False, test_size=0.3, random_state=1):
#     X = df_final.drop(target, axis=1)
#     y = df_final[target]
#     X_train, X_test, y_train, y_test = train_test_split(X,
#                                                         y,
#                                                         test_size=test_size,
#                                                         random_state=1)
#     if LR_type:
#         X_train['intercept'] = [1] * X_train.shape[0]
#         X_test['intercept'] = [1] * X_test.shape[0]
#         return X_train, X_test, y_train, y_test
#     else:
#         print("训练样本好坏比{:.3f},样本量{}".format(y_train.mean(), y_train.shape[0]))
#         print("oot样本好坏比{:.3f}，样本量{}".format(y_test.mean(), y_test.shape[0]))
#         return X_train, X_test, y_train, y_test

def predtion(vail_data=None, model_name="select", select_=[]):
    clf_0 = load_model(f"{model_name}_lgb_0.pmml")
    clf_1 = load_model(f"{model_name}_lgb_1.pmml")
    clf_2 = load_model(f"{model_name}_lgb_2.pmml")
    clf_3 = load_model(f"{model_name}_lgb_3.pmml")
    clf_4 = load_model(f"{model_name}_lgb_4.pmml")
    vail_data["pred0"] = clf_0.predict_proba(vail_data[select_], num_iteration=clf_0.best_iteration_)[:, 1]
    vail_data["pred1"] = clf_1.predict_proba(vail_data[select_], num_iteration=clf_1.best_iteration_)[:, 1]
    vail_data["pred2"] = clf_2.predict_proba(vail_data[select_], num_iteration=clf_2.best_iteration_)[:, 1]
    vail_data["pred3"] = clf_3.predict_proba(vail_data[select_], num_iteration=clf_3.best_iteration_)[:, 1]
    vail_data["pred4"] = clf_4.predict_proba(vail_data[select_], num_iteration=clf_4.best_iteration_)[:, 1]
    vail_data["pred_mean"] = (vail_data["pred0"] + vail_data[
        "pred1"] + vail_data["pred2"] + vail_data["pred3"] + vail_data["pred4"]) / 5
    vail_data["score"] = vail_data["pred_mean"].apply(prob_to_score)
    return vail_data


def select_important_feature(df, thro=0, numbers=100, select_values=False):
    if select_values:
        df = df[df["importance_value"] > thro]
        feature = df["feature"].tolist()
    else:
        df = df.sort_values(by="importance_value", ascending=False)
        feature = df["feature"][0:numbers].tolist()
    return feature


def split_ootdata(df, borrow_time, tar, oot_time='2019-11-20'):
    df[borrow_time] = pd.to_datetime(df[borrow_time])
    df_train = df[df[borrow_time] <= oot_time]
    df_oot = df[df[borrow_time] > oot_time]
    print("df_train", df_train.shape[0])
    print("df_oot", df_oot.shape[0])
    X_train = df_train.drop([borrow_time, tar], axis=1)
    y_train = df_train[tar]
    X_oot = df_oot.drop([borrow_time, tar], axis=1)
    y_oot = df_oot[tar]
    print(f"训练样本好坏比{y_train.mean()},样本量{y_train.shape[0]}")
    print(f"oot样本好坏比{y_oot.mean()}，样本量{y_oot.shape[0]}")
    return X_train, y_train, X_oot, y_oot


def cal_ks(df, score_col, target):
    """
    df:数据集
    target:目标变量的字段名
    score_col:最终得分的字段名
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


def prob_to_score(prob, base_point=450, PDO=100):
    y = np.log(prob / (1 - prob))
    return base_point + PDO / np.log(2) * (-y)


def split_data(train_dt=None, vail_dt=None, target=None):
    X_train = train_dt.drop(target, axis=1)
    y_train = train_dt[target]
    columns = train_dt.columns.tolist()
    columns.remove(target)
    X_test = vail_dt[columns]
    y_test = vail_dt[target]
    print(f"训练样本好坏比{y_train.mean()},样本量{y_train.shape[0]}")
    print(f"oot样本好坏比{y_test.mean()}，样本量{y_test.shape[0]}")
    return X_train, X_test, y_train, y_test


def lgbClassifer_KFold(X,
                       y,
                       X_test,
                       y_test,
                       num_folds=None,
                       estimators=None,
                       max_depth=None,
                       num_leaves=None,
                       scale_pos_weight=None,
                       learning_rate=None,
                       colsample_bytree=None,
                       subsample=None,
                       reg_alpha=None,
                       reg_lambda=None,
                       min_split_gain=None,
                       min_child_weight=None,
                       min_child_samples=None,
                       model_name=None):
    feature_names = list(X.columns)
    train_scores = []
    valid_scores = []
    test_scores = []
    X_valid_pred = np.zeros(X.shape[0])
    test_pred = np.zeros(X_test.shape[0])
    feature_importance_value = np.zeros(len(feature_names))

    k_fold = KFold(n_splits=num_folds, shuffle=False, random_state=50)

    for n_fold, (train_idx, valid_idx) in enumerate(k_fold.split(X, y)):
        print("continue...", n_fold + 1)
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_valid, y_valid = X.iloc[valid_idx], y.iloc[valid_idx]

        clf = lgb.LGBMClassifier(nthread=-1,
                                 n_estimators=estimators,
                                 learning_rate=learning_rate,
                                 num_leaves=num_leaves,
                                 colsample_bytree=colsample_bytree,
                                 subsample=subsample,
                                 max_depth=max_depth,
                                 reg_alpha=reg_alpha,
                                 reg_lambda=reg_lambda,
                                 min_split_gain=min_split_gain,
                                 min_child_weight=min_child_weight,
                                 silent=-1,
                                 verbose=-1,
                                 scale_pos_weight=scale_pos_weight,
                                 min_child_samples=min_child_samples,
                                 random_state=2018,
                                 importance_type="gain",
                                 class_weight="balanced")

        clf.fit(X_train,
                y_train,
                eval_set=[(X_train, y_train), (X_valid, y_valid)],
                eval_names=['train', 'valid'],
                eval_metric='auc',
                verbose=200,
                early_stopping_rounds=200)

        X_valid_pred[valid_idx] = clf.predict_proba(
            X_valid, num_iteration=clf.best_iteration_)[:, 1]
        test_pred += clf.predict_proba(
            X_test, num_iteration=clf.best_iteration_)[:, 1] / num_folds
        feature_importance_value += clf.feature_importances_ / num_folds

        # 计算auc值
        # print("clf.best_score_:",clf.best_score_)
        valid_auc = clf.best_score_['valid']['auc']
        train_auc = clf.best_score_['train']['auc']
        test_auc = roc_auc_score(y_test, test_pred)
        # valid_score = model.best_score_['valid']['auc']
        # train_score = model.best_score_['train']['auc']

        train_scores.append(train_auc)
        valid_scores.append(valid_auc)
        test_scores.append(test_auc)
        dump_model(clf, f"{model_name}_lgb_{n_fold}.pmml")

    # 输出信息

    # feature_importance_df
    feature_importance_df = pd.DataFrame({
        'feature':
            feature_names,
        'importance_value':
            feature_importance_value
    })

    # train_scores and valid_scores metrics
    # all_valid_score = roc_auc_score(y, X_valid_pred)

    fold_names = np.array(range(num_folds)) + 1

    metrics = pd.DataFrame({
        'num_fold': fold_names,
        'train_auc': train_scores,
        'valid_auc': valid_scores,
        'test_auc': test_scores
    })
    met = dict(metrics.mean())
    met["num_fold"] = "auc_mean"
    met = pd.DataFrame.from_dict(met, orient='index').T
    metrics = pd.concat([metrics, met], axis=0).set_index("num_fold")
    feature_importance_df = feature_importance_df.sort_values(
        by="importance_value", ascending=False)
    return feature_importance_df, metrics, test_pred


def lgb_Classifer_model(train_dt=None,
                        vail_dt=None,
                        target=None,
                        num_folds=5,
                        num_leaves=20,
                        estimators=1000,
                        max_depth=4,
                        scale_pos_weight=0.5,
                        learning_rate=0.05,
                        colsample_bytree=0.7,
                        subsample=0.7,
                        reg_alpha=10,
                        reg_lambda=20,
                        min_split_gain=0.5,
                        min_child_weight=0.1,
                        min_child_samples=50,
                        model_name="all_feature"):
    X_train, X_test, y_train, y_test = split_data(train_dt=train_dt,
                                                  vail_dt=vail_dt,
                                                  target=target)

    # isNowOverdue=X_test["isNowOverdue"]
    # X_train,X_test=X_train.drop("isNowOverdue",axis=1),X_test.drop("isNowOverdue",axis=1)
    feat_col = X_train.columns.tolist()
    feature_importance_df, metrics, test_pred = lgbClassifer_KFold(
        X_train,
        y_train,
        X_test,
        y_test,
        num_folds=num_folds,
        estimators=estimators,
        num_leaves=num_leaves,
        max_depth=max_depth,
        scale_pos_weight=scale_pos_weight,
        learning_rate=learning_rate,
        colsample_bytree=colsample_bytree,
        subsample=subsample,
        reg_alpha=reg_alpha,
        reg_lambda=reg_lambda,
        min_split_gain=min_split_gain,
        min_child_weight=min_child_weight,
        min_child_samples=min_child_samples,
        model_name=model_name)
    X_test["pred"] = test_pred
    X_test["tar"] = y_test.values
    X_test["score"] = X_test["pred"].apply(prob_to_score)
    # X_test["isNowOverdue"]=isNowOverdue
    ks = cal_ks(X_test, "pred", "tar")
    # ks_advance=cal_ks(X_test,"custom_score","tar")
    score_ks = cal_ks(X_test, "score", "tar")
    print(f"score_ks:{score_ks}")
    print(f"ks:{ks}")
    # print(f"ks_advance:{ks_advance}")
    # clf.save_model("clf.model",num_iteration=clf.best_iteration_)
    # joblib.dump(clf, 'clf.pkl')
    return metrics, test_pred, feature_importance_df, X_test


def XgbClassifer_KFold(
        X,
        y,
        X_test,
        y_test,
        num_folds=5,
        max_depth=None,
        learning_rate=None,
        n_estimators=None,
        gamma=None,
        min_child_weight=None,
        subsample=None,
        colsample_bytree=None,
        reg_alpha=None,
        reg_lambda=None,
        scale_pos_weight=None,
        model_name=None
):
    feature_names = list(X.columns)
    train_scores = []
    valid_scores = []
    test_scores = []
    X_valid_pred = np.zeros(X.shape[0])
    test_pred = np.zeros(X_test.shape[0])
    feature_importance_value = np.zeros(len(feature_names))

    k_fold = KFold(n_splits=num_folds, shuffle=False, random_state=50)

    for n_fold, (train_idx, valid_idx) in enumerate(k_fold.split(X, y)):
        print("continue...", n_fold + 1)
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_valid, y_valid = X.iloc[valid_idx], y.iloc[valid_idx]

        clf = xgb.XGBClassifier(max_depth=max_depth,
                                learning_rate=learning_rate,
                                n_estimators=n_estimators,
                                silent=True,
                                objective='binary:logistic',
                                nthread=-1,
                                gamma=gamma,
                                min_child_weight=min_child_weight,
                                subsample=subsample,
                                colsample_bytree=colsample_bytree,
                                reg_alpha=reg_alpha,
                                reg_lambda=reg_lambda,
                                scale_pos_weight=scale_pos_weight,
                                seed=1024)

        clf.fit(X_train,
                y_train,
                eval_set=[(X_train, y_train), (X_valid, y_valid)],
                eval_metric='auc',
                verbose=200,
                early_stopping_rounds=200)

        test_pred += clf.predict_proba(X_test,
                                       clf.best_iteration)[:, 1] / num_folds
        feature_importance_value += clf.feature_importances_ / num_folds

        # 计算auc值

        valid_auc = clf.best_score
        train_auc = roc_auc_score(
            y_train,
            clf.predict_proba(X_train, clf.best_iteration)[:, 1])
        test_auc = roc_auc_score(y_test, test_pred)

        train_scores.append(train_auc)
        valid_scores.append(valid_auc)
        test_scores.append(test_auc)
        dump_model(clf, f"{model_name}xgb_{n_fold}.pmml")
    feature_importance_df = pd.DataFrame({
        'feature':
            feature_names,
        'importance_value':
            feature_importance_value
    })

    fold_names = np.array(range(num_folds)) + 1

    metrics = pd.DataFrame({
        'num_fold': fold_names,
        'train_auc': train_scores,
        'valid_auc': valid_scores,
        'test_auc': test_scores
    })
    met = dict(metrics.mean())
    met["num_fold"] = "auc_mean"
    met = pd.DataFrame.from_dict(met, orient='index').T
    metrics = pd.concat([metrics, met], axis=0).set_index("num_fold")
    feature_importance_df = feature_importance_df.sort_values(
        by="importance_value", ascending=False)
    return feature_importance_df, metrics, test_pred


def Xgb_Classifer_model(
        train_dt=None,
        vail_dt=None,
        target=None,
        num_folds=5,
        max_depth=4,
        learning_rate=0.1,
        n_estimators=1000,
        gamma=0.5,
        min_child_weight=50,
        subsample=0.7,
        colsample_bytree=0.7,
        reg_alpha=10,
        reg_lambda=20,
        scale_pos_weight=0.5,
        model_name="all_feature"
):
    X_train, X_test, y_train, y_test = split_data(train_dt=train_dt,
                                                  vail_dt=vail_dt,
                                                  target=target)
    feature_importance_df, metrics, test_pred = XgbClassifer_KFold(
        X_train,
        y_train,
        X_test,
        y_test,
        num_folds=num_folds,
        max_depth=max_depth,
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        gamma=gamma,
        min_child_weight=min_child_weight,
        subsample=subsample,
        colsample_bytree=colsample_bytree,
        reg_alpha=reg_alpha,
        reg_lambda=reg_lambda,
        scale_pos_weight=scale_pos_weight,
        model_name=model_name
    )
    X_test["pred"] = test_pred
    X_test["tar"] = y_test.values
    X_test["score"] = X_test["pred"].apply(prob_to_score)
    ks = cal_ks(X_test, "pred", "tar")
    score_ks = cal_ks(X_test, "score", "tar")
    print(f"score_ks:{score_ks}")
    print(f"ks:{ks}")
    return metrics, test_pred, feature_importance_df, X_test


def cale_woe(df1, var, target):
    df = df1.copy()
    # df[var]=df[var].fillna("missing")

    data = df.groupby([var])[target].agg([(
        "count", "count"),
        ("bad", "sum"),
        ("bad_rate", "mean")
    ]).reset_index()
    bad_total = sum(data["bad"])
    data["bad_pcnt"] = data["bad"] / bad_total
    data["good"] = data["count"] - data["bad"]
    data["good_rate"] = 1 - data["bad_rate"]
    good_total = sum(data["good"])
    data["good_pcnt"] = data["good"] / good_total
    data["count_distr"] = data["count"] / df.shape[0]
    data["woe"] = np.log(data["good_pcnt"] / data["bad_pcnt"])
    data["iv"] = (data["good_pcnt"] - data["bad_pcnt"]) * np.log(
        data["good_pcnt"] / data["bad_pcnt"])
    data["iv_sum"] = sum(data["iv"])
    data["lift"] = data["bad_rate"] / df[target].mean()
    data["variable"] = var
    print("{}等于'{}'时最大提升度为{:.2f}".format(
        var, str(data[data["lift"] == data["lift"].max()][var].values[0]),
        data["lift"].max()))
    data = data[[
        "variable", var, 'count', 'bad', 'bad_rate', 'good', 'good_rate',
        'count_distr', 'woe', 'iv', 'iv_sum', 'lift'
    ]]
    return data


def woe_values(df, col, tar):
    woe_data = cale_woe(df, col, tar)

    woe_dict = {x: y for x, y in zip(woe_data[col], woe_data["woe"])}
    return woe_dict


def cale_combi_badrate(data,
                       col,
                       targ,
                       cut=True,
                       original_col=None,
                       sort=True,
                       show_all=False,
                       bins=10):
    if cut:
        data = data.copy()
        col = f"{original_col}_range"
        if len(data[original_col].unique()) > 50:
            data[col] = pd.qcut(data[original_col], bins)
        elif 20 < len(data[original_col].unique()) <= 50:
            data[col] = pd.qcut(data[original_col], bins)
        else:
            data[col] = pd.qcut(data[original_col], bins)
    group = data.groupby([col])[targ].agg([
        ("totle_cnt", "count"),
        ("bad_cnt", "sum"),
        ("bad_rate", "mean")
    ])
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
    group["iv"] = (group["good_pcnt"] - group["bad_pcnt"]) * np.log(
        group["good_pcnt"] / group["bad_pcnt"])
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
            col, 'totle_cnt', 'totle_cnt_cum', 'bad_rate', 'bad_rate_cum',
            'count_distr', 'count_distr_cum', 'woe', 'iv_sum', 'lift', 'ks',
            'ks_max'
        ]]


def woe_mapping(df, tar, woe_col=[], None_target=True, woe_dict_name="woe_dict"):
    if None_target:
        # dump_model(woe_dict,file_name="woe_dict.pkl")
        woe_dict_loan = load_model(f"{woe_dict_name}.pmml")
        for col in woe_dict_loan.keys():
            df[col] = df[col].map(woe_dict_loan[col])
    else:
        woe_dict = {}
        for col in woe_col:
            woe_dict[col] = woe_values(df, col, tar)
        for col in woe_dict.keys():
            df[col] = df[col].map(woe_dict[col])
        dump_model(woe_dict, f"{woe_dict_name}.pmml")
    return df