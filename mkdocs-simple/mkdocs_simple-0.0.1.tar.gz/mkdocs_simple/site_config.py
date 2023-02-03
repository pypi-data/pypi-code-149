from dataclasses import dataclass
from typing import Optional


@dataclass
class SiteConfig:
    site_name: str
    site_url: Optional[str]
    site_description: str
    copyright: Optional[str]  # noqa:A003
    repo_name: Optional[str]
    repo_url: Optional[str]
    edit_url: Optional[str]
