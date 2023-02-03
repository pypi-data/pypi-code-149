import numpy as np
import pandas as pd

from floodlight.philly.processing.possession import get_individual_possession_code
from floodlight.philly.processing.geometry import number_of_players_between_point_and_goal, vector_in_zone
from floodlight.philly.processing.events import add_video_time
from floodlight.philly.utils.opta_definitions import opta_keys
from floodlight.philly.param import POSSESSION_SEARCH_RANGE_MIN, POSSESSION_SEARCH_RANGE_MAX, MINIMAL_FORWARD_FIRST_DRIBBLE_DISTANCE


def forwardfirsttransitions(
        xy_home, xy_away, ball,
        events_home, events_away,
        possession,
        teamsheet_home, teamsheet_away,
    ):
    """"""
    # param
    fps = ball.framerate
    teams = ["Home", "Away"]
    switch_link = {"Home": "Away", "Away": "Home"}
    xy_data = {
        "Home": xy_home,
        "Away": xy_away,
    }
    events = {
        "Home": events_home,
        "Away": events_away,
    }
    links_xID_player = {
        "Home": teamsheet_home.get_links("xID", "player"),
        "Away": teamsheet_away.get_links("xID", "player")
    }
    links_pID_xID = {
        "Home": teamsheet_home.get_links("pID", "xID"),
        "Away": teamsheet_away.get_links("pID", "xID")
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
        "Home": home_possession.find_sequences(return_type="list"),
        "Away": away_possession.find_sequences(return_type="list")
    }

    # bin
    forward_first_by_team = {
        team: {
            var: [] for var in [
                "start", "initial_action", "next_action",
                "player_xID", "player_name", "carried", "bypassed",
            ]
        } for team in teams
    }

    # loop: tams
    for team in ["Home", "Away"]:
        # identify legitimate events initializing transitions
        tackles = events[team].select(conditions=[("eID", 7), ("outcome", 1)])
        interceptions = events[team].select(conditions=(("eID", 8)))
        recoveries = events[team].select(conditions=(("eID", 49)))
        transition_events = pd.concat([tackles, interceptions, recoveries])
        transition_events.sort_values("gameclock", inplace=True)

        # loop
        for idx in transition_events.index:
            # param
            IS_FORWARD_FIRST_TRANSITION = False
            trans_event_name = opta_keys.get(transition_events.at[idx, "eID"], "Unknown event")
            type_of_continutation = None

            # catch case if no subsequent event exists (index out of bounds)
            if idx+1 > events[team].events.last_valid_index():
                continue
            else:
                subsequent_event = events[team].events.iloc[idx + 1]

            # CHECK: subsequent forward pass
            if subsequent_event["eID"] == 1 and subsequent_event["outcome"] == 1:
                if vector_in_zone(
                        at=(subsequent_event["at_x"], subsequent_event["at_y"]),
                        to=(subsequent_event["to_x"], subsequent_event["to_y"]),
                        zone="strictly_forward",
                        direction=events[team].direction
                ):
                    IS_FORWARD_FIRST_TRANSITION = True
                    type_of_continutation = "forward pass"

            # CHECK: subsequent forward dribble
            else:
                # determine possessions after transition
                transition_frame = transition_events.at[idx, "frameclock"]
                possession_sequence_range = range(
                    transition_frame - fps * POSSESSION_SEARCH_RANGE_MIN,
                    transition_frame + fps * POSSESSION_SEARCH_RANGE_MAX
                )
                transition_possessions = [
                    seq for seq in player_possession_sequences[team] if seq[0] in possession_sequence_range
                ]
                # break if none found
                if len(transition_possessions) == 0:
                    continue
                # else examine the first
                start, end, dribble_xID = transition_possessions[0]
                player_xy = xy_data[team].player(int(dribble_xID))
                # CHECK: dribble at least some yards forward
                distance_dribbled = player_xy[end][0] - player_xy[start][0]
                if xy_data[team].direction == "lr":
                    if distance_dribbled < MINIMAL_FORWARD_FIRST_DRIBBLE_DISTANCE:
                        continue
                elif xy_data[team].direction == "rl":
                    if (-1 * distance_dribbled) < MINIMAL_FORWARD_FIRST_DRIBBLE_DISTANCE:
                        continue
                # Check: eliminate at least 1 defender
                defending_start = number_of_players_between_point_and_goal(
                    xy=xy_data[switch_link[team]], ball=ball, t=start
                )
                defending_end = number_of_players_between_point_and_goal(
                    xy=xy_data[switch_link[team]], ball=ball, t=end
                )
                bypassed = defending_start - defending_end
                if bypassed < 1:
                    continue
                # if all checks have passed:
                IS_FORWARD_FIRST_TRANSITION = True
                type_of_continutation = f"dribble"

            # record transition if detected
            if IS_FORWARD_FIRST_TRANSITION:
                forward_first_by_team[team]["start"].append(transition_events.at[idx, 'video_time'])
                forward_first_by_team[team]["initial_action"].append(trans_event_name)
                forward_first_by_team[team]["next_action"].append(type_of_continutation)
                if type_of_continutation == "forward pass":
                    pID = int(subsequent_event["pID"])
                    xID = links_pID_xID[team][pID]
                    forward_first_by_team[team]["player_xID"].append(xID)
                    forward_first_by_team[team]["player_name"].append(links_xID_player[team][xID])
                    forward_first_by_team[team]["carried"].append("")
                    forward_first_by_team[team]["bypassed"].append("")
                elif type_of_continutation == "dribble":
                    xID = dribble_xID
                    forward_first_by_team[team]["player_xID"].append(xID)
                    forward_first_by_team[team]["player_name"].append(links_xID_player[team][xID])
                    forward_first_by_team[team]["carried"].append(f"{abs(round(distance_dribbled, 2))} m")
                    forward_first_by_team[team]["bypassed"].append(bypassed)

    return forward_first_by_team


offset_ht1 = 526
offset_ht2 = 4375
for events in [home_ht1_event, away_ht1_event]:
    add_video_time(events, offset_ht1)
for events in [home_ht2_event, away_ht2_event]:
    add_video_time(events, offset_ht2)

fft_ht1 = forwardfirsttransitions(
    home_ht1_xy, away_ht1_xy, ball_ht1_xy,
    home_ht1_event, away_ht1_event, possession_ht1, teamsheet_home, teamsheet_away)
fft_ht2 = forwardfirsttransitions(
    home_ht2_xy, away_ht2_xy, ball_ht2_xy,
    home_ht2_event, away_ht2_event, possession_ht2, teamsheet_home, teamsheet_away)

# save
home_fft = pd.concat((pd.DataFrame(fft_ht1["Home"]), pd.DataFrame(fft_ht2["Home"])))
away_fft = pd.concat((pd.DataFrame(fft_ht1["Away"]), pd.DataFrame(fft_ht2["Away"])))
home_fft.to_csv("forward_first_home.csv")
away_fft.to_csv("forward_first_away.csv")





