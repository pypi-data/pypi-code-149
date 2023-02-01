"""Tests for CLI.

Tests for command-line interface in report module,
"""
from unittest.mock import patch

import pytest
from tabulate import tabulate

from report.report import Cli, OrderedNamespace
import report.constant as c


class TestCli:

    def test_cli_init(self):
        cli = Cli()
        assert len(cli._print_func) == 8

    @pytest.fixture(scope="session")
    def report_files_empty(self, tmp_path_factory):
        # Create directory with necessary files.
        path = tmp_path_factory.mktemp("sub")
        abbr = path / "abbreviations.txt"
        abbr.write_text("")
        start = path / "start.log"
        start.write_text("")
        end = path / "end.log"
        end.write_text("")
        # Create empty directory.
        empty_dir = tmp_path_factory.mktemp("empty")

        return [path, abbr, start, end, empty_dir]

    @pytest.fixture(scope="session")
    def setup(self):
        cli = Cli()
        return cli

    def test_get_path_to_file(self, report_files_empty, setup):
        result = setup.get_path_to_files(str(report_files_empty[0]))
        assert result == {"abbreviations": str(report_files_empty[1]),
                          "start": str(report_files_empty[2]),
                          "end": str(report_files_empty[3])}

    def test_get_path_to_file_with_error1(self, report_files_empty, setup):
        with pytest.raises(NotADirectoryError):
            assert setup.get_path_to_files(str(report_files_empty[1]))

    def test_get_path_to_file_with_error2(self, report_files_empty, setup):
        with pytest.raises(UserWarning):
            assert setup.get_path_to_files(str(report_files_empty[4]))

    def test_get_path_to_file_with_error3(self, setup):
        with pytest.raises(FileNotFoundError):
            assert setup.get_path_to_files("no/such/directory")

    def test_output_with_file_argument(self, setup, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        try:
            with patch("sys.argv", ["report.py", "-f", "./data"]):
                setup.cli()
        except SystemExit:
            output = capsys.readouterr().out.rstrip()
            assert "Report of Monaco 2018 racing." in output

    @pytest.fixture(scope="session")
    def report_files(self, tmp_path_factory):
        path = tmp_path_factory.mktemp("sub")
        abbr = path / "abbreviations.txt"
        abbr.write_text("""DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER""")
        start = path / "start.log"
        start.write_text("""DRR2018-05-24_12:11:24.067""")
        end = path / "end.log"
        end.write_text("""DRR2018-05-24_12:14:12.054""")
        return {"abbreviations": abbr, "start": start, "end": end}

    @pytest.fixture(scope="session")
    def setup_with_race(self, setup, report_files):
        setup.create_race(report_files)
        return setup

    @patch("report.report.Race.get_date_of_race", return_value="2019")
    def test_output_date(self, mock_obj, setup_with_race, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        setup_with_race.print_date_of_the_race()
        output = capsys.readouterr().out.rstrip()
        assert "\nDate of the race:\n\t2019" == output

    @patch("report.report.Race.get_start_time_of_q1", return_value="12:00:00")
    def test_output_time(self, mock_obj, setup_with_race, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        setup_with_race.print_time()
        output = capsys.readouterr().out.rstrip()
        assert "\n1st qualification round started at:\n\t12:00:00" == output

    @patch("report.report.Race.get_number_of_racers", return_value="19")
    def test_output_number_of_racers(self, mock_obj, setup_with_race, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        setup_with_race.print_number_of_racers()
        output = capsys.readouterr().out.rstrip()
        assert "\nNumber of the racers in the race:\n\t19" == output

    @patch("report.report.Race.get_report",
           return_value=[["Sergio Perez", "FORCE INDIA MERCEDES", "00:01:12:333000"],
                         ["Daniel Ricciardo", "RED BULL RACING TAG HEUER", "00:01:12:333000"],
                         ])
    def test_output_report(self, mock_obj, setup_with_race, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        setup_with_race.print_report()
        output = capsys.readouterr().out.rstrip()
        assert tabulate([["1", "Sergio Perez",
                          "FORCE INDIA MERCEDES",
                          "01:12:333"],
                         ["2", "Daniel Ricciardo",
                          "RED BULL RACING TAG HEUER",
                          "01:12:333"],
                         ],
                        headers=["", "Full Name", "Team", "Q1 Time"],
                        tablefmt=c.TABLE_FORMAT) in output

    @patch("report.report.Race.get_racer",
           return_value=["SPF", "Sergio Perez", "FORCE INDIA MERCEDES", "01:12:333000"])
    def test_output_racer(self, mock_obj, setup_with_race, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        setup_with_race.print_driver("Sergio Perez")
        output = capsys.readouterr().out.rstrip()
        assert tabulate([["SPF", "Sergio Perez",
                          "FORCE INDIA MERCEDES",
                          "01:12:333000"]],
                        headers=["Abbr", "Full Name", "Team", "Q1 Time"],
                        tablefmt=c.TABLE_FORMAT) in output

    @patch("report.report.Race.get_names_of_racers")
    @pytest.mark.parametrize("order, result, mock_result", [("asc",
                                                             [["Sergio Perez"], ["Esteban Ocon"]],
                                                             ["Sergio Perez", "Esteban Ocon"]),
                                                            ("desc",
                                                             [["Esteban Ocon"], ["Sergio Perez"]],
                                                             ["Esteban Ocon", "Sergio Perez"])
                                                            ])
    def test_output_racers(self, mock_obj, setup_with_race, capsys, order, result, mock_result):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        mock_obj.return_value = mock_result
        setup_with_race.print_racers(order)
        output = capsys.readouterr().out.rstrip()
        assert tabulate(result,
                        headers=["List of racers:"],
                        tablefmt=c.TABLE_FORMAT) in output

    @patch("report.report.Race.get_teams")
    @pytest.mark.parametrize("order, result, mock_result", [("asc",
                                                             [["FERRARI"], ["RENAULT"]],
                                                             ["FERRARI", "RENAULT"]),
                                                            ("desc",
                                                             [["RENAULT"], ["FERRARI"]],
                                                             ["RENAULT", "FERRARI"])
                                                            ])
    def test_output_teams(self, mock_obj, setup_with_race, capsys, order, result, mock_result):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        mock_obj.return_value = mock_result
        setup_with_race.print_teams(order)
        output = capsys.readouterr().out.rstrip()
        assert tabulate(result,
                        headers=["List of teams:"],
                        tablefmt=c.TABLE_FORMAT) in output

    @patch("report.report.Race.get_racers_in_team")
    def test_output_racers_in_teams(self, mock_obj, report_files, setup_with_race, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        mock_obj.return_value = [["SPF", "Sergio Perez", "FORCE INDIA MERCEDES", "01:12:333000"],
                                 ["EOF", "Esteban Ocon", "FORCE INDIA MERCEDES", "01:12:555000"]]
        setup_with_race.print_racers_in_team("FORCE INDIA MERCEDES")
        output = capsys.readouterr().out.rstrip()
        assert tabulate([["SPF", "Sergio Perez", "FORCE INDIA MERCEDES", "01:12:333000"],
                         ["EOF", "Esteban Ocon", "FORCE INDIA MERCEDES", "01:12:555000"]],
                        headers=["Abbr", "Full Name", "Team", "Q1 Time"],
                        tablefmt=c.TABLE_FORMAT) in output

    @pytest.fixture(scope="session")
    def dict_path(self, tmp_path_factory):
        path = tmp_path_factory.mktemp("sub")
        abbr = path / "abbreviations.txt"
        abbr.write_text("""DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER""")
        start = path / "start.log"
        start.write_text("""DRR2018-05-24_12:11:24.067""")
        end = path / "end.log"
        end.write_text("""DRR2018-05-24_12:14:12.054""")
        return path

    def test_args_from_cli(self, dict_path, setup, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        with patch("sys.argv", ["report.py", "--files", f"{str(dict_path)}", "--report"]):
            setup.cli()
            assert len(setup.args.ordered()) == 1

