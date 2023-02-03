class BaseSongRecognizeException(Exception):
    ...


class ProcessError(BaseSongRecognizeException):
    """subprocess error"""
