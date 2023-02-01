# -*- coding: UTF-8 -*-

from json import loads, dumps
from logging import getLogger, Logger, StreamHandler, Formatter, DEBUG
from threading import Thread

from websocket import WebSocketApp

from .authentication import WSAuth
from .constants import MARKET_DATA, DIRECT_MARKET_DATA
from .utils import WSQueue


# noinspection PyUnusedLocal
class MarketData(object):
    """Websocket client session handler."""

    # create a logger and set level to debug:
    _log: Logger = getLogger(__name__)
    _log.setLevel(DEBUG)

    # create console handler and set level to debug:
    _console = StreamHandler()
    _console.setLevel(DEBUG)

    # create formatter:
    _formatter = Formatter(
        "[%(asctime)s] - %(levelname)s - <%(filename)s, %(lineno)d, %(funcName)s>: %(message)s"
    )

    # add formatter to console:
    _console.setFormatter(_formatter)

    # add console to logger:
    _log.addHandler(_console)

    _hostnames: dict = MARKET_DATA

    def __init__(
            self,
            environment: str = "production",
            debug: bool = False,
            logger: Logger = None,
            **kwargs
    ):
        """
        **kwargs:**
            - channels: list
            - product_ids: list

        :param environment: The API environment: `production` or `sandbox`
            (defaults to: `production`).
        :param debug: Set to True to log all requests/responses to/from server
            (defaults to: `False`).
        :param logger: The handler to be used for logging.
        :param kwargs: Websocket subscription parameters.
        """

        self._params = kwargs
        self._queue = WSQueue()
        self._debug = debug

        if logger is not None:
            self._log = logger

        self.debug("Creating a new websocket client instance...")

        self._websocket = WebSocketApp(
            url=f"wss://{self._hostnames.get(environment)}",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )

    @property
    def queue(self) -> WSQueue:
        return self._queue

    def listen(self, *args, **kwargs):
        """Start the listener."""
        thread = Thread(
            target=self._websocket.run_forever,
            name="websocket",
            args=args,
            kwargs=kwargs
        )
        thread.start()
        self.debug("Listening for websocket client messages...")

    def close(self):
        self.unsubscribe(self._websocket)
        self._websocket.close()
        self._queue.close()

    def on_open(self, websocket: WebSocketApp):
        """Action taken on websocket open event."""
        self.subscribe(websocket)

    def on_message(self, websocket: WebSocketApp, message: str):
        """Action taken for each message received."""
        message = loads(message)

        if message.get("type").lower() == "error":
            self._log.error(f"{message.get('message')}! {message.get('reason')}!")
            self.close()
            self.debug("The websocket client instance was terminated.")

        self._queue.put(message)

    def on_close(self, websocket: WebSocketApp, status, reason):
        """Action taken on websocket close event."""
        self.debug("The websocket client instance was terminated.")

    def on_error(self, websocket: WebSocketApp, exception):
        """Action taken when exception occurs."""
        self._log.error("Websocket client failed!", exc_info=exception)

    def subscribe(self, websocket: WebSocketApp):
        self.debug(f"Subscribing to: {dumps(self._params)}")
        params = dict(type="subscribe", **self._params)
        websocket.send(dumps(params))

    def unsubscribe(self, websocket: WebSocketApp):
        self.debug(f"Unsubscribing from: {dumps(self._params)}")
        params = dict(type="unsubscribe", **self._params)
        websocket.send(dumps(params))

    def debug(self, message: str):
        if self._debug is True:
            self._log.debug(message)


class DirectMarketData(MarketData):
    """Websocket client session handler."""

    _hostnames: dict = DIRECT_MARKET_DATA

    def __init__(
            self,
            key: str,
            passphrase: str,
            secret: str,
            environment: str = "production",
            debug: bool = False,
            logger: Logger = None,
            **kwargs
    ):
        """
        **kwargs:**
            - channels: list
            - product_ids: list

        :param key: The API key;
        :param passphrase: The API passphrase;
        :param secret: The API secret;
        :param environment: The API environment: `production` or `sandbox`
            (defaults to: `production`).
        :param debug: Set to True to log all requests/responses to/from server
            (defaults to: `False`).
        :param logger: The handler to be used for logging.
        :param kwargs: Websocket subscription parameters.
        """
        self.__hmac = WSAuth(key=key, passphrase=passphrase, secret=secret)
        super(DirectMarketData, self).__init__(environment, debug, logger, **kwargs)

    def subscribe(self, websocket: WebSocketApp):
        self.debug(f"Subscribing to: {dumps(self._params)}")
        params = dict(type="subscribe", **self._params)
        self.__hmac.sign("GET", "/users/self/verify", params)
        websocket.send(dumps(params))


__all__ = ["MarketData", "DirectMarketData"]
