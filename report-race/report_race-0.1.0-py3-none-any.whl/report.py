"""Command-line interface for report of Monaco race.

Class:
    OrderedNamespace
    CliArguments
    CliEngine
"""
import sys
import argparse
from typing import Any

from tabulate import tabulate

from report_race.constant import ORDER, TOP_RACERS, TABLE_FORMAT
from report_race.race import Race, LogFilesValidator


class OrderedNamespace(argparse.Namespace):
    """Namespace with ordered arguments.

    Adds dictionary which saves order of input arguments in cli.
    """

    def __init__(self, **kwargs):
        """Initialize with new attribute

        Args:
            kwargs: arguments in parser
        """
        # _order will save input arguments in given order
        self.__dict__["_order"] = []
        super().__init__(**kwargs)

    def __setattr__(self, attr: str, value: Any):
        """Set attributes.

        _order will contain only attribute names, that was
        provided in cli in preserved order. If same attribute is entered more
        than once, only last one will be executed.

        Example:
            cli arguments:
            --files <path> --time --date --time --report --time
            execution order:
            --date -- report --time

        Args:
            attr: Attributes in Namespace.
            value: Values of attributes in Namespace.
        """
        super().__setattr__(attr, value)
        # Ignore attributes without data from cli.
        if value not in [None, False]:
            if attr not in self.__dict__["_order"]:
                self.__dict__["_order"].append(attr)
            else:
                # Delete attr and append to the list to preserve
                # the order of input arguments.
                self.__dict__["_order"].remove(attr)
                self.__dict__["_order"].append(attr)

    def ordered(self) -> list[tuple]:
        """Generate values for attributes in _order.

        Returns:
            Return _order pairs of attributes and values.
        """
        return [(attr, getattr(self, attr)) for attr in self._order
                if attr != "files"]

    def only_file_path(self):
        """Checks argument quantity.

        Checks if any argument was given beside files path argument.

        Raises:
            UserWarning: If only files path was given as argument.
        """
        if len(self.__dict__["_order"]) == 1:
            raise UserWarning("Application should use at least one argument (except 'files' argument!)")


class CliArguments:
    """Represents command-line interface"""

    @staticmethod
    def cli():
        """Implement command-line interface

        Uses argparse to get input from command-line
        and print according result.
        """
        parser = argparse.ArgumentParser(
            prog="Report of Monaco 2018 racing.",
            description="Get information about the race from the log files."
        )
        parser.add_argument(
            "-f", "--files", required=True,
            help="directory path where the race log files are located (required argument)"
        )
        parser.add_argument(
            "-r", "--report", action="store_true",
            help="report of the 1st qualification results"
        )
        parser.add_argument(
            "-d", "--date", action="store_true",
            help="date of the 1st qualification"
        )
        parser.add_argument(
            "-t", "--time", action="store_true",
            help="start time of the 1st qualifications"
        )
        parser.add_argument(
            "--racers-number", action="store_true",
            help="number of the racers in the race"
        )
        parser.add_argument(
            "--driver",
            help="information about specific driver"
        )
        parser.add_argument(
            "--racers",
            const=list(ORDER.keys())[0],
            nargs="?",
            choices=ORDER.keys(),
            help="""list of all racers in the race in asc or"
                    desc order (default is asc)"""
        )
        parser.add_argument(
            "--teams",
            const=list(ORDER.keys())[0],
            nargs="?",
            choices=ORDER.keys(),
            help="""list of all teams in the race in asc "
                    or desc order (default is asc)"""
        )
        parser.add_argument(
            "--team-racers",
            help="list of all racers from specific team"
        )

        args = parser.parse_args(namespace=OrderedNamespace())

        try:
            # Check if only "files" argument was passed
            args.only_file_path()
        except UserWarning as err:
            print(err)
            parser.print_usage()
            sys.exit()
        return args


class CliEngine:
    """Cli engine.

    Class provides methods to get arguments from command-line, check input data
    and print appropriate result.

    Attributes:
        METHODS_WITH_ARGUMENTS: Methods that are called with one argument
        REPORT_HEADER: Header for report table
        RACERS_HEADER Header for racers and racers in teams table

    """
    METHODS_WITH_ARGUMENTS = ["driver", "racers", "teams", "team_racers"]
    REPORT_HEADER = ["", "Full Name", "Team", "Q1 Time"]
    RACERS_HEADER = ["Abbr", "Full Name", "Team", "Q1 Time"]
    RACERS_HEADER_SHORT = ["Abbr", "Full Name"]

    def __init__(self):
        """Initialize args, race and print_func attributes"""
        self.args = CliArguments.cli()
        try:
            # Get log files from file directory and create race instance.
            self.race = CliEngine.race_from_log_files(self.args.files)
        except (TypeError, FileNotFoundError, NotADirectoryError, UserWarning) as err:
            sys.exit(err)
        # Save all print functions in dictionary in order to make execution simpler.
        self._print_func = {"report": self.print_report,
                            "time": self.print_time,
                            "date": self.print_date_of_the_race,
                            "racers_number": self.print_number_of_racers,
                            "driver": self.print_driver,
                            "racers": self.print_racers,
                            "teams": self.print_teams,
                            "team_racers": self.print_racers_in_team}

    @staticmethod
    def race_from_log_files(path: str) -> Race:
        """Create Race instance

        Create Race instance from log_files in given directory.

        Args:
            path: path of directory with log files.
        """
        validator = LogFilesValidator(path)
        return validator.init_race()

    def print_result(self):
        """Call print methods according cli arguments"""
        # Go through passed arguments and execute according print functions.
        for arg, value in self.args.ordered():
            if arg in CliEngine.METHODS_WITH_ARGUMENTS:
                self._print_func[arg](value)
            else:
                self._print_func[arg]()

    def print_date_of_the_race(self):
        """Print date of the race."""
        print("\nDate of the race:")
        print(f"\t{self.race.get_date_of_race()}")

    def print_time(self):
        """Print start time of the 1st qualification."""
        print("\n1st qualification round started at:")
        print(f"\t{self.race.get_start_time_of_q1()}")

    def print_number_of_racers(self):
        """Print number of racers in the race."""
        print("\nNumber of the racers in the race:")
        print(f"\t{self.race.get_number_of_racers()}")

    def print_report(self):
        """Print race report.

        Prints race report in nice table look.
        """
        # Build report of the race.
        race_report = self.race.get_report()
        print("\nReport of the race:")
        # Calculate separation line length for each column.
        place_sep = "--"
        racer_sep = "-" * len(max(self.race.get_racers()[1], key=len))
        team_sep = "-" * len(max(self.race.get_teams(), key=len))
        time_sep = "-" * len(race_report[0][3])
        # Add separation line.
        separation_line = [place_sep, racer_sep, team_sep, time_sep]
        race_report.insert(TOP_RACERS, separation_line)
        print(tabulate(race_report,
                       headers=CliEngine.REPORT_HEADER,
                       tablefmt=TABLE_FORMAT))

    def print_driver(self, name: str):
        """Print driver information.

        Args:
            name: Driver full name.

        Raises:
            UserWarning: if no racer found with given name.
        """
        try:
            driver = self.race.get_racer(name)
            print(f"\nInformation about {driver[1]}:")
            print(tabulate([driver],
                           headers=CliEngine.RACERS_HEADER_SHORT,
                           tablefmt=TABLE_FORMAT))
        except UserWarning as err:
            print(err)

    def print_racers(self, order: str):
        """Print list of racers in the race.

        Args:
            order: defines order of the result list by racer's abbreviation.
        """
        racers = self.race.get_racers(reverse=ORDER[order])
        print(tabulate(racers,
                       headers=CliEngine.RACERS_HEADER,
                       tablefmt=TABLE_FORMAT))

    def print_teams(self, order: str):
        """Print list of teams in the race.

        Args:
            order: Flag for racers order.
        """
        teams = [[team] for team in self.race.get_teams(reverse=ORDER[order])]
        print(tabulate(teams,
                       headers=["List of teams:"],
                       tablefmt=TABLE_FORMAT))

    def print_racers_in_team(self, team: str):
        """Print racers in specific team.

        Args:
            team: Name of the team.
        """
        try:
            racers = self.race.get_racers_in_team(team)
            print(f"\nRacers from {team.upper()} team:")
            print(tabulate(racers,
                           headers=CliEngine.RACERS_HEADER,
                           tablefmt=TABLE_FORMAT, ))
        except UserWarning as err:
            print(err)


if __name__ == "__main__":
    cli = CliEngine()
    cli.print_result()
