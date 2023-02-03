import argparse
from argparse import Namespace
from unittest.mock import mock_open, patch

import pytest

from src.uniqcharspac.app import execution_arguments_priority, main, read_file
from src.uniqcharspac.utils import (CommandLineArgumentsException,
                                    CustomFileNotFoundException,
                                    CustomTypeErrorException)

fake_file_path = "/path/to/fake_file"
negative_params = [{"2": 2}, (1, 2), None, True, 1, 2.2]


@patch("builtins.open", new_callable=mock_open, read_data="test_string")
@patch("src.uniqcharspac.app.app.os.path.exists", return_value=True)
def test_read_file_is_exists_positive(mock_exist, mock_open_file):
    assert read_file(fake_file_path) == ["test_string"]
    mock_exist.assert_called_once()
    mock_open_file.assert_called_once()


@patch("src.uniqcharspac.app.app.os.path.exists", return_value=False)
def test_read_file_is_not_exists_negative(mock_exist):
    message = f"No such file or directory: '{fake_file_path}'"
    with pytest.raises(CustomFileNotFoundException) as exception:
        read_file(fake_file_path)
    assert str(exception.value) == message
    mock_exist.assert_called_once()


@patch("src.uniqcharspac.app.app.count_uniq_chars_in_string")
@patch("src.uniqcharspac.app.app.count_uniq_chars_in_list")
@patch("src.uniqcharspac.app.app.read_file")
def test_arguments_priority_with_data_and_string_args(
        mocked_read_file,
        mocked_list_func,
        mocked_file_func
):
    namespace_with_data_and_string = argparse.Namespace(data="/fake/path/to/file", string="string")
    assert execution_arguments_priority(namespace_with_data_and_string)
    mocked_read_file.assert_called_once()
    mocked_list_func.assert_called_once()
    mocked_file_func.assert_not_called()


@patch("src.uniqcharspac.app.app.count_uniq_chars_in_string")
@patch("src.uniqcharspac.app.app.count_uniq_chars_in_list")
@patch("src.uniqcharspac.app.app.read_file")
def test_arguments_priority_with_only_data_arg(
        mocked_read_file,
        mocked_list_func,
        mocked_string_func
):
    namespace_with_string_only_arg = argparse.Namespace(data=None, string="string")
    assert execution_arguments_priority(namespace_with_string_only_arg)
    mocked_read_file.assert_not_called()
    mocked_list_func.assert_not_called()
    mocked_string_func.assert_called_once()


def test_arguments_priority_with_empty_namespace():
    empty_namespace = argparse.Namespace(data=None, string=None)
    message = "Required argument '--string' or '--data' is missing"
    with pytest.raises(CommandLineArgumentsException) as exception:
        execution_arguments_priority(empty_namespace)
    assert str(exception.value) == message


@pytest.mark.parametrize("test_data", negative_params)
def test_execution_arguments_priority_negative(test_data):
    message = f"Wrong data type {type(test_data)}, must be a {Namespace}"
    with pytest.raises(CustomTypeErrorException) as exception:
        execution_arguments_priority(test_data)
    assert str(exception.value) == message


@patch("src.uniqcharspac.app.app.execution_arguments_priority")
@patch("src.uniqcharspac.app.app.ArgumentParser.parse_args")
def test_main_mocked_positive(mocked_parse_args, mocked_arguments_priority):
    assert main()
    mocked_parse_args.assert_called_once()
    mocked_arguments_priority.assert_called_once()
