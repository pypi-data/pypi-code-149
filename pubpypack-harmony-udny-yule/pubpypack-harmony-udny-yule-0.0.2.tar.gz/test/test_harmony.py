import pytest
import sys

from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch
from imppkg.harmony import main
from termcolor import colored
from typing import List, Union


def test_harmony_happy_path(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]):
    inputs = ["1", "4", "4"]
    monkeypatch.setattr(target=sys, name="argv", value=["harmony"] + inputs)

    main()

    expected_result_value = 2.0
    assert capsys.readouterr().out.strip() == colored(
        text=str(expected_result_value), color="red", on_color="on_cyan", attrs=["bold"]
    )


@pytest.mark.parametrize(
    "inputs, expected_result_value",
    [
        (["1", "4", "4"], 2.0),
        ([], ValueError),
        (["foo", "bar"], ValueError),
    ],
)
def test_harmony_parametrized(
    inputs: List[Union[int, float]], expected_result_value: float, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
):
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)
    if isinstance(expected_result_value, type) and issubclass(expected_result_value, Exception):
        with pytest.raises(expected_result_value):
            main()
    else:
        main()
        assert capsys.readouterr().out.strip() == colored(
            text=str(expected_result_value), color="red", on_color="on_cyan", attrs=["bold"]
        )
