from copy import deepcopy

import numpy as np
from floodlight import Code
from floodlight.philly.processing.filter import rolling_mode
from scipy.spatial.distance import cdist


def get_closest_player_code(xy, ball, threshold=np.inf):
    """Creates a code object showing for each frame the xID of the player from 'xy'
    that is closest to 'ball'.

    threshold: max distance [m] between player and ball so that he can technically be
    in control."""
    T = len(xy)
    closest_player_xID = np.full(T, np.nan)
    for t in range(T):
        player_to_ball_distances = cdist(
            xy.frame(t=t).reshape(-1, 2),
            ball.frame(t=t).reshape(-1, 2)
        )
        if not np.isnan(player_to_ball_distances).all():
            xID = np.nanargmin(player_to_ball_distances)
            if player_to_ball_distances[xID] <= threshold:
                closest_player_xID[t] = xID

    closest_player_xID = Code(
        code=closest_player_xID,
        name="closest_player",
        framerate=xy.framerate
    )

    return closest_player_xID


def get_individual_possession_code(xy_home, xy_away, ball, possession, filter_data=False):
    """"""
    home_possession = get_closest_player_code(xy_home, ball, threshold=3)
    away_possession = get_closest_player_code(xy_away, ball, threshold=3)

    home_possession[possession != "H"] = np.nan
    away_possession[possession != "A"] = np.nan

    # rolling mode
    if filter_data:
        window_size = (ball.framerate * 2) + 1
        home_possession.code = rolling_mode(home_possession.code, window_size=window_size)
        away_possession.code = rolling_mode(away_possession.code, window_size=window_size)

    return home_possession, away_possession


def get_activity_code(possession, ballstatus):
    """Get code of activity (possession in non-dead phases of play) by combining
    possession and ballstatus codes."""
    activity = deepcopy(possession)
    activity[ballstatus == "D"] = "D"
    activity.name = "activity"
    activity.definitions["D"] = "Dead Ball"

    return activity