from typing import Final, Iterable, Callable

from pyannotating import Special
from pyhandling.collections_ import MultiRange

from flask import Response, Config


class StatusCodeGroup:
    """
    Class for storing the HTTP status codes of responses in the form of a
    structure and declarative access to them.
    """

    INFORMATIONAL: Final[MultiRange] = MultiRange(range(100, 200))
    SUCCESSFUL: Final[MultiRange] = MultiRange(range(200, 300))
    REDIRECTION: Final[MultiRange] = MultiRange(range(300, 400))
    CLIENT_ERROR: Final[MultiRange] = MultiRange(range(400, 500))
    SERVER_ERROR: Final[MultiRange] = MultiRange(range(500, 600))

    GOOD: Final[MultiRange] = MultiRange(range(100, 400))
    ERROR: Final[MultiRange] = MultiRange(range(400, 600))

    ALL: Final[MultiRange] = MultiRange(range(100, 600))


def status_code_from(response: Special[Response | Iterable]) -> int:
    """Function to get code status from non-structural data."""

    if isinstance(response, Response):
        return response.status_code
    elif (
        isinstance(response, Iterable)
        and len(response) >= 2
        and isinstance(response[1], int | float)
        and int(response[1]) == response[1]
    ):
        return response[1]
    else:
        return 200


def config_from(
    file_name: str,
    config_parse_method: Callable[[Config, str], None] = Config.from_object
) -> Config:
    """Function for creating a config, delegating the update method to it."""

    config = Config(str())
    config_parse_method(config, file_name)

    return config