import json
import logging
import os
import concurrent.futures

from copy import copy

import requests
import asyncio

# import aiohttp
import telebot
import time

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

COLORS = {
    "DEBUG": 30 + BLUE,
    "INFO": 30 + GREEN,
    "WARNING": 30 + YELLOW,
    "HTTP": 30 + CYAN,
    "ERROR": 30 + RED,
}

PREFIX = "\033["
SUFFIX = "\033[0m"

TIME = "%Y-%m-%d %H:%M:%S"
FORMAT = "%(asctime)s | [%(levelname)-7s] | %(message)s %(status)s %(data)s"


class LoggerFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record: logging.LogRecord) -> str:
        try:
            _record = copy(record)
            status: int | None = record.args.get("status") if record.args else None
            data: dict[str, any] | None = (
                record.args.get("data") if record.args else None
            )

            if status and type(status) != int:
                raise TypeError("Status type must be integer.")

            _record.status = f"| [STATUSCODE {status}]" if status else ""
            _record.data = f"| {data}" if data else ""

            message = logging.Formatter.format(self, _record)
            color = COLORS.get(_record.levelname.upper(), 37)

            return "{0}{1}m{2}{3}".format(PREFIX, color, message, SUFFIX)
        except Exception as error:
            return f"Error while logging your message: {error}"


def setup_logger(appname: str):
    HTTP = logging.DEBUG + 2
    logging.addLevelName(HTTP, "HTTP")

    def http(self, message, *args, **kws):
        self.log(HTTP, message, *args, **kws)

    logging.Logger.http = http

    logger = logging.getLogger(appname)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # Silence other loggers
    for log_name, log_obj in logging.Logger.manager.loggerDict.items():
        if log_name != appname:
            log_obj.disabled = True

    ch = logging.StreamHandler()
    ch.setFormatter(LoggerFormatter(FORMAT, TIME))

    logger.addHandler(ch)
    return logger
    
class PyLogger:
    def __init__(self, appname: str = "myapp"):
        self.logger = setup_logger(appname)
        self.vault(appname)

    @staticmethod
    def check_params(status_code, data):
        obj = {}
        if status_code:
            obj.update({"status": status_code})
        if data:
            obj.update({"data": data})
        return obj

    def error(self, message: str, status_code: int = None, data=None):
        args = self.check_params(status_code, data)
        if args:
            self.logger.error(message, args)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(asyncio.run, self.send_alert(message=message, status_code=status_code, data=data, args=args))
        else:
            self.logger.error(message)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(asyncio.run, self.send_alert(message=message, args=args))

    def warning(self, message: str, status_code: int = None, data=None):
        args = self.check_params(status_code, data)
        if args:
            self.logger.warning(message, args)
        else:
            self.logger.warning(message)

    def debug(self, message: str, status_code: int = None, data=None):
        args = self.check_params(status_code, data)
        if args:
            self.logger.debug(message, args)
        else:
            self.logger.debug(message)

    def info(self, message: str, status_code: int = None, data=None):
        args = self.check_params(status_code, data)
        if args:
            self.logger.info(message, args)
        else:
            self.logger.info(message)

    def http(self, message: str, status_code: int = None, data=None):
        args = self.check_params(status_code, data)
        if args:
            self.logger.http(message, args)
        else:
            self.logger.http(message)

    def vault(self, appname: str):
        vault_host = os.environ.get("VAULT_HOST")
        vault_token = os.environ.get("VAULT_TOKEN")
        auth_headers = {"X-Vault-Token": vault_token}

        try:
            response = requests.get(f"{vault_host}v1/prd/data/alert-logger", headers=auth_headers)
            response = response.json()["data"]["data"]
            self.credentials = response[f"{appname}"]
            self.bot_token = response.get('bot_token')
            # self.url =  f"https://api.telegram.org/bot{}/sendMessage?parse_mode=HTML"
        except Exception:
            self.warning("Not faund app in vault alertconfig")
   
    def send_alert(self, message: str, status_code: int = None, data=None, args=None):

        credentials = self.credentials

        bot = telebot.TeleBot(self.bot_token)

        alert_title = f"❌ <b>{credentials.get('name').upper()} - LOG ALERT</b> ❌\n"
        status = f"\n<b>Status Code:</b> {args.get('status')}" if args.get("status") else ""
        error_message = f"\n<b>Message:</b> {message}"
        error = f"\n<b>Error:</b> <code>{json.dumps(args.get('data'))}</code>" if args.get("data") else ""
        dashboard_link = f"\n<b>Dashboard:</b> <a href='{credentials.get('dasboard_link')}'>Link</a>" if credentials.get("dasboard_link") else ""
        body = f"{alert_title}{error_message}{status}{error}{dashboard_link}"
        payload = {"chat_id": credentials.get('chat_id'), "text": body}
        
        try:
            # asyncio.run(self.send_message(self.url, payload))
            bot.send_message(credentials.get("chat_id"), "Test 01")
        except Exception:
            self.warning("Not pasrsing data for send alert in telegram")

    # async def send_message(self, url: str, payload: dict):
    #     # requests.post(url=url, data=payload)
    #     # async with aiohttp.ClientSession() as session:
    #     await aiohttp.ClientSession().post(url=url, data=payload)

if __name__ == "__main__":
    inicio =time.time()
    logger = PyLogger(appname="test")
    
    logger.error(message="deu ruim", data={"error": "errror"}, status_code=500)
    fim = time.time()
    print(fim - inicio)
