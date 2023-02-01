import pytest
from imppkg.harmonic_mean import harmonic_mean
from hypothesis import given, assume
from hypothesis.strategies import lists, floats, integers, one_of, text


@given(lists(integers(min_value=1), min_size=1))
def test_harmonic_mean_valid_input(numbers):
    assert harmonic_mean(numbers) == (len(numbers) / sum(1 / x for x in numbers))


def test_harmonic_mean_empty_input():
    with pytest.raises(ValueError, match="Numbers list must not be empty."):
        harmonic_mean([])


@given(lists(one_of(floats(allow_nan=False, allow_infinity=False), integers()), min_size=1))
def test_harmonic_mean_with_negative_numbers(numbers):
    assume(any(i <= 0 for i in numbers))
    with pytest.raises(ValueError, match="Numbers list must contain only strictly positive numbers."):
        harmonic_mean(numbers)


@given(lists(one_of(floats(allow_nan=True, allow_infinity=True), integers(), text()), min_size=1))
def test_harmonic_mean_with_non_numeric_values(numbers):
    assume(any(isinstance(i, (int, float)) is False for i in numbers))
    with pytest.raises(TypeError, match="Numbers list must contain only numeric values."):
        harmonic_mean(numbers)
