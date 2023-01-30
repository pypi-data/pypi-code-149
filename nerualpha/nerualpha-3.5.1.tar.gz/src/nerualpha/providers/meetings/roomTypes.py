from dataclasses import dataclass, field, asdict
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod


class RoomTypes:
    Instant = "instant"
    LongTerm = "long_term"
