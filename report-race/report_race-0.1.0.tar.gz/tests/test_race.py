"""Tests for Race class.

This module have tests for Race class and it's methods.

Functions:
"""
from datetime import datetime
from dataclasses import dataclass, field
from unittest.mock import patch, mock_open
import pytest

from report.race import Race


def test_init_race_without_argument():
    with pytest.raises(TypeError):
        r = Race()


@pytest.mark.parametrize("err, arg", [
    (UserWarning, {"abbreviations": "file"}),
    (UserWarning, {"one": "path/to/abbreviations.txt",
                   "two": "path/to/start.log",
                   "three": "path/to/end.log"}),
    (UserWarning, {"abbreviations": "path/to/abbr.txt",
                   "start": "path/to/start.log",
                   "end": "path/to/end.log"}),
    (FileNotFoundError, {"abbreviations": "path/to/abbreviations.txt",
                         "start": "path/to/start.log",
                         "end": "path/to/end.log"})])
def test_init_race_with_invalid_log_files(err, arg):
    with pytest.raises(err):
        r = Race(log_files=arg)


class TestRaceGetMethods:
    @pytest.fixture(scope="session")
    def report_file_paths(self, tmp_path_factory):
        path = tmp_path_factory.mktemp("sub")
        abbr = path / "abbreviations.txt"
        abbr.write_text("""DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER
                       EOF_Esteban Ocon_FORCE INDIA MERCEDES
                       SPF_Sergio Perez_FORCE INDIA MERCEDES""")
        start = path / "start.log"
        start.write_text("""DRR2018-05-24_12:11:24.067
                        EOF2018-05-24_12:12:11.838
                        SPF2018-05-24_12:12:01.035""")
        end = path / "end.log"
        end.write_text("""DRR2018-05-24_12:14:12.054
                      EOF2018-05-24_12:17:58.810
                      SPF2018-05-24_12:13:13.883""")
        return {"abbreviations": abbr, "start": start, "end": end}

    @pytest.fixture(scope="session")
    def setup(self, report_file_paths):
        race = Race(report_file_paths)
        return race

    def test_non_existent_file_path(self, report_file_paths):
        with patch("builtins.open", mock_open()) as mo:
            mo.side_effect = PermissionError
            with pytest.raises(PermissionError):
                race = Race(report_file_paths)

    def test_racers_attribute(self, setup):
        assert setup.racers == {"DRR":
                                    {"name": "Daniel Ricciardo",
                                     "team": "RED BULL RACING TAG HEUER",
                                     "q1_start": datetime.strptime("2018-05-24_12:11:24.067", "%Y-%m-%d_%H:%M:%S.%f"),
                                     "q1_end": datetime.strptime("2018-05-24_12:14:12.054", "%Y-%m-%d_%H:%M:%S.%f")},
                                "EOF":
                                    {"name": "Esteban Ocon",
                                     "team": "FORCE INDIA MERCEDES",
                                     "q1_start": datetime.strptime("2018-05-24_12:12:11.838", "%Y-%m-%d_%H:%M:%S.%f"),
                                     "q1_end": datetime.strptime("2018-05-24_12:17:58.810", "%Y-%m-%d_%H:%M:%S.%f")},
                                "SPF":
                                    {"name": "Sergio Perez",
                                     "team": "FORCE INDIA MERCEDES",
                                     "q1_start": datetime.strptime("2018-05-24_12:12:01.035", "%Y-%m-%d_%H:%M:%S.%f"),
                                     "q1_end": datetime.strptime("2018-05-24_12:13:13.883", "%Y-%m-%d_%H:%M:%S.%f")},
                                }

    def test_get_number_of_racers(self, setup):
        assert setup.get_number_of_racers() == 3

    def test_get_date_of_race(self, setup):
        assert str(setup.get_date_of_race()) == "2018-05-24"

    def test_get_start_time_of_q1(self, setup):
        assert str(setup.get_start_time_of_q1()) == "12:11:24.067000"

    @pytest.mark.parametrize("reverse, result", [
        (False, ["Daniel Ricciardo", "Esteban Ocon", "Sergio Perez"]),
        (True, ["Sergio Perez", "Esteban Ocon", "Daniel Ricciardo"])
    ])
    def test_get_names_of_racers(self, setup, reverse, result):
        assert setup.get_names_of_racers(reverse) == result

    def test_get_names_of_racers_without_arguments(self, setup):
        assert setup.get_names_of_racers() == ["Daniel Ricciardo",
                                               "Esteban Ocon",
                                               "Sergio Perez"]

    @pytest.mark.parametrize("reverse, result", [
        (False, ["FORCE INDIA MERCEDES", "RED BULL RACING TAG HEUER"]),
        (True, ["RED BULL RACING TAG HEUER", "FORCE INDIA MERCEDES"])
    ])
    def test_get_teams(self, setup, reverse, result):
        assert setup.get_teams(reverse) == result

    def test_get_teams_without_arguments(self, setup):
        assert setup.get_teams() == ["FORCE INDIA MERCEDES",
                                     "RED BULL RACING TAG HEUER"]

    @pytest.fixture(scope="session")
    def driver_time(self):
        esteban_start = datetime.strptime("2018-05-24_12:12:11.838",
                                          "%Y-%m-%d_%H:%M:%S.%f")
        esteban_end = datetime.strptime("2018-05-24_12:17:58.810",
                                        "%Y-%m-%d_%H:%M:%S.%f")
        esteban_timedelta = esteban_end - esteban_start
        sergio_start = datetime.strptime("2018-05-24_12:12:01.035",
                                         "%Y-%m-%d_%H:%M:%S.%f")
        sergio_end = datetime.strptime("2018-05-24_12:13:13.883",
                                       "%Y-%m-%d_%H:%M:%S.%f")
        sergio_timedelta = sergio_end - sergio_start
        daniel_start = datetime.strptime("2018-05-24_12:11:24.067",
                                         "%Y-%m-%d_%H:%M:%S.%f")
        daniel_end = datetime.strptime("2018-05-24_12:14:12.054",
                                       "%Y-%m-%d_%H:%M:%S.%f")
        daniel_timedelta = daniel_end - daniel_start
        return {"esteban": esteban_timedelta,
                "sergio": sergio_timedelta,
                "daniel": daniel_timedelta}

    def test_get_report(self, setup, driver_time):
        assert setup.get_report() == [["Sergio Perez",
                                       "FORCE INDIA MERCEDES",
                                       driver_time["sergio"]],
                                      ["Daniel Ricciardo",
                                       "RED BULL RACING TAG HEUER",
                                       driver_time["daniel"]],
                                      ["Esteban Ocon",
                                       "FORCE INDIA MERCEDES",
                                       driver_time["esteban"]]
                                      ]

    def test_get_racer(self, setup, driver_time):
        assert setup.get_racer("Sergio Perez") == ["SPF",
                                                   "Sergio Perez",
                                                   "FORCE INDIA MERCEDES",
                                                   str(driver_time["sergio"])[3: -3]]

    def test_get_racer_no_racer_name(self, setup):
        with pytest.raises(UserWarning):
            setup.get_racer("Elon Mask")

    def test_get_racers_in_team_desc(self, setup, driver_time):
        assert setup.get_racers_in_team("FORCE INDIA MERCEDES", order=True) == [["SPF",
                                                                                 "Sergio Perez",
                                                                                 "FORCE INDIA MERCEDES",
                                                                                 str(driver_time["sergio"])[3: -3]],
                                                                                ["EOF",
                                                                                 "Esteban Ocon",
                                                                                 "FORCE INDIA MERCEDES",
                                                                                 str(driver_time["esteban"])[3: -3]]]

    def test_get_racers_in_team_asc(self, setup, driver_time):
        assert setup.get_racers_in_team("force india mercedes", order=False) == [["EOF",
                                                                                  "Esteban Ocon",
                                                                                  "FORCE INDIA MERCEDES",
                                                                                  str(driver_time["esteban"])[3: -3]],
                                                                                 ["SPF",
                                                                                  "Sergio Perez",
                                                                                  "FORCE INDIA MERCEDES",
                                                                                  str(driver_time["sergio"])[3: -3]]]

    def test_get_racers_in_team_no_order_argument(self, setup, driver_time):
        assert setup.get_racers_in_team("FORCE INDIA MERCEDES") == [["EOF",
                                                                     "Esteban Ocon",
                                                                     "FORCE INDIA MERCEDES",
                                                                     str(driver_time["esteban"])[3: -3]],
                                                                    ["SPF",
                                                                     "Sergio Perez",
                                                                     "FORCE INDIA MERCEDES",
                                                                     str(driver_time["sergio"])[3: -3]]]

    def test_get_racers_in_team_no_team_name(self, setup, driver_time):
        with pytest.raises(UserWarning):
            assert setup.get_racers_in_team("SpaceX")
