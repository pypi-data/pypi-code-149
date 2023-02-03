import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean

from floodlight.philly.processing.possession import get_individual_possession_code
from floodlight.philly.processing.geometry import number_of_players_between_point_and_goal, point_in_zone
from floodlight.philly.utils.time import gameclock_to_wallclock
from floodlight.philly.param import MINIMAL_CB_CARRY_DRIBBLE_DISTANCE as THRESHOLD


def centerback_carries(xy_home, xy_away, ball,
                       events_home, events_away,
                       possession,
                       teamsheet_home, teamsheet_away,
                       pitch,
                       offset
    ):
    """"""
    # param
    fps = ball.framerate
    T = len(ball)
    teams = ["Home", "Away"]
    switch_link = {"Home": "Away", "Away": "Home"}
    N = {"Home": xy_home.N, "Away": xy_away.N}
    xy_data = {
        "Home": xy_home,
        "Away": xy_away,
    }
    events = {
        "Home": events_home,
        "Away": events_away,
    }
    links_xID_pID = {
        "Home": teamsheet_home.get_links("xID", "pID"),
        "Away": teamsheet_away.get_links("xID", "pID")
    }
    links_xID_position = {
        "Home": teamsheet_home.get_links("xID", "position"),
        "Away": teamsheet_away.get_links("xID", "position")
    }
    links_xID_player = {
        "Home": teamsheet_home.get_links("xID", "player"),
        "Away": teamsheet_away.get_links("xID", "player")
    }

    # get possessions
    home_possession, away_possession = get_individual_possession_code(
        xy_home=xy_home,
        xy_away=xy_away,
        ball=ball,
        possession=possession,
        filter_data=True
    )
    player_possession_sequences = {
        "Home": home_possession.find_sequences(return_type="dict"),
        "Away": away_possession.find_sequences(return_type="dict")
    }

    # bin
    centerback_carries_by_team = {
        team: {
            var: [] for var in ["player_name", "start", "end", "player_xID", "carried", "bypassed", "next action"]
        } for team in teams
    }

    # loop: tams
    for team in ["Home", "Away"]:
        # loop: players
        for xID in range(N[team]):
            # skip non-CBs
            if links_xID_position[team][xID] not in ["CB", "RCB", "LCB"]:
                continue
            pID = links_xID_pID[team][xID]

            # access player specific sequences and xy data
            individual_possession_sequences = player_possession_sequences[team].get(xID)
            if individual_possession_sequences is None:
                continue
            player_xy = xy_data[team].player(xID)

            for start, end in individual_possession_sequences:
                # Check: Dribble 10+ yards
                # distance_dribbled = euclidean(player_xy[start], player_xy[end])
                # if distance_dribbled < THRESHOLD:
                #     continue
                # Check: Advance Ball 10+ yards up the field
                distance_dribbled = player_xy[end][0] - player_xy[start][0]
                if xy_data[team].direction == "lr":
                    if distance_dribbled < THRESHOLD:
                        continue
                elif xy_data[team].direction == "rl":
                    if (-1 * distance_dribbled) < THRESHOLD:
                        continue

                # Check: Touch Endzone
                final_touch_in_attacking_third = point_in_zone(
                    point=player_xy[end],
                    zone="attacking_third",
                    direction=xy_data[team].direction,
                    pitch=pitch
                )
                final_touch_in_middle_third = point_in_zone(
                    point=player_xy[end],
                    zone="middle_third",
                    direction=xy_data[team].direction,
                    pitch=pitch
                )
                if not (final_touch_in_middle_third or final_touch_in_attacking_third):
                    continue

                # Check: Eliminate at least 1 defender
                defending_start = number_of_players_between_point_and_goal(
                    xy=xy_data[switch_link[team]], ball=ball, t=start
                )
                defending_end = number_of_players_between_point_and_goal(
                    xy=xy_data[switch_link[team]], ball=ball, t=end
                )
                bypassed = defending_start - defending_end
                if bypassed < 1:
                    continue

                # Check: Legitimate Next Action
                search_horizon_start = start - 2 * fps
                search_horizon_end = end + 3 * fps
                eligible_events = events[team].select(
                    conditions=[
                        ("frameclock", (search_horizon_start, search_horizon_end)),
                        ("pID", pID)
                    ]
                )
                if eligible_events.empty:
                    continue
                eligible_event_occured = False
                next_action = None
                idxs = list(eligible_events.index)
                idxs.reverse()
                # loop backwards through eligible events and determine if "good" next action
                for idx in idxs:
                    event = eligible_events.loc[idx]
                    # completed pass: forward or key pass
                    if int(event["eID"]) == 1 and int(event["outcome"]) == 1:
                        if events[team].direction == 'lr':
                            if event["at_x"] < event["to_x"]:
                                eligible_event_occured = True
                                next_action = event["eID"]
                        elif events[team].direction == 'rl':
                            if event["at_x"] > event["to_x"]:
                                eligible_event_occured = True
                                next_action = event["eID"]
                        if eval(event["qualifier"]).get(210) is not None:
                            eligible_event_occured = True
                    # foul suffered, out of play, corner, miss, post, saved attempt, goal
                    elif int(event["eID"]) in [4, 5, 6, 13, 14, 15, 16, 4]:
                        eligible_event_occured = True
                        next_action = event["eID"]

                if not eligible_event_occured:
                    continue

                # All checks passed: Save details
                wallclock_start = gameclock_to_wallclock(round(start / fps + offset, 2))
                wallclock_end = gameclock_to_wallclock(round(end / fps + offset, 2))
                centerback_carries_by_team[team]["player_name"].append(links_xID_player[team][xID])
                centerback_carries_by_team[team]["start"].append(wallclock_start)
                centerback_carries_by_team[team]["end"].append(wallclock_end)
                centerback_carries_by_team[team]["player_xID"].append(xID)
                centerback_carries_by_team[team]["carried"].append(distance_dribbled)
                centerback_carries_by_team[team]["bypassed"].append(bypassed)
                centerback_carries_by_team[team]["next action"].append(next_action)

    return centerback_carries_by_team


# duration = round((end - start) / fps, 2)
# offset = 526
# start = round(start / fps + offset, 2)
# end = round(end / fps + offset, 2)
# print(f"Possession: "
#       f"{gameclock_to_wallclock(start)} - "
#       f"{gameclock_to_wallclock(end)} "
#       f"({duration} s)")

offset_ht1 = 526
cbcarry_ht1 = centerback_carries(
    home_ht1_xy, away_ht1_xy, ball_ht1_xy,
    home_ht1_event, away_ht1_event, possession_ht1, teamsheet_home, teamsheet_away, pitch, offset_ht1)
offset_ht2 = 4375
cbcarry_ht2 = centerback_carries(
    home_ht2_xy, away_ht2_xy, ball_ht2_xy,
    home_ht2_event, away_ht2_event, possession_ht2, teamsheet_home, teamsheet_away, pitch, offset_ht2)

# home
home_carries = pd.concat((pd.DataFrame(cbcarry_ht1["Home"]), pd.DataFrame(cbcarry_ht2["Home"])))
away_carries = pd.concat((pd.DataFrame(cbcarry_ht1["Away"]), pd.DataFrame(cbcarry_ht2["Away"])))
home_carries.to_csv("cb_carries_home_10yds_dribble.csv")
away_carries.to_csv("cb_carries_away_10yds_dribble.csv")
