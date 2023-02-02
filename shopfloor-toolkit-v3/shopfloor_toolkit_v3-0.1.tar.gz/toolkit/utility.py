import logging.handlers
import os

import requests

from toolkit.code_status_tkt import CodesStatusTkt


def is_true(byte_value: bytes):
    """
    Converts the given byte value of b'true' or b'false' into True or False respectively.

    :param byte_value: Byte value of true/false (e.g. b'false', b'true')
    :return: True if byte value is b'true'.
    """
    result_content = False
    if byte_value.decode("utf-8") == "true":
        result_content = True

    return result_content


def to_string(byte_value: bytes):
    """
    Convert provided byte to string.

    :param byte_value: byte value in UTF-8. To be converted to string.
    :return: decoded string value
    """
    result_content = byte_value.decode("utf-8")
    return result_content


def get_comm_logger_name():
    """
    Returns the logger name for the communication logger.

    :return: string name of the communication logger.
    """
    return "comm_logger"


def get_default_comm_logger(comm_log_path: str,
                            comm_log_level: int = logging.ERROR,
                            max_log_size: int =(5*1024*1024)):
    """
    Generate and configure a communication logger. Logger will archive log file if it reaches max_log_size, and
    maximum of 10 backup files only. Log file is named toolkit.log, and is not encoded.

    :param comm_log_path: Directory of the log file
    :param comm_log_level: minimum log level to print, default is only Errors and Criticals are logged
    :param max_log_size: maximum size for each log files, default max size is 5MB
    :return: Communication logger instance
    """
    handler = logging.handlers.RotatingFileHandler(filename=f"{comm_log_path}toolkit.log",
                                                   mode='a',
                                                   maxBytes=max_log_size,
                                                   backupCount=10,
                                                   encoding=None,
                                                   delay=False)

    formatter = logging.Formatter('%(asctime)s %(levelname)s '
                                  '[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(get_comm_logger_name())
    logger.setLevel(comm_log_level)
    logger.addHandler(handler)

    return logger


def get_status_code_msg(status_code: CodesStatusTkt, lang='en'):
    """
    Returns the localization message of the give status code.


    :param status_code: Status code. See Status Code in API documentation.
    :param lang: 'en' for english (as of now english is only supported)
    :return: String message
    """
    msg = ""

    match lang:
        case 'en':
            match status_code:
                case CodesStatusTkt.ERR_CODE_NO_TOKEN.value:
                    msg = f"Error Code#{status_code}:No Token found. Try logging in."
                case CodesStatusTkt.ERR_CODE_CONN_ERR.value:
                    msg = f"Error Code#{status_code}:Connection error. Check if hostname and port are correct."
                case CodesStatusTkt.ERR_CODE_SSL_ERR.value:
                    msg = f"Error Code#{status_code}:SSL Error. Check if SSL Certificate is valid."
                case CodesStatusTkt.ERR_CODE_NO_RESPONSE.value:
                    msg = f"Error Code#{status_code}:No Response. Contact publisher (https://medulla.net/contact)."
                case _:
                    msg = f"Error Code#{status_code}"
        case _:
            msg = "Unsupported language."

    return msg


def request_post(status_code, logger, connection_url, content_dict, header=None, verify=False):
    """
    Send requests POST method to provided connection_url.

    :param status_code: A list of 1 entry. Contains resulting Status Code. Value of 200 means its successful, \
    600-699 means error occurs
    :param logger:  Logger instance (from logging)
    :param connection_url: URL to request POST method (ex: https://test.com:443/test)
    :param content_dict: Body content for your request
    :param header: Header content for your request
    :param verify: Set to False if SSL Certificate is available.
    :return: requests POST method response
    """
    result = None
    try:
        if header is None:
            result = requests.post(connection_url, json=content_dict, verify=verify)
        else:
            result = requests.post(connection_url, json=content_dict, headers=header, verify=verify)

        if result is not None:
            status_code[0] = 200
        else:
            logger.error(f"Unexpected response (None). Error code({result.status_code})")
            status_code[0] = CodesStatusTkt.ERR_CODE_NO_RESPONSE.value

    except requests.exceptions.SSLError:
        logger.error(f"SSL Error occurs. url={connection_url} content={content_dict}")
        status_code[0] = CodesStatusTkt.ERR_CODE_SSL_ERR.value
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection Error occurs. url={connection_url} content={content_dict}")
        status_code[0] = CodesStatusTkt.ERR_CODE_CONN_ERR.value

    return result


def request_get(status_code, logger, connection_url, content_dict, header=None, verify=False):
    """
    Send requests GET method to provided connection_url.

    :param status_code: A list of 1 entry. Contains resulting Status Code. Value of 200 means its successful, \
    600-699 means error occurs
    :param logger:  Logger instance (from logging)
    :param connection_url: URL to request GET method (ex: https://test.com:443/test)
    :param content_dict: Body content for your request
    :param header: Header content for your request
    :param verify: Set to False if SSL Certificate is available.
    :return: requests GET method response
    """
    result = None
    try:
        if header is None:
            result = requests.get(connection_url, json=content_dict, verify=verify)
        else:
            result = requests.get(connection_url, json=content_dict, headers=header, verify=verify)

        if result is not None:
            status_code[0] = 200
        else:
            logger.error(f"Unexpected response (None). Error code({result.status_code})")
            status_code[0] = CodesStatusTkt.ERR_CODE_NO_RESPONSE.value

    except requests.exceptions.SSLError:
        logger.error(f"SSL Error occurs. url={connection_url} content={content_dict}")
        status_code[0] = CodesStatusTkt.ERR_CODE_SSL_ERR.value
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection Error occurs. url={connection_url} content={content_dict}")
        status_code[0] = CodesStatusTkt.ERR_CODE_CONN_ERR.value

    return result
