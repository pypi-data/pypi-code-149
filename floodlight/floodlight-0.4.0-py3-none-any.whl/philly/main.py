from floodlight.io.secondspectrum import read_secspec_files, read_secspec_insight
from floodlight.philly.processing.events import add_event_destinations

from floodlight.philly.processing.sync import align_data

filepath_tracking = "C:\\Users\\Lenovo\\draabe\\repositories\\philadelphiaunion\\data\\PHI-CIN_Data.jsonl"
filepath_insights = "C:\\Users\\Lenovo\\draabe\\repositories\\philadelphiaunion\\data\\PHI-CIN_Insight.jsonl"
filepath_metadata = "C:\\Users\\Lenovo\\draabe\\repositories\\philadelphiaunion\\data\\PHI-CIN_Metadata.json"


(
    home_ht1_event,
    home_ht2_event,
    away_ht1_event,
    away_ht2_event,
    pitch_event
) = read_secspec_insight(filepath_insights, filepath_metadata)
events = home_ht1_event

(
    home_ht1_xy,
    home_ht2_xy,
    away_ht1_xy,
    away_ht2_xy,
    ball_ht1_xy,
    ball_ht2_xy,
    teamsheet_home,
    teamsheet_away,
    possession_ht1,
    possession_ht2,
    ballstatus_ht1,
    ballstatus_ht2,
    pitch
) = read_secspec_files(filepath_tracking, filepath_metadata)

# events pre-processing
for events in [home_ht2_event, away_ht1_event, away_ht2_event, home_ht1_event]:
    add_event_destinations(events)
    align_data(events, pitch_event)
    events.add_frameclock(home_ht1_xy.framerate)


ball = ball_ht1_xy
xy_home = home_ht1_xy
xy_away = away_ht1_xy
events_home = home_ht1_event
events_away = away_ht1_event
possession = possession_ht1
ballstatus = ballstatus_ht1

# events processing
# for events in [home_ht2_event, away_ht1_event, away_ht2_event, home_ht1_event]:
#     add_events_into_box(events, pitch_xy)

