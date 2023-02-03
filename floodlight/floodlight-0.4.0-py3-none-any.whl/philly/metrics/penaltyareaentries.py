import pandas as pd
from scipy.spatial.distance import euclidean

from floodlight.philly.processing.possession import get_individual_possession_code
from floodlight.philly.processing.geometry import point_in_zone
from floodlight.philly.processing.events import add_events_into_box, add_video_time
from floodlight.philly.utils.time import gameclock_to_wallclock
from floodlight.philly.param import ZONE_BOUNDARY_TOLERANCE


def dribbles_into_box(
        xy_home, xy_away, ball,
        possession,
        teamsheet_home, teamsheet_away,
        pitch,
        offset
):
    """"""
    # param
    fps = ball.framerate
    teams = ["Home", "Away"]
    N = {"Home": xy_home.N, "Away": xy_away.N}
    xy_data = {
        "Home": xy_home,
        "Away": xy_away,
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
    dribbles_into_box_by_team = {
        team: {
            var: [] for var in ["start", "player_xID", "player_name", "distance"]
        } for team in teams
    }

    # loop: tams
    for team in ["Home", "Away"]:
        for xID in range(N[team]):
            # access player specific sequences and xy data
            individual_possession_sequences = player_possession_sequences[team].get(xID)
            if individual_possession_sequences is None:
                continue
            player_xy = xy_data[team].player(xID)

            for start, end in individual_possession_sequences:
                end = end -1
                distance_dribbled = round(euclidean(player_xy[start], player_xy[end]), 2)
                start_outside_box = not point_in_zone(
                    point=player_xy[start],
                    zone="opp_box",
                    direction=xy_data[team].direction,
                    pitch=pitch,
                )
                end_inside_box = point_in_zone(
                    point=player_xy[end],
                    zone="opp_box",
                    direction=xy_data[team].direction,
                    pitch=pitch,
                    tolerance=ZONE_BOUNDARY_TOLERANCE
                )

                if start_outside_box and end_inside_box:
                    video_time = gameclock_to_wallclock(int(start / fps) + offset)
                    dribbles_into_box_by_team[team]["start"].append(video_time)
                    dribbles_into_box_by_team[team]["player_xID"].append(xID)
                    dribbles_into_box_by_team[team]["player_name"].append(links_xID_player[team][xID])
                    dribbles_into_box_by_team[team]["distance"].append(distance_dribbled)

    return dribbles_into_box_by_team


def passes_into_box(events_home, events_away, teamsheet_home, teamsheet_away, pitch):
    """"""
    # param
    teams = ["Home", "Away"]
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

    # bin
    passes_into_box_by_team = {
        team: {
            var: [] for var in ["start", "player_xID", "player_name"]
        } for team in teams
    }

    # loop
    for team in teams:
        add_events_into_box(events[team], pitch)
        success_pass_into_box = events[team].select(
            conditions=[
                ("eID", 1),
                ("outcome", 1),
                ("into_box", True)
            ]
        )
        success_pass_into_box.reset_index(drop=True, inplace=True)

        for idx in success_pass_into_box.index:
            pID = int(success_pass_into_box.at[idx, "pID"])
            xID = links_pID_xID[team][pID]
            passes_into_box_by_team[team]["start"].append(success_pass_into_box.at[idx, 'video_time'])
            passes_into_box_by_team[team]["player_xID"].append(xID)
            passes_into_box_by_team[team]["player_name"].append(links_xID_player[team][xID])

    return passes_into_box_by_team


offset_ht1 = 526
offset_ht2 = 4375
for events in [home_ht1_event, away_ht1_event]:
    add_video_time(events, offset_ht1)
for events in [home_ht2_event, away_ht2_event]:
    add_video_time(events, offset_ht2)

dib_ht1 = dribbles_into_box(home_ht1_xy, away_ht1_xy, ball_ht1_xy, possession_ht1, teamsheet_home, teamsheet_away, pitch, offset_ht1)
dib_ht2 = dribbles_into_box(home_ht2_xy, away_ht2_xy, ball_ht2_xy, possession_ht2, teamsheet_home, teamsheet_away, pitch, offset_ht2)
home_dib = pd.concat((pd.DataFrame(dib_ht1["Home"]), pd.DataFrame(dib_ht2["Home"]))).sort_values("start")
away_dib = pd.concat((pd.DataFrame(dib_ht1["Away"]), pd.DataFrame(dib_ht2["Away"]))).sort_values("start")
home_dib.to_csv("dribbles_into_box_home.csv")
away_dib.to_csv("dribbles_into_box_away.csv")


pib_ht1 = passes_into_box(home_ht1_event, away_ht1_event, teamsheet_home, teamsheet_away, pitch)
pib_ht2 = passes_into_box(home_ht2_event, away_ht2_event, teamsheet_home, teamsheet_away, pitch)
home_pib = pd.concat((pd.DataFrame(pib_ht1["Home"]), pd.DataFrame(pib_ht2["Home"]))).sort_values("start")
away_pib = pd.concat((pd.DataFrame(pib_ht1["Away"]), pd.DataFrame(pib_ht2["Away"]))).sort_values("start")
home_pib.to_csv("passes_into_box_home.csv")
away_pib.to_csv("passes_into_box_away.csv")




