import numpy as np

from floodlight.io.utils import get_and_convert
from floodlight.philly.processing.geometry import point_in_zone
from floodlight.philly.utils.time import gameclock_to_wallclock
from floodlight.philly.param import ZONE_BOUNDARY_TOLERANCE


def add_event_destinations(events):
    """"""
    events[["to_x", "to_y"]] = np.nan
    for i in events.events.index:
        q = eval(events.events.at[i, "qualifier"])
        events.events.at[i, "to_x"] = get_and_convert(q, 140, float)
        events.events.at[i, "to_y"] = get_and_convert(q, 141, float)


def add_events_into_box(events, pitch):
    """"""
    events["into_box"] = None
    side = events.direction
    for i in events.events.index:
        point_at = (events.events.at[i, "at_x"], events.events.at[i, "at_y"])
        point_to = (events.events.at[i, "to_x"], events.events.at[i, "to_y"])
        in_zone_before = point_in_zone(point_at, "opp_box", side, pitch)
        in_zone_after = point_in_zone(point_to, "opp_box", side, pitch, tolerance=ZONE_BOUNDARY_TOLERANCE)
        events.events.at[i, "into_box"] = not in_zone_before and in_zone_after


def add_player_positions(events, teamsheet):
    events["player_position"] = None
    links = teamsheet.get_links("pID", "position")
    for idx in events.events.index:
        pID = events.events.at[idx, "pID"]
        if not np.isnan(pID):
            events.events.at[idx, "player_position"] = links[int(pID)]


def add_subsequent_event(events):
    events["subseq_eID"] = None
    events["subseq_pID"] = None
    for idx in events.events.index:
        try:
            eID = int(events.events.at[idx + 1, "eID"])
        except:
            eID = None
        events.events.at[idx, "subseq_eID"] = eID
        try:
            pID = int(events.events.at[idx + 1, "pID"])
        except:
            pID = None
        events.events.at[idx, "subseq_pID"] = pID


def add_video_time(events, offset):
    events["video_time"] = None
    for idx in events.events.index:
        vtime = gameclock_to_wallclock(events.events.at[idx, "gameclock"] + offset)
        events.events.at[idx, "video_time"] = vtime
