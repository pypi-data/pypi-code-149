class InvalidLoginError(Exception):
    """The login provided is invalid."""


class InvalidDeviceIDError(Exception):
    """The device ID provided is invalid."""


class NotOpenError(Exception):
    """The WebSocket has not been opened."""


class UnexpectedError(Exception):
    """This error should never be raised."""


class ResponseError(Exception):
    """General response error."""
