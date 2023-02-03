import json

import pandas as pd

from floodlight.io.utils import get_and_convert
from floodlight.io.secondspectrum import _get_position_precedence


filepath_metadata = "C:\\Users\\Lenovo\\draabe\\repositories\\philadelphiaunion\\data\\PHI-CIN_Metadata.json"

# read file
with open(str(filepath_metadata), "r") as f:
    metajson = json.load(f)

# bin
teamsheets = {team: None for team in ["Home", "Away"]}

# loop through teams
key_map = {"Home": "homePlayers", "Away": "awayPlayers"}
for team in ["Home", "Away"]:
    # bin
    teamsheet = {
        column: [] for column in ["precedence", "player", "jID", "pID", "position"]
    }
    # query team player list
    player_list = metajson[key_map[team]]
    # add players to list
    for player in player_list:
        # query
        name = get_and_convert(player, "name", str)
        position = get_and_convert(player, "position", str)
        jID = get_and_convert(player, "number", int)
        pID = get_and_convert(player, "optaId", int)
        precedence = _get_position_precedence(position)
        # assign
        teamsheet["player"].append(name)
        teamsheet["position"].append(position)
        teamsheet["jID"].append(jID)
        teamsheet["pID"].append(pID)
        teamsheet["precedence"].append(precedence)
    # curate
    teamsheet = pd.DataFrame(teamsheet)
    teamsheet.sort_values("precedence", inplace=True)
    teamsheet.drop(["precedence"], axis=1, inplace=True)
    teamsheet.reset_index(drop=True, inplace=True)
    teamsheets[team] = teamsheet


