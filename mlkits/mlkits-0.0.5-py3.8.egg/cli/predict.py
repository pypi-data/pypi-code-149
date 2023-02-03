import os
import gc
import json
import mlkits
import pickle
import pandas as pd
from mlkits.utils import init_instance_by_config
import argparse

mlkits.init()

def main():
    parser = argparse.ArgumentParser(description='Predict')

    parser.add_argument('--config_path', type=str, default=None)
    parser.add_argument('--model_path', type=str, default=None)
    parser.add_argument('--data_path', type=str, default=None)
    parser.add_argument('--output_path', type=str, default=None)

    args = parser.parse_args()

    with open(args.model_path, 'rb') as fp:
        model = pickle.load(fp)

    TASK_CONFIG = {}
    with open(args.config_path, "r") as fp:
        TASK_CONFIG = json.load(fp)

    TASK_CONFIG_DATASET_SPLITS = TASK_CONFIG['dataset']['kwargs']['handler']['kwargs']['data_loader']['kwargs']['config']['splits']
    TASK_CONFIG_DATASET_SPLITS['test']['path'] = args.data_path
    del_keys = [k for k in TASK_CONFIG_DATASET_SPLITS if k != 'test']
    for k in del_keys:
        del TASK_CONFIG_DATASET_SPLITS[k]

    dataset = init_instance_by_config(TASK_CONFIG['dataset'])
    test_data = dataset.prepare("test", col_set=dataset.feature_columns)
    result = model.predict(test_data)
    result.to_csv(args.output_path)

