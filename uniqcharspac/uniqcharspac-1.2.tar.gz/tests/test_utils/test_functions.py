import pytest

from src.uniqcharspac.utils import (CustomTypeErrorException,
                                    count_uniq_chars_in_list,
                                    count_uniq_chars_in_string)

negative_params = [1, 2.2, (1, 2), None, True]


@pytest.mark.parametrize(
    "test_string, expected_count",
    [
        ("123 3467", 6),
        ("22222222", 0),
        ("", 0),
        (" ", 1),
    ]
)
def test_count_uniq_chars_in_string_positive(test_string, expected_count):
    assert count_uniq_chars_in_string(test_string) == expected_count


@pytest.mark.parametrize("test_data", negative_params)
def test_count_uniq_chars_in_string_negative(test_data):
    message = f"Wrong data type {type(test_data)}, must be a {str}"
    with pytest.raises(CustomTypeErrorException) as exception:
        count_uniq_chars_in_string(test_data)
    assert str(exception.value) == message


@pytest.mark.parametrize(
    "test_data, expected_count",
    [
        (["one", "two", "!@#$%^& *()"], [3, 3, 11]),
        (["", " "], [0, 1]),
        (["11111111", "2222"], [0, 0]),
    ]
)
def test_count_uniq_chars_in_list_positive(test_data, expected_count):
    assert count_uniq_chars_in_list(test_data) == expected_count


@pytest.mark.parametrize(
    "test_data",
    [1, 2.2, {"2": 2}, (1, 2), None, True]
)
def test_count_uniq_chars_in_list_negative(test_data):
    message = f"Wrong data type {type(test_data)}, must be a {list}"
    with pytest.raises(CustomTypeErrorException) as exception:
        count_uniq_chars_in_list(test_data)
    assert str(exception.value) == message
