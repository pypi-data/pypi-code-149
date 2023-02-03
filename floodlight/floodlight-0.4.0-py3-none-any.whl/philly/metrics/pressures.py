import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist

from floodlight import XY, Code

from floodlight.philly.processing.geometry import point_in_zone
from floodlight.philly.processing.possession import get_activity_code, get_individual_possession_code
from floodlight.philly.utils.time import gameclock_to_wallclock
from floodlight.philly.param import PRESSURE_TIME_THRESHOLD, PRESSURE_DISTANCE_THRESHOLD, COUNTEPRESSURE_TIME_THRESHOLD


def calc_pressure_metrics(
        xy_home: XY,
        xy_away,
        ball,
        possession,
        ballstatus,
        teamsheet_home,
        teamsheet_away,
        pitch,
        offset
):
    """"""
    # param
    fps = xy_home.framerate
    T = len(xy_home)
    teams = ["Home", "Away"]
    switch_link = {"Home": "Away", "Away": "Home"}
    N = {"Home": xy_home.N, "Away": xy_away.N}
    links_xID_player = {
        "Home": teamsheet_home.get_links("xID", "player"),
        "Away": teamsheet_away.get_links("xID", "player")
    }

    # bin
    pressing_players = {team: np.full(T, np.nan) for team in teams}
    pressures_by_player = {team: np.zeros(N[team]) for team in teams}
    pressures_successful_by_player = {team: np.zeros(N[team]) for team in teams}
    counterpressures_by_player = {team: np.zeros(N[team]) for team in teams}
    counterpressures_successful_by_player = {team: np.zeros(N[team]) for team in teams}
    pressures_by_team = {
        team: {
            var: [] for var in ["player_name", "start", "end", "success", "counter", "player_xID"]
        } for team in teams
    }

    # step 1: find all turnovers for both teams
    activity = get_activity_code(possession, ballstatus)
    all_possession_sequences = activity.find_sequences()
    turnovers = {
        team: [end for (_, end) in all_possession_sequences[team[0]]]
        for team in teams
    }

    # step 2: find player possession sequences
    home_closest, away_closest = get_individual_possession_code(
        xy_home,
        xy_away,
        ball,
        possession,
        filter_data=True
    )
    player_possession_sequences = {
        "Home": home_closest.find_sequences(return_type="list"),
        "Away": away_closest.find_sequences(return_type="list")
    }

    # loop: teams
    for team in teams:
        # re-assign xy data based on role
        if team == "Home":
            xy_attackers = xy_away
            xy_defenders = xy_home
        elif team == "Away":
            xy_attackers = xy_home
            xy_defenders = xy_away

        # step 3: find all pressure sequences of individual players
        # loop: individual possession sequences
        for start, end, possessing_player_xID in player_possession_sequences[
            switch_link[team]
        ]:

            # loop: frames in sequence
            for t in range(start, end):

                # CHECK: ball in attacking half
                if not point_in_zone(
                    point=ball[t],
                    zone="attacking_half",
                    direction=xy_defenders.direction,
                    pitch=pitch,
                    tolerance=0
                ):
                    continue

                # determine distances of defenders to player in possession
                points_player_in_possession = xy_attackers.player(
                    int(possessing_player_xID)
                )[t].reshape(-1, 2)
                points_players_defending = xy_defenders.frame(t).reshape(-1, 2)
                distances = cdist(points_player_in_possession, points_players_defending)
                # CHECK: pressure moment
                if (distances < PRESSURE_DISTANCE_THRESHOLD).any():
                    pressing_player_xID = np.nanargmin(distances)
                    pressing_players[team][t] = pressing_player_xID

        pressing_players_code = Code(
            pressing_players[team],
            name="pressing_players",
            framerate=activity.framerate
        )
        pressing_sequences = pressing_players_code.find_sequences()

        # step 4: evaluate individual pressure sequences (count, success, counterpressure)
        # loop through players
        for p in range(N[team]):
            player_pressing_sequences = pressing_sequences.get(p)
            if player_pressing_sequences is None:
                continue
            pressures_by_player[team][p] = len(player_pressing_sequences)

            # loop through individual pressure sequences
            for start, end in player_pressing_sequences:
                # flags
                IS_SUCCESSFUL = False
                IS_COUNTERPRESSURE = False

                # define ranges for pressures and counterpressures
                pressure_range = range(end, end + fps * PRESSURE_TIME_THRESHOLD)
                counterpressure_range = range(
                    start - fps * COUNTEPRESSURE_TIME_THRESHOLD,
                    start
                )

                # CHECK SUCCESS: any turnover occured in time range
                turnovers_in_pressure_range = [
                    turnover in pressure_range for turnover in turnovers[switch_link[team]]
                ]
                if sum(turnovers_in_pressure_range) > 0:
                    IS_SUCCESSFUL = True
                    pressures_successful_by_player[team][p] += 1

                # CHECK COUNTERPRESSURE: any giveaway occured in time range
                turnovers_in_countepressure_range = [
                    turnover in counterpressure_range for turnover in turnovers[team]
                ]
                if sum(turnovers_in_countepressure_range) > 0:
                    IS_COUNTERPRESSURE = True
                    counterpressures_by_player[team][p] += 1
                    if IS_SUCCESSFUL:
                        counterpressures_successful_by_player[team][p] += 1

                wallclock_start = gameclock_to_wallclock(round(start / fps + offset, 2))
                wallclock_end = gameclock_to_wallclock(round(end / fps + offset, 2))
                pressures_by_team[team]["player_name"].append(links_xID_player[team][int(p)])
                pressures_by_team[team]["start"].append(wallclock_start)
                pressures_by_team[team]["end"].append(wallclock_end)
                pressures_by_team[team]["success"].append(IS_SUCCESSFUL)
                pressures_by_team[team]["counter"].append(IS_COUNTERPRESSURE)
                pressures_by_team[team]["player_xID"].append(int(p))

    return pressures_by_team


offset_ht1 = 526
pressures_ht1 = calc_pressure_metrics(
    home_ht1_xy, away_ht1_xy, ball_ht1_xy,
    possession_ht1, ballstatus_ht1,
    teamsheet_home, teamsheet_away, pitch, offset_ht1
)
offset_ht2 = 4375
pressures_ht2 = calc_pressure_metrics(
    home_ht2_xy, away_ht2_xy, ball_ht2_xy,
    possession_ht2, ballstatus_ht2,
    teamsheet_home, teamsheet_away, pitch, offset_ht2
)

home_pressures = pd.concat((pd.DataFrame(pressures_ht1["Home"]), pd.DataFrame(pressures_ht2["Home"])))
away_pressures = pd.concat((pd.DataFrame(pressures_ht1["Away"]), pd.DataFrame(pressures_ht2["Away"])))
home_pressures.sort_values(["player_xID", "start"], inplace=True, ascending=True)
away_pressures.sort_values(["player_xID", "start"], inplace=True, ascending=True)
home_pressures.to_csv("pressures_home.csv")
away_pressures.to_csv("pressures_away.csv")


# home_pressures = pd.DataFrame(pressures_by_team["Home"])
# away_pressures = pd.DataFrame(pressures_by_team["Away"])
# home_name_links = home_teamsheet.get_links("xID", "player")
# away_name_links = away_teamsheet.get_links("xID", "player")
# duration = round((end - start) / fps, 2)
# offset = 526
# start = round(start / fps + offset, 2)
#
# for idx in home_pressures.index:
#     start, end = home_pressures.at[idx, "start"], home_pressures.at[idx, "end"]
#     start = round(start / fps + offset, 2)
#     end = round(end / fps + offset, 2)
#     event = "Counterpressure" if home_pressures.at[idx, "counter"] else "       Pressure"
#     success = "  Successful" if home_pressures.at[idx, "counter"] else "Unsuccessful"
#     player = home_name_links[home_pressures.at[idx, "player_xID"]]
#     print(f"{event} | "
#           f"{gameclock_to_wallclock(start)} - "
#           f"{gameclock_to_wallclock(end)} "
#           f"({duration} s) | "
#           f"{success} | "
#           f"by {player}"
#           )
