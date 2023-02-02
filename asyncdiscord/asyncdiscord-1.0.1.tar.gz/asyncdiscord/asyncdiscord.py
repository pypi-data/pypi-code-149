from __future__ import annotations
import datetime
import json
import logging
import time
from contextlib import asynccontextmanager
from functools import partial
from typing import Any, Dict, List, cast, TYPE_CHECKING, Optional, Tuple, Union
import requests
import colorsys
import random
import re

if TYPE_CHECKING:
    from typing_extensions import Self
logger = logging.getLogger(__name__)

try:
    import httpx
except ImportError:
    pass


class ColorNotInRangeException(Exception):
    """
    A valid color must take an integer value between 0 and 16777216 inclusive.
    This Exception will be raised when a colour is not in that range.
    """
    color: Union[str, int]

    def __init__(self, color: Union[str, int]) -> None:
        self.color = color
        super().__init__()

    def __str__(self) -> str:
        return repr(
            f"{self.color!r} is not in valid range of colors. The valid ranges "
            "of colors are 0 to 16777215 inclusive (INTEGERS) and 0 "
            "to FFFFFF inclusive (HEXADECIMAL)"
        )


__all__ = (
    'Webhook',
    'DiscordWebhook',
    'DiscordEmbed',
    'DiscordColor',
    'Color',
)

RGB_REGEX = re.compile(r'rgb\s*\((?P<r>[0-9.]+%?)\s*,\s*(?P<g>[0-9.]+%?)\s*,\s*(?P<b>[0-9.]+%?)\s*\)')


def parse_hex_number(argument: str) -> DiscordColor:
    arg = ''.join(i * 2 for i in argument) if len(argument) == 3 else argument
    try:
        value = int(arg, base=16)
        if not (0 <= value <= 0xFFFFFF):
            raise ValueError('hex number out of range for 24-bit colour')
    except ValueError:
        raise ValueError('invalid hex digit given') from None
    else:
        return Color(value=value)


def parse_rgb_number(number: str) -> int:
    if number[-1] == '%':
        value = float(number[:-1])
        if not (0 <= value <= 100):
            raise ValueError('rgb percentage can only be between 0 to 100')
        return round(255 * (value / 100))

    value = int(number)
    if not (0 <= value <= 255):
        raise ValueError('rgb number can only be between 0 to 255')
    return value


def parse_rgb(argument: str, *, regex: re.Pattern[str] = RGB_REGEX) -> DiscordColor:
    match = regex.match(argument)
    if match is None:
        raise ValueError('invalid rgb syntax found')

    red = parse_rgb_number(match.group('r'))
    green = parse_rgb_number(match.group('g'))
    blue = parse_rgb_number(match.group('b'))
    return Color.from_rgb(red, green, blue)


class DiscordColor:
    """Represents a Discord role colour. This class is similar
    to a (red, green, blue) :class:`tuple`.
    There is an alias for this called Color.
    .. container:: operations
        .. describe:: x == y
             Checks if two colours are equal.
        .. describe:: x != y
             Checks if two colours are not equal.
        .. describe:: hash(x)
             Return the colour's hash.
        .. describe:: str(x)
             Returns the hex format for the colour.
        .. describe:: int(x)
             Returns the raw colour value.
    Attributes
    ------------
    value: :class:`int`
        The raw integer colour value.
    """

    __slots__ = ('value',)

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f'Expected int parameter, received {value.__class__.__name__} instead.')

        self.value: int = value

    def _get_byte(self, byte: int) -> int:
        return (self.value >> (8 * byte)) & 0xFF

    def __eq__(self, other: object) -> bool:
        return isinstance(other, DiscordColor) and self.value == other.value

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f'#{self.value:0>6x}'

    def __int__(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f'<DiscordColor value={self.value}>'

    def __hash__(self) -> int:
        return hash(self.value)

    @property
    def r(self) -> int:
        """:class:`int`: Returns the red component of the colour."""
        return self._get_byte(2)

    @property
    def g(self) -> int:
        """:class:`int`: Returns the green component of the colour."""
        return self._get_byte(1)

    @property
    def b(self) -> int:
        """:class:`int`: Returns the blue component of the colour."""
        return self._get_byte(0)

    def to_rgb(self) -> Tuple[int, int, int]:
        """Tuple[:class:`int`, :class:`int`, :class:`int`]: Returns an (r, g, b) tuple representing the colour."""
        return (self.r, self.g, self.b)

    @classmethod
    def from_rgb(cls, r: int, g: int, b: int) -> Self:
        """Constructs a :class:`DiscordColor` from an RGB tuple."""
        return cls((r << 16) + (g << 8) + b)

    @classmethod
    def from_hsv(cls, h: float, s: float, v: float) -> Self:
        """Constructs a :class:`DiscordColor` from an HSV tuple."""
        rgb = colorsys.hsv_to_rgb(h, s, v)
        return cls.from_rgb(*(int(x * 255) for x in rgb))

    @classmethod
    def from_str(cls, value: str) -> Self:
        """Constructs a :class:`DiscordColor` from a string.
        The following formats are accepted:
        - ``0x<hex>``
        - ``#<hex>``
        - ``0x#<hex>``
        - ``rgb(<number>, <number>, <number>)``
        Like CSS, ``<number>`` can be either 0-255 or 0-100% and ``<hex>`` can be
        either a 6 digit hex number or a 3 digit hex shortcut (e.g. #fff).
        Raises
        -------
        ValueError
            The string could not be converted into a colour.
        """

        if value[0] == '#':
            return parse_hex_number(value[1:])

        if value[0:2] == '0x':
            rest = value[2:]
            # Legacy backwards compatible syntax
            if rest.startswith('#'):
                return parse_hex_number(rest[1:])
            return parse_hex_number(rest)

        arg = value.lower()
        if arg[0:3] == 'rgb':
            return parse_rgb(arg)

        raise ValueError('unknown colour format given')

    @classmethod
    def default(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0``."""
        return cls(0)

    @classmethod
    def random(cls, *, seed: Optional[Union[int, str, float, bytes, bytearray]] = None) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a random hue.
        .. note::
            The random algorithm works by choosing a colour with a random hue but
            with maxed out saturation and value.
        .. versionadded:: 1.6
        Parameters
        ------------
        seed: Optional[Union[:class:`int`, :class:`str`, :class:`float`, :class:`bytes`, :class:`bytearray`]]
            The seed to initialize the RNG with. If ``None`` is passed the default RNG is used.
        """
        rand = random if seed is None else random.Random(seed)
        return cls.from_hsv(rand.random(), 1, 1)

    @classmethod
    def teal(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x1abc9c``."""
        return cls(0x1ABC9C)

    @classmethod
    def dark_teal(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x11806a``."""
        return cls(0x11806A)

    @classmethod
    def brand_green(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x57F287``.
        """
        return cls(0x57F287)

    @classmethod
    def green(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x2ecc71``."""
        return cls(0x2ECC71)

    @classmethod
    def dark_green(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x1f8b4c``."""
        return cls(0x1F8B4C)

    @classmethod
    def blue(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x3498db``."""
        return cls(0x3498DB)

    @classmethod
    def dark_blue(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x206694``."""
        return cls(0x206694)

    @classmethod
    def purple(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x9b59b6``."""
        return cls(0x9B59B6)

    @classmethod
    def dark_purple(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x71368a``."""
        return cls(0x71368A)

    @classmethod
    def magenta(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xe91e63``."""
        return cls(0xE91E63)

    @classmethod
    def dark_magenta(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xad1457``."""
        return cls(0xAD1457)

    @classmethod
    def gold(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xf1c40f``."""
        return cls(0xF1C40F)

    @classmethod
    def dark_gold(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xc27c0e``."""
        return cls(0xC27C0E)

    @classmethod
    def orange(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xe67e22``."""
        return cls(0xE67E22)

    @classmethod
    def dark_orange(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xa84300``."""
        return cls(0xA84300)

    @classmethod
    def brand_red(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xED4245``.
        """
        return cls(0xED4245)

    @classmethod
    def red(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xe74c3c``."""
        return cls(0xE74C3C)

    @classmethod
    def dark_red(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x992d22``."""
        return cls(0x992D22)

    @classmethod
    def lighter_grey(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x95a5a6``."""
        return cls(0x95A5A6)

    lighter_gray = lighter_grey

    @classmethod
    def dark_grey(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x607d8b``."""
        return cls(0x607D8B)

    dark_gray = dark_grey

    @classmethod
    def light_grey(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x979c9f``."""
        return cls(0x979C9F)

    light_gray = light_grey

    @classmethod
    def darker_grey(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x546e7a``."""
        return cls(0x546E7A)

    darker_gray = darker_grey

    @classmethod
    def og_blurple(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x7289da``."""
        return cls(0x7289DA)

    @classmethod
    def blurple(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x5865F2``."""
        return cls(0x5865F2)

    @classmethod
    def greyple(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x99aab5``."""
        return cls(0x99AAB5)

    @classmethod
    def dark_theme(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0x36393F``.
        This will appear transparent on Discord's dark theme.
        """
        return cls(0x36393F)

    @classmethod
    def fuchsia(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xEB459E``.
        """
        return cls(0xEB459E)

    @classmethod
    def yellow(cls) -> Self:
        """A factory method that returns a :class:`DiscordColor` with a value of ``0xFEE75C``.
        """
        return cls(0xFEE75C)


Color = DiscordColor


class DiscordEmbed:
    """
    Discord Embed
    """
    title: Optional[str]
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[str]
    color: Optional[int]
    footer: Optional[Dict[str, Optional[str]]]
    image: Optional[Dict[str, Optional[Union[str, int]]]]
    thumbnail: Optional[Union[str, Dict[str, Optional[Union[str, int]]]]]
    video: Optional[Union[str, Dict[str, Optional[Union[str, int]]]]]
    provider: Optional[Dict[str, Any]]
    author: Optional[Dict[str, Optional[str]]]
    fields: List[Dict[str, Optional[Any]]]

    def __init__(
            self,
            title: Optional[str] = None,
            description: Optional[str] = None,
            **kwargs: Any,
    ) -> None:
        """
        Init Discord Embed

        :keyword ``title:`` title of embed\n
        :keyword ``description:`` description body of embed\n
        :keyword ``url:`` add an url to make your embedded title a clickable
        link\n
        :keyword ``timestamp:`` timestamp of embed content\n
        :keyword ``color:`` color code of the embed as int\n
        :keyword ``footer:`` footer texts\n
        :keyword ``image:`` your image url here\n
        :keyword ``thumbnail:`` your thumbnail url here\n
        :keyword ``video:``  to apply video with embedded, your video source
        url here\n
        :keyword ``provider:`` provider information\n
        :keyword ``author:`` author information\n
        :keyword ``fields:`` fields information
        """
        self.title = title
        self.description = description
        self.url = cast(str, kwargs.get("url"))
        self.timestamp = cast(str, kwargs.get("timestamp"))
        self.footer = kwargs.get("footer")
        self.image = kwargs.get("image")
        self.thumbnail = kwargs.get("thumbnail")
        self.video = kwargs.get("video")
        self.provider = kwargs.get("provider")
        self.author = kwargs.get("author")
        self.fields = kwargs.get("fields", [])
        self.set_color(kwargs.get("color"))

    def set_title(self, title: str) -> None:
        """
        set title of embed

        :param title: title of embed
        """
        self.title = title

    def set_description(self, description: str) -> None:
        """
        set description of embed

        :param description: description of embed
        """
        self.description = description

    def set_url(self, url: str) -> None:
        """
        set url of embed

        :param url: url of embed
        """
        self.url = url

    def set_timestamp(self, timestamp: Optional[float] = None) -> None:
        """
        set timestamp of embed content

        :param timestamp: (optional) timestamp of embed content
        """
        if timestamp is None:
            timestamp = time.time()
        self.timestamp = str(datetime.datetime.utcfromtimestamp(timestamp))

    def set_color(self, color: DiscordColor) -> None:
        """
        set color code of the embed as decimal(int) or hex(string)

        :param color: color code of the embed as decimal(int) or hex(string)
        """
        self.color = int(color.value, 16) if isinstance(color.value, str) else color.value
        if self.color is not None and self.color not in range(16777216):
            raise ColorNotInRangeException(color.value)

    def set_footer(self, **kwargs: str) -> None:
        """
        set footer information of embed

        :keyword text: footer text
        :keyword icon_url: url of footer icon (only supports http(s) and
        attachments)
        :keyword proxy_icon_url: a proxied url of footer icon
        """
        self.footer = {
            "text": kwargs.get("text"),
            "icon_url": kwargs.get("icon_url"),
            "proxy_icon_url": kwargs.get("proxy_icon_url"),
        }

    def set_image(self, url: str, **kwargs: Union[str, int]) -> None:
        """
        set image of embed

        :param url: source url of image (only supports http(s) and attachments)
        :keyword proxy_url: a proxied url of the image
        :keyword height: height of image
        :keyword width: width of image
        """
        self.image = {
            "url": url,
            "proxy_url": cast(Optional[str], kwargs.get("proxy_url")),
            "height": cast(Optional[int], kwargs.get("height")),
            "width": cast(Optional[int], kwargs.get("width")),
        }

    def set_thumbnail(self, url: str, **kwargs: Union[str, int]) -> None:
        """
        set thumbnail of embed

        :param url: source url of thumbnail (only supports http(s) and
        attachments)
        :keyword proxy_url: a proxied thumbnail of the image
        :keyword height: height of thumbnail
        :keyword width: width of thumbnail
        """
        self.thumbnail = {
            "url": url,
            "proxy_url": cast(Optional[str], kwargs.get("proxy_url")),
            "height": cast(Optional[int], kwargs.get("height")),
            "width": cast(Optional[str], kwargs.get("width")),
        }

    def set_video(self, **kwargs: Union[str, int]) -> None:
        """
        set video of embed

        :keyword url: source url of video
        :keyword height: height of video
        :keyword width: width of video
        """
        self.video = {
            "url": cast(Optional[str], kwargs.get("url")),
            "height": cast(Optional[int], kwargs.get("height")),
            "width": cast(Optional[int], kwargs.get("width")),
        }

    def set_provider(self, **kwargs: str) -> None:
        """
        set provider of embed

        :keyword name: name of provider
        :keyword url: url of provider
        """
        self.provider = {
            "name": kwargs.get("name"),
            "url": kwargs.get("url"),
        }

    def set_author(self, name: str, **kwargs: str) -> None:
        """
        set author of embed

        :param name: name of author
        :keyword url: url of author
        :keyword icon_url: url of author icon (only supports http(s) and
        attachments)
        :keyword proxy_icon_url: a proxied url of author icon
        """
        self.author = {
            "name": name,
            "url": kwargs.get("url"),
            "icon_url": kwargs.get("icon_url"),
            "proxy_icon_url": kwargs.get("proxy_icon_url"),
        }

    def add_field(self, name: str, value: str,
                  inline: bool = True) -> None:
        """
        set field of embed

        :param name: name of the field
        :param value: value of the field
        :param inline: (optional) whether this field should display inline
        """
        self.fields.append(
            {
                "name": name,
                "value": value,
                "inline": inline,
            }
        )

    def del_embed_field(self, index: int) -> None:
        """
        remove field from `self.fields`

        :param index: index of field in `self.fields`
        """
        self.fields.pop(index)

    def get_embed_fields(self) -> List[Dict[str, Optional[Any]]]:
        """
        get all `self.fields` as list

        :return: `self.fields`
        """
        return self.fields


class DiscordWebhook:
    """
    Webhook for Discord
    """

    url: Optional[Union[str, List[str]]]
    content: Optional[Union[str, bytes]]
    username: Optional[str]
    avatar_url: Optional[str]
    tts: bool
    files: Dict[str, Tuple[Optional[str], Union[bytes, str]]]
    embeds: List[Dict[str, Any]]
    proxies: Optional[Dict[str, str]]
    allowed_mentions: List[str]
    timeout: Optional[float]
    rate_limit_retry: bool = False

    def __init__(
            self,
            url: Optional[Union[str, List[str]]] = None,
            *,
            content: Optional[str] = None,
            username: Optional[str] = None,
            avatar_url: Optional[str] = None,
            tts: bool = False,
            files: Optional[
                Dict[str, Tuple[Optional[str], Union[bytes, str]]]] = None,
            embeds: Optional[List[Dict[str, Any]]] = None,
            proxies: Optional[Dict[str, str]] = None,
            timeout: Optional[float] = None,
            rate_limit_retry: bool = False,
            allowed_mentions: Optional[List[str]] = None,
    ) -> None:
        """
        Init Webhook for Discord

        :param ``url``: your discord webhook url (type: str, list)\n
        :keyword ``content:`` the message contents (type: str)\n
        :keyword ``username:`` override the default username of the webhook\n
        :keyword ``avatar_url:`` override the default avatar of the webhook\n
        :keyword ``tts:`` true if this is a TTS message\n
        :keyword ``file``: to apply file(s) with message
        (For example: file=f.read() (here, f = variable that contain
        attachement path as "rb" mode))\n
        :keyword ``filename:`` apply custom file name on attached file
        content(s)\n
        :keyword ``embeds:`` list of embedded rich content\n
        :keyword ``allowed_mentions:`` allowed mentions for the message\n
        :keyword ``proxies:`` dict of proxies\n
        :keyword ``timeout:`` (optional) amount of seconds to wait for a
        response from Discord
        """
        if embeds is None:
            embeds = []
        if files is None:
            files = {}
        if allowed_mentions is None:
            allowed_mentions = []
        self.url = url
        self.content = content
        self.username = username
        self.avatar_url = avatar_url
        self.tts = tts
        self.files = files
        self.embeds = embeds
        self.proxies = proxies
        self.allowed_mentions = allowed_mentions
        self.timeout = timeout
        self.rate_limit_retry = rate_limit_retry

    def add_file(self, file: bytes, filename: str) -> None:
        """
        adds a file to the webhook

        :param file: file content
        :param filename: filename
        :return:
        """
        self.files[f"_{filename}"] = (filename, file)

    def add_embed(self, embed: Union[DiscordEmbed, Dict[str, Any]]) -> None:
        """
        adds an embedded rich content

        :param embed: embed object or dict
        """
        self.embeds.append(
            embed.__dict__ if isinstance(embed, DiscordEmbed) else embed)

    def remove_embed(self, index: int) -> None:
        """
        removes embedded rich content from `self.embeds`

        :param index: index of embed in `self.embeds`
        """
        self.embeds.pop(index)

    def remove_file(self, filename: str) -> None:
        """
        removes file from `self.files` using specified `filename` if it exists

        :param filename: filename
        """
        filename = f"_{filename}"
        if filename in self.files:
            del self.files[filename]

    def get_embeds(self) -> List[Dict[str, Any]]:
        """
        gets all self.embeds as list

        :return: self.embeds
        """
        return self.embeds

    def set_proxies(self, proxies: Dict[str, str]) -> None:
        """
        sets proxies

        :param proxies: dict of proxies
        :type proxies: dict
        """
        self.proxies = proxies

    def set_content(self, content: str) -> None:
        """
        sets content

        :param content: content string
        :type content: string
        """
        self.content = content

    @property
    def json(self) -> Dict[str, Any]:
        """
        convert webhook data to json

        :return webhook data as json:
        """
        embeds = self.embeds
        self.embeds = []
        for embed in embeds:
            self.add_embed(embed)
        data = {
            key: value
            for key, value in self.__dict__.items()
            if value and key not in {"url", "files", "filename"}
        }
        embeds_empty = not any(data["embeds"]) if "embeds" in data else True
        if embeds_empty and "content" not in data and bool(self.files) is False:
            logger.error("webhook message is empty! set content or embed data")
        return data

    def remove_embeds(self) -> None:
        """
        Sets `self.embeds` to empty `list`.
        """
        self.embeds = []

    def remove_files(self) -> None:
        """
        Sets `self.files` to empty `dict`.
        """
        self.files = {}

    def api_post_request(self, url: str) -> requests.Response:
        if bool(self.files) is False:
            response = requests.post(
                url,
                json=self.json,
                proxies=self.proxies,
                params={"wait": True},
                timeout=self.timeout,
            )
        else:
            self.files["payload_json"] = (None, json.dumps(self.json))
            response = requests.post(
                url,
                files=self.files,
                proxies=self.proxies,
                timeout=self.timeout,
            )
        return response

    def execute(
            self,
            remove_embeds: bool = False,
            remove_files: bool = False,
    ) -> Union[List[requests.Response], requests.Response]:
        """
        executes the Webhook

        :param remove_embeds: if set to True, calls `self.remove_embeds()`
        to empty `self.embeds` after webhook is executed
        :param remove_files: if set to True, calls `self.remove_files()`
        to empty `self.files` after webhook is executed
        :return: Webhook response
        """
        webhook_urls = self.url
        if isinstance(self.url, str):
            webhook_urls = [self.url]
        urls_len = len(webhook_urls)
        responses = []
        for i, url in enumerate(webhook_urls):
            response = self.api_post_request(url)
            if response.status_code in [200, 204]:
                logger.debug(f"[{i + 1}/{urls_len}] Webhook executed")
            elif response.status_code == 429 and self.rate_limit_retry:
                while response.status_code == 429:
                    errors = json.loads(response.content.decode("utf-8"))
                    wh_sleep = (int(errors["retry_after"]) / 1000) + 0.15
                    time.sleep(wh_sleep)
                    logger.error(
                        f"Webhook rate limited: sleeping for {wh_sleep} "
                        "seconds..."
                    )
                    response = self.api_post_request(url)
                    if response.status_code in [200, 204]:
                        logger.debug(f"[{i + 1}/{urls_len}] Webhook executed")
                        break
            else:
                logger.error(
                    f"[{i + 1}/{urls_len}] Webhook status code "
                    f"{response.status_code}: "
                    f"{response.content.decode('utf-8')}"
                )
            responses.append(response)
        if remove_embeds:
            self.remove_embeds()
        if remove_files:
            self.remove_files()
        return responses[0] if len(responses) == 1 else responses

    def edit(
            self,
            sent_webhook: Union[List[requests.Response], requests.Response],
    ) -> Union[List[requests.Response], requests.Response]:
        """
        edits the webhook passed as a response

        :param sent_webhook: webhook.execute() response
        :return: Another webhook response
        """
        if not isinstance(sent_webhook, list):
            sent_webhook = cast(List[requests.Response], [sent_webhook])
        responses: List[requests.Response] = []
        for i, webhook in enumerate(sent_webhook):
            assert isinstance(webhook.content, bytes)
            previous_sent_message_id = json.loads(
                webhook.content.decode("utf-8")
            )["id"]
            url = (
                    webhook.url.split("?")[0] + "/messages/" + str(
                previous_sent_message_id)
            )
            # removes any query params
            if bool(self.files) is False:
                request = partial(
                    requests.patch,
                    url,
                    json=self.json,
                    proxies=self.proxies,
                    params={"wait": True},
                    timeout=self.timeout,
                )
            else:
                self.files["payload_json"] = (None, json.dumps(self.json))
                request = partial(
                    requests.patch,
                    url,
                    files=self.files,
                    proxies=self.proxies,
                    timeout=self.timeout,
                )
            response = request()
            if response.status_code in [200, 204]:
                logger.debug(f"[{i + 1}/{len(sent_webhook)}] Webhook edited")
            elif response.status_code == 429 and self.rate_limit_retry:
                while response.status_code == 429:
                    errors = json.loads(response.content.decode("utf-8"))
                    wh_sleep = (int(errors["retry_after"]) / 1000) + 0.15
                    time.sleep(wh_sleep)
                    logger.error(
                        f"Webhook rate limited: sleeping for {wh_sleep} "
                        f"seconds..."
                    )
                    response = request()
                    if response.status_code in [200, 204]:
                        logger.debug(
                            f"[{i + 1}/{len(sent_webhook)}] Webhook edited")
                        break
            else:
                logger.error(
                    f"[{i + 1}/{len(sent_webhook)}] Webhook status code "
                    f"{response.status_code}: "
                    f"{response.content.decode('utf-8')}"
                )
            responses.append(response)
        return responses[0] if len(responses) == 1 else responses

    def delete(
            self, sent_webhook: Union[List["DiscordWebhook"], "DiscordWebhook"]
    ) -> Union[List[requests.Response], requests.Response]:
        """
        deletes the webhook passed as a response

        :param sent_webhook: webhook.execute() response
        :return: Response
        """
        if not isinstance(sent_webhook, list):
            sent_webhook = cast(List[DiscordWebhook], [sent_webhook])
        responses: List[requests.Response] = []
        for i, webhook in enumerate(sent_webhook):
            assert isinstance(webhook.content, bytes)
            url = webhook.url.split("?")[0]
            previous_sent_message_id = json.loads(
                webhook.content.decode("utf-8")
            )["id"]
            response = requests.delete(
                url + "/messages/" + str(previous_sent_message_id),
                proxies=self.proxies,
                timeout=self.timeout,
            )
            if response.status_code in [200, 204]:
                logger.debug(f"[{i + 1}/{len(sent_webhook)}] Webhook deleted")
            else:
                logger.error(
                    f"[{i + 1}/{len(sent_webhook)}] Webhook status code "
                    f"{response.status_code}: {response.content.decode('utf-8')}"
                )
            responses.append(response)
        return responses[0] if len(responses) == 1 else responses


class Webhook(DiscordWebhook):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            import httpx
        except ImportError:
            raise ImportError(
                "This version is async, but you dont have httpx module."
                " install it using `pip install httpx`."
            ) from None

    @property
    @asynccontextmanager
    async def http_client(self):
        """
        A property that returns an httpx.AsyncClient instance that is used for a 'with' statement.
        Example:
            async with self.http_client as client:
                client.post(url, data=data)
        It will automatically close the client when the context is exited.

        :return: httpx.AsyncClient
        """
        client = httpx.AsyncClient(proxies=self.proxies)
        yield client
        await client.aclose()

    async def api_post_request(self, url):
        async with self.http_client as client:  # type: httpx.AsyncClient
            if bool(self.files) is False:
                response = await client.post(url, json=self.json,
                                             params={'wait': True},
                                             timeout=self.timeout)
            else:
                self.files["payload_json"] = (None, json.dumps(self.json).encode('utf-8'))
                response = await client.post(url, files=self.files,
                                             timeout=self.timeout)
        return response

    async def execute(self, remove_embeds=False, remove_files=False):
        """
        executes the Webhook

        :param remove_embeds: if set to True, calls `self.remove_embeds()` to empty `self.embeds` after webhook is executed
        :param remove_files: if set to True, calls `self.remove_files()` to empty `self.files` after webhook is executed
        :return: Webhook response
        """
        webhook_urls = self.url if isinstance(self.url, list) else [self.url]
        urls_len = len(webhook_urls)
        responses = []
        for i, url in enumerate(webhook_urls):
            response = await self.api_post_request(url)
            if response.status_code in [200, 204]:
                logger.debug(
                    "[{index}/{length}] Webhook executed".format(
                        index=i + 1, length=urls_len
                    )
                )
            elif response.status_code == 429 and self.rate_limit_retry:
                while response.status_code == 429:
                    await self.handle_rate_limit(response)
                    response = await self.api_post_request(url)
                    if response.status_code in [200, 204]:
                        logger.debug(
                            "[{index}/{length}] Webhook executed".format(
                                index=i + 1, length=urls_len
                            )
                        )
                        break
            else:
                logger.error(
                    "[{index}/{length}] Webhook status code {status_code}: {content}".format(
                        index=i + 1,
                        length=urls_len,
                        status_code=response.status_code,
                        content=response.content.decode("utf-8"),
                    )
                )
            responses.append(response)
        if remove_embeds:
            self.remove_embeds()
        if remove_files:
            self.remove_files()
        return responses[0] if len(responses) == 1 else responses

    async def edit(self, sent_webhook):
        """
        edits the webhook passed as a response

        :param sent_webhook: webhook.execute() response
        :return: Another webhook response
        """
        sent_webhook = sent_webhook if isinstance(sent_webhook, list) else [sent_webhook]
        webhook_len = len(sent_webhook)
        responses = []
        async with self.http_client as client:  # type: httpx.AsyncClient
            for i, webhook in enumerate(sent_webhook):
                previous_sent_message_id = json.loads(webhook.content.decode('utf-8'))['id']
                url = webhook.url.split('?')[0] + '/messages/' + str(
                    previous_sent_message_id)  # removes any query params
                if bool(self.files) is False:
                    patch_kwargs = {'json': self.json, 'params': {'wait': True}, 'timeout': self.timeout}
                else:
                    self.files["payload_json"] = (None, json.dumps(self.json))
                    patch_kwargs = {'files': self.files, 'timeout': self.timeout}
                response = await client.patch(url, **patch_kwargs)
                if response.status_code in [200, 204]:
                    logger.debug(
                        "[{index}/{length}] Webhook edited".format(
                            index=i + 1,
                            length=webhook_len,
                        )
                    )
                elif response.status_code == 429 and self.rate_limit_retry:
                    while response.status_code == 429:
                        await self.handle_rate_limit(response)
                        response = await client.patch(url, **patch_kwargs)
                        if response.status_code in [200, 204]:
                            logger.debug(
                                "[{index}/{length}] Webhook edited".format(
                                    index=i + 1,
                                    length=webhook_len,
                                )
                            )
                            break
                else:
                    logger.error(
                        "[{index}/{length}] Webhook status code {status_code}: {content}".format(
                            index=i + 1,
                            length=webhook_len,
                            status_code=response.status_code,
                            content=response.content.decode("utf-8"),
                        )
                    )
                responses.append(response)
        return responses[0] if len(responses) == 1 else responses

    async def delete(self, sent_webhook):
        """
        deletes the webhook passed as a response

        :param sent_webhook: webhook.execute() response
        :return: Response
        """
        sent_webhook = sent_webhook if isinstance(sent_webhook, list) else [sent_webhook]
        webhook_len = len(sent_webhook)
        responses = []
        async with self.http_client as client:  # type: httpx.AsyncClient
            for i, webhook in enumerate(sent_webhook):
                url = webhook.url.split('?')[0]  # removes any query params
                previous_sent_message_id = json.loads(webhook.content.decode('utf-8'))['id']
                response = await client.delete(url + '/messages/' + str(previous_sent_message_id), timeout=self.timeout)
                if response.status_code in [200, 204]:
                    logger.debug(
                        "[{index}/{length}] Webhook deleted".format(
                            index=i + 1,
                            length=webhook_len,
                        )
                    )
                else:
                    logger.error(
                        "[{index}/{length}] Webhook status code {status_code}: {content}".format(
                            index=i + 1,
                            length=webhook_len,
                            status_code=response.status_code,
                            content=response.content.decode("utf-8"),
                        )
                    )
                responses.append(response)
        return responses[0] if len(responses) == 1 else responses

    async def handle_rate_limit(self, response):
        """
        handles the rate limit

        :param response: Response
        :return: Response
        """
        errors = response.json()
        wh_sleep = (int(errors['retry_after']) / 1000) + 0.1
        logger.error(
            "Webhook rate limited: sleeping for {wh_sleep} "
            "seconds...".format(
                wh_sleep=wh_sleep
            )
        )
        time.sleep(wh_sleep)
