import json
import zipfile
from tqdm import tqdm
import glob
import os

from SoccerNet.utils import getListGames
from SoccerNet.Evaluation.utils import LoadJsonFromZip

import numpy as np


def evaluate(SoccerNet_path, Predictions_path, prediction_file="results_caption.json", label_files="Labels-caption.json", split="test"):
    # evaluate the prediction with respect to some ground truth
    # Params:
    #   - SoccerNet_path: path for labels (folder or zipped file)
    #   - Predictions_path: path for predictions (folder or zipped file)
    #   - prediction_file: name of the predicted files - if set to None, try to infer it
    #   - label_files: name of the label files - by default "Labels-cpation.json"
    #   - split: split to evaluate from ["test", "challenge"]
    # Return:
    #   - dictionary of metrics

    list_games = getListGames(split=split, task="caption")

    for game in tqdm(list_games):

        # load labels
        if zipfile.is_zipfile(SoccerNet_path):
            labels = LoadJsonFromZip(
                SoccerNet_path, os.path.join(game, label_files))
        else:
            labels = json.load(
                open(os.path.join(SoccerNet_path, game, label_files)))
                

        # infer name of the prediction_file
        if prediction_file == None:
            if zipfile.is_zipfile(Predictions_path):
                with zipfile.ZipFile(Predictions_path, "r") as z:
                    for filename in z.namelist():
                        #       print(filename)
                        if filename.endswith(".json"):
                            prediction_file = os.path.basename(filename)
                            break
            else:
                for filename in glob.glob(os.path.join(Predictions_path, "*/*/*/*.json")):
                    prediction_file = os.path.basename(filename)
                    # print(prediction_file)
                    break

        # Load predictions
        if zipfile.is_zipfile(Predictions_path):
            predictions = LoadJsonFromZip(
                Predictions_path, os.path.join(game, prediction_file))
        else:
            predictions = json.load(
                open(os.path.join(Predictions_path, game, prediction_file)))

        # compute metrics
        # TODO: compute metrics

    # aggregate metrics per game
    # TODO: compute metrics
    metricA = 0.5
    metricB = 0.5
    metricC = 0.5

    results = {
        "metricA": metricA,
        "metricB": metricB,
        "metricC": metricC,
    }
    return results
