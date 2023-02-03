# from floodlight.io.datasets import StatsBombOpenDataset
# from floodlight.io.dfl import read_event_data_xml, read_position_data_xml
# from floodlight.io.opta import read_event_data_xml
# from floodlight.io.secondspectrum import read_teamsheets_from_meta_json, read_event_data_jsonl, read_position_data_jsonl
# from floodlight.io.sportradar import read_event_data_json
# from floodlight.io.statsbomb import read_open_event_data_json, read_teamsheets_from_open_event_data_json
# from floodlight.io.tracab import read_position_data_dat, read_teamsheets_from_dat, read_teamsheets_from_meta_json

# # DFL
# dfl_data_path = "C:\\Users\\Lenovo\\draabe\\repositories\\floodlight\\data\\DFL\\"
# dfl_matchinfo_path = dfl_data_path + "DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-0025CU.xml"
# dfl_events_path = dfl_data_path + "DFL_03_02_events_raw_DFL-COM-000001_DFL-MAT-0025CU.xml"
# dfl_positions_path = dfl_data_path + "DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-0025CU.xml"
#
# event_objects, teamsheets, pitch = read_event_data_xml(dfl_events_path, dfl_matchinfo_path)
# xydata, possession, ballstatus, teamsheets, pitch = read_position_data_xml(dfl_positions_path, dfl_matchinfo_path)

# # Opta
# f24_path = "C:\\Users\\Lenovo\\sciebo\\floodlight\\Opta\\f24-4-2017-958085-eventdetails.xml"
# event_objects, pitch = read_event_data_xml(f24_path)

# # Second Spectrum
# secspec_data_path = "C:\\Users\\Lenovo\\draabe\\data\\secspecsample\\"
# secspec_metajson = secspec_data_path + "g2261165_SecondSpectrum_meta.json"
# secspec_positions = secspec_data_path + "g2261165_SecondSpectrum_tracking-produced.jsonl"
# secspec_insight_path = "C:\\Users\\Lenovo\\draabe\\repositories\\philadelphiaunion\\data\\PHI-CIN_Insight.jsonl"
# secspec_insight_meta_path = "C:\\Users\\Lenovo\\draabe\\repositories\\philadelphiaunion\\data\\PHI-CIN_Metadata.json"
#
# teamsheets = read_teamsheets_from_meta_json(secspec_insight_meta_path)
# event_objects, pitch = read_event_data_jsonl(secspec_insight_path, secspec_insight_meta_path)
# xydata, possession, ballstatus, teamsheets, pitch = read_position_data_jsonl(secspec_positions, secspec_metajson)

# # Sportradar
# sportradar_filepath = "C:\\Users\\Lenovo\\sciebo\\floodlight\\Sportradar\\sport_events_28449852_timeline.json"
# events_objects = read_event_data_json(sportradar_filepath)

# # StatsBomb
# statsbomb_filepath_events = ".data\\statsbomb_dataset\\events\\2302764.json"
# statsbomb_filepath_match = ".data\\statsbomb_dataset\\matches\\16\\37.json"
# teamsheets = read_teamsheets_from_open_event_data_json(
#     statsbomb_filepath_events, statsbomb_filepath_match
# )
# event_objects, teamsheets = read_open_event_data_json(statsbomb_filepath_events, statsbomb_filepath_match)

# # StatsBomb Dataset
# dataset = StatsBombOpenDataset()
# events, teamsheets = dataset.get("UEFA Euro", "2020", "England vs. Germany")
# pitch = dataset.get_pitch()
# # matches = dataset.available_matches
# # clasicos = matches[matches["match_name"] == "Barcelona vs. Real Madrid"]
# # for _, match in clasicos.iterrows():
# #     print(f"Season {match['season_name']} - Barcelona {match['score']} Real'")
# # clasico_events = []
# # for _, clasico in clasicos.iterrows():
# #     data = dataset.get("La Liga", clasico["season_name"], clasico["match_name"])
# #     clasico_events.append(data)

# TRACAB
# tracab_dat_json_case = "C:\\Users\\Lenovo\\draabe\\union analytics\\data samples\\Sample Data Tracab\\2022-08-22_SKC-POR.dat"
# tracab_meta_json_case = "C:\\Users\\Lenovo\\draabe\\union analytics\\data samples\\Sample Data Tracab\\2022-08-22_SKC-POR_metadata.json"
tracab_dat_xml_case = "C:\\Users\\Lenovo\\draabe\\repositories\\floodlight\\data\\1040191\\1040191.dat"
tracab_meta_xml_case = "C:\\Users\\Lenovo\\draabe\\repositories\\floodlight\\data\\1040191\\1040191_metadata.xml"

teamsheets = read_teamsheets_from_dat(tracab_dat_xml_case)
xydata, possession, ballstatus, teamsheets, pitch = read_position_data_dat(tracab_dat_xml_case, tracab_meta_xml_case)
# teamsheets = read_teamsheets_from_meta_json(tracab_meta_json_case)
# xydata, possession, ballstatus, teamsheets, pitch = read_position_data_dat(tracab_dat_json_case, tracab_meta_json_case, teamsheet_home=teamsheets["Home"])
xy = xydata["HT1"]["Home"]

from matplotlib import pyplot as plt

fig, ax = plt.subplots()
pitch.plot(ax=ax)
xy.plot(t=(0, 1000), plot_type="trajectories", ax=ax)

# # Kinexon
# sample_kinexon_path = "C:\\Users\\Lenovo\\sciebo\\floodlight\\Kinexon\\Game 1.csv"
# sampe_sportradar_path = "C:\\Users\\Lenovo\\sciebo\\floodlight\\Sportradar\\sport_events_28449852_timeline.json"





