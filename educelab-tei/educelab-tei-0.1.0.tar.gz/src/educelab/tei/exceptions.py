class TEILibError(Exception):
    """Base class for other exceptions"""
    pass


class ParseError(TEILibError):
    """Raised when xml file could not be parsed into library objects"""
    pass


class TEIVerificationError(TEILibError):
    """Raised when library objects do not contain all information required by TEI standard"""
    pass
