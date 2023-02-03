import pickle
import json
import mlkits
import lightgbm as lgb
from mlkits.data.dataset import Dataset
from mlkits.utils import init_instance_by_config
import argparse

mlkits.init()

def prepare_lgb_data(dataset, key, reweighter = None):
    if reweighter:
        df = dataset.prepare(key, col_set=dataset.feature_columns + [dataset.label_column, 'weight'])
    else:
        df = dataset.prepare(key, col_set=dataset.feature_columns + [dataset.label_column])
    if df.empty:
        raise ValueError("Empty data from dataset, please check your dataset config.")
    x, y = df[dataset.feature_columns], df[dataset.label_column]
    w = None
    if reweighter:
        w = reweighter.reweight(df)
    return lgb.Dataset(x.values, label=y, weight=w)


def train_and_predict(task):
    model = init_instance_by_config(task['model'])
    
    dataset = init_instance_by_config(task['dataset'])

    train_data = prepare_lgb_data(dataset, 'train')
    valid_data = prepare_lgb_data(dataset, 'valid')
    test_data = dataset.prepare("test", col_set=dataset.feature_columns)
    
    dataset = [(train_data, "train"), (valid_data, "valid")]
    model.fit(dataset)
    
    result = model.predict(test_data)
    
    return model, result


def main():
    parser = argparse.ArgumentParser(description='Predict')

    parser.add_argument('--config_path', type=str, default=None)
    parser.add_argument('--model_path', type=str, default=None)
    parser.add_argument('--output_path', type=str, default=None)

    args = parser.parse_args()

    TASK_CONFIG = {}
    with open(args.config_path, "r") as fp:
        TASK_CONFIG = json.load(fp)

    model, result = train_and_predict(TASK_CONFIG)

    result.to_csv(args.output_path)
    with open(args.model_path, 'wb') as fp:
        pickle.dump(model, fp)


