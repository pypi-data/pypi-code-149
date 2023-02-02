from enum import Enum


class CodesStatusTkt(Enum):
    """
    Contains list of internal error codes from the Toolkit. Toolkit error codes starts at error codes 600 to 699.
    """

    ERR_CODE_CONN_ERR = 600
    """
    Connection Error Code Status. Your provided hostname or port might be incorrect.
    """

    ERR_CODE_NO_TOKEN = 610
    """
    No Token Code Status. When a Toolkit API requires a token to initiate request, and token is not provided yet.
    Login is required to retrieve the appropriate token.
    """

    ERR_CODE_SSL_ERR = 611
    """
    SSL Error Code Status. SSL Certificate is incorrect or it might expire.
    """

    ERR_CODE_NO_RESPONSE = 630
    """
    No Response Code Status. Communication to endpoint post no response. This is an unexpected error.
    """
