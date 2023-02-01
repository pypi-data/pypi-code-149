"""Use for creating Race class

Class:
    Race
    LogFilesValidator
"""
import os
from datetime import datetime, timedelta
from typing import Union

from report_race.constant import REPORT_FILES


class Race:
    """Class represents race.

    Args:
        racers: dictionary of racers participated in the race. example:
            {"NHR":
               {"name": "Nico Hulkenberg",
                "team": RENAULT,
                "q1_start": datatime of string 2018-05-24_12:02:49.914,
                "q1_end": datatime of string 2018-05-24_12:04:02.979}

    Attributes:
        TRAILING_ZEROS: Index where trailing zeros ends in the lap time string
            Example: 00:02:12:831000
        LEADING_ZEROS: Index where leading zeros starts in the lap time string
            Example: 00:02:12:831000

    Raises:
        UserError:
            if get_racer and get_racers_in_team methods can't find name of the
            racer or the team in dictionary of racers.

    """
    TRAILING_ZEROS = 3
    LEADING_ZEROS = -3

    def __init__(self, racers: dict[str: dict[str: Union[str, datetime]]]):
        self.racers = racers

    def get_number_of_racers(self) -> int:
        """Get number of the racers in the race.

        Returns:
            Number of the racers in the race.
        """
        number_of_racers = len(self.racers.keys())
        return number_of_racers

    def get_date_of_race(self) -> datetime.date:
        """Get date in which race took place

        Returns:
            Date of the race.
        """
        race_date = self.racers[list(self.racers.keys())[0]]["q1_start"].date()
        return race_date

    def get_start_time_of_q1(self) -> datetime.time:
        """Get start time of the 1st qualification.

        Returns:
            1st qualifications start time.
        """
        q1_start_time = None
        # Loop through all racers q1_start time and find the earliest one.
        for racer in self.racers.values():
            racer_start_time = racer["q1_start"].time()
            if q1_start_time:
                # Check if racer_stat_time is earlier than q1_start_time.
                if q1_start_time > racer_start_time:
                    q1_start_time = racer_start_time
            else:
                # If q1 start time is None assign with first racers start time.
                q1_start_time = racer_start_time
        return q1_start_time

    def get_racers(self, reverse=False) -> list[list]:
        """Get all racer names in the race.

        Collect all racer abbreviation and full name
        by asc or desc order.

        Args:
            reverse: Defines order of racers in the list.
                If True than order of the racer abbreviation is reverse.

        Returns:
           List of information about racers in the list of list in asc or desc order.
        """
        racers = [[abbr,
                   racer["name"]]
                  for abbr, racer in self.racers.items()]
        # Sort by abbreviation.
        racers = sorted(racers, key=lambda x: x[0], reverse=reverse)
        return racers

    def get_teams(self, reverse=False) -> list[str]:
        """Get all team names in race.

        Collect all team names which are participating in the race
        by asc or desc order.

        Args:
            reverse: Defines order of team names in the list.
                If True than order of the team names is reverse.

        Returns:
            List of team names in asc or desc order.
        """
        # Use set to filter unique teams
        teams_in_race = {racer["team"] for racer in self.racers.values()}
        teams_in_race = sorted(teams_in_race, reverse=reverse)
        return teams_in_race

    def get_report(self) -> list[list[str, str, timedelta]]:
        """Build result of the 1st qualification.

        Returns:
            List of Racers place, name, team, lap time.
        """
        race_report = []
        for racer in self.racers.values():
            # list[name, team, lap time in string format: 2:12:831]
            race_report.append(
                [racer["name"],
                 racer["team"],
                 (str(racer["q1_end"] - racer["q1_start"])[Race.TRAILING_ZEROS: Race.LEADING_ZEROS])])
        # Sort report by lap time.
        race_report = sorted(race_report, key=lambda x: x[2])
        # Add place of the racer. Need to add after sorted lap time result.
        for place, racer in enumerate(race_report):
            racer.insert(0, place + 1)
        return race_report

    def get_racer(self, name: str) -> list:
        """Get racer data.

        Args:
            name: Name of the racer.

        Returns:
            Data about racer.

        Raises:
            UserWarning when name of the racers is not in dictionary of racers.
        """
        for key, racer in self.racers.items():
            if racer["name"] == name:
                racer_data = [key, racer["name"], racer["team"],
                              str(racer["q1_end"] - racer["q1_start"])[3: -3]]
                return racer_data
        raise UserWarning(f"Can't find racer with name: {name}")

    def get_racer_by_id(self, abbr: str) -> list:
        """Get racer data by id (abbreviation).

        Args:
            abbr: ID (abbreviation) of the racer.

        Returns:
            Data about racer.

        Raises:
            UserWarning when ID of the racer is not in dictionary of racers.
        """
        for key, racer in self.racers.items():
            if key == abbr:
                racer_data = [key, racer["name"], racer["team"],
                              str(racer["q1_end"] - racer["q1_start"])[3: -3]]
                return racer_data
        raise UserWarning(f"Can't find racer with id: {abbr}")

    def get_racers_in_team(self, team: str, order=False) -> list[list]:
        """Get racers from the team.

            Args:
                team: Name of the team.
                order: Defines order of racer names in the list.
                    If True than order of the racer names is reverse.

            Returns:
                List of racers data.

            Raises:
                UserWarning when team is not in dictionary of racers.
            """
        racers_in_team = []
        for key, racer in self.racers.items():
            if racer["team"] == team.upper():
                racer_data = [key, racer["name"], racer["team"],
                              str(racer["q1_end"] - racer["q1_start"])[3: -3]]
                racers_in_team.append(racer_data)
        racers_in_team = sorted(racers_in_team, key=lambda x: x[0], reverse=order)
        if racers_in_team:
            return racers_in_team
        raise UserWarning(f"Can't find team with name: {team}")


class LogFilesValidator:
    """Validator for Race class.

    Validates log_files from which Race class could be built.

    Args:
        path: path of directory with log files.

    Attributes:
        LOOK_UP_KEYS: list of keys for log_files validation.
        _racers: dictionary of racers participated in the race.

    Raises:
        UserError:
            if file/s in the path is/are missing or "log_files" argument contains invalid data.
        TypeError:
            if "log_files" argument contains unacceptable types.
        FileNotFoundError:
            if file in path from "log_files" can't be found.
        PermissionError:
            if file in path from "log_files" can't be read.
    """
    LOOK_UP_KEYS = ["abbreviations", "start", "end"]

    def __init__(self, path: str):
        """Get "log_files" from "path" argument."""
        self.log_files = self.get_path_to_files(path)
        self._racers = {}
        # Check "log_files" argument for valid structure and content.
        self._validate_log_files_argument()
        # Get information about racers.
        self._data_from_abbreviation(self.log_files["abbreviations"])
        # Get start and finish time of racer's best lap.
        for key, file_path in self.log_files.items():
            if key in ["start", "end"]:
                self._data_from_log_files(key, file_path)

    @staticmethod
    def get_path_to_files(path: str) -> dict[str: str]:
        """Get path to the log files.

        "log_files" argument must be a dictionary with three key-value pairs:
        {"abbreviations": "path/to/abbreviations.txt",
        "start": "path/to/start.log",
        "end": "path/to/end.log"}

        Returns:
            Dictionary with file name as key and path to the file as value.

        Raises:
            UserWarning: if not all files where found in the folder.
            NotADirectoryError: if path argument is not a dictionary.
            FileNotFoundError: if path does not exist.
        """
        # Get path of the log files from directory if file name is in lookup list
        log_files = {os.path.splitext(f)[0]: os.path.join(path, f)
                     for f in os.listdir(path)
                     if f.lower() in REPORT_FILES}
        # Check if dictionary has all necessary files.
        if len(log_files) != len(REPORT_FILES):
            raise UserWarning("File missing. Make sure that folder contains this files:"
                              f" {REPORT_FILES}")
        return log_files

    @staticmethod
    def __validate_log_files_len(log_file_len: int):
        """Validate length of "log_files" argument

        Args:
            log_file_len: length of log_files.

        Raises:
            UserWarning: if "log_files" argument len is not 3.
        """
        if log_file_len != 3:
            raise UserWarning("log_files argument should contain three key value pairs. "
                              f"{log_file_len} was provided.")

    @staticmethod
    def __validate_log_files_keys(key: str):
        """Check if "log_files" argument have all necessary keys.

        Args:
            key: key in "log_files" argument.

        Raises:
            UserWarning: if invalid key in "log_files" argument.
        """
        if key not in LogFilesValidator.LOOK_UP_KEYS:
            raise UserWarning(f"Invalid key in log_files argument: {key}")

    @staticmethod
    def __validate_log_files_values(file_path: str):
        """Check if file name in "log_files" argument are correct.

        Args:
            file_path: path to the log file.

        Raises:
            UserWarning: if invalid value in "log_files" argument.
            """
        try:
            if os.path.basename(file_path) not in REPORT_FILES:
                raise UserWarning(f"Invalid value in log_files argument {file_path}")
        except (TypeError, UserWarning):
            raise

    @staticmethod
    def __validate_log_files_is_empty(file_path):
        """Check if file in file_path from "log_files" argument is mot empty.

        Args:
            file_path: path of the log file.

        Raises:
            UserWarning: if file is empty.
        """
        if os.stat(file_path).st_size == 0:
            raise UserWarning(f"File is empty: {os.path.basename(file_path)}")

    def _validate_log_files_argument(self):
        """Validate "log_files" argument.

        "log_files" argument must be a dictionary with three key-value pairs:
        {"abbreviations": "path/to/abbreviations.txt",
        "start": "path/to/start.log",
        "end": "path/to/end.log"}

        Raises:
            UserWarning: if invalid key value pairs.
            TypeError: if file_path string can't be used by [os.path.basename].
        """
        try:
            # Check length of log_files argument.
            self.__validate_log_files_len(len(self.log_files))
            # Check if keys and values are acceptable.
            for key, file_path in self.log_files.items():
                self.__validate_log_files_keys(key)
                self.__validate_log_files_values(file_path)
                self.__validate_log_files_is_empty(file_path)
        except (TypeError, UserWarning):
            raise

    def _data_from_log_files(self, key, file_path):
        """Get data from log files.

                Read files and get the start and finish time of racers best lap.

                Args:
                    key: key in log_files argument.
                    file_path: file_path string in log_files argument

                Raises:
                    FileNotFoundError: if file_path is not found.
                    PermissionError: if program don't have permission to read file_path.
                """
        try:
            with open(file_path, encoding="utf8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        # First three chars in the line is abbreviation - key,
                        # rest is 1st qualification start time or end time of the lap
                        self._racers[line[:3]]["q1_" + key] = datetime.strptime(
                            line[3:].strip(), "%Y-%m-%d_%H:%M:%S.%f")
        except (FileNotFoundError, PermissionError):
            raise

    def _data_from_abbreviation(self, file_path):
        """Get data from abbreviations file.

        Read file and get abbreviation, full name and the team of the racer.

        Args:
            file_path: file_path string in log_files argument

        Raises:
            FileNotFoundError: if file_path is not found.
            PermissionError: if program don't have permission to read file_path.
        """
        try:
            with open(file_path, encoding="utf8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        # Information about racer is split with underscore:
                        # "abbreviation_name of the racer_racer team".
                        racer = line.split("_")
                        # Abbreviation is the key in dictionary of racers.
                        self._racers[racer[0]] = {"name": racer[1], "team": racer[2]}
        except (FileNotFoundError, PermissionError):
            raise

    def init_race(self) -> Race:
        """Initialize Race class from _racers

        Returns:
            Instance of Race class
        """
        return Race(self._racers)
