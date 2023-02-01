import os
import ruamel.yaml as yaml


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def readYaml(path):
    Config = {}
    with open(path,encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if data:
            Config.update(data)
    return Config


def writeYaml(path, data=None):
    if not os.path.isfile(path):
        with open(path, mode="w",encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, Dumper=yaml.RoundTripDumper)


def addComments(path, comments):
    with open(path,encoding='utf-8') as f:
        Config = yaml.round_trip_load(f)
    comments(Config)
    with open(path, mode="w",encoding='utf-8') as f:
        yaml.round_trip_dump(Config, f, allow_unicode=True)
