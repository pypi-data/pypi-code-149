from typing import TypedDict, Optional
from enum import Enum


class Status(Enum):
    Future = "future"
    Active = "active"
    Security = "security"
    EndOfLife = "end-of-life"


class Link(TypedDict):
    type: str
    rel: str
    href: str


class LaravelVersion(TypedDict):
    major: int
    latest_minor: int
    latest_patch: int
    latest: str
    is_lts: bool
    released_at: str
    ends_bugfixes_at: Optional[str]
    ends_securityfixes_at: Optional[str]
    status: Status
    links: list[Link]


class LaravelVersionsCollection(TypedDict):
    data: list[LaravelVersion]


class LaravelVersionsSingular(TypedDict):
    data: LaravelVersion
