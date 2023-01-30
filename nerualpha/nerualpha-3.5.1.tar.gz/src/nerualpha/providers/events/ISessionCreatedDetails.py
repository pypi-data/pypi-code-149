from dataclasses import dataclass, field, asdict
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod



#interface
class ISessionCreatedDetails(ABC):
    expiresAt:str
