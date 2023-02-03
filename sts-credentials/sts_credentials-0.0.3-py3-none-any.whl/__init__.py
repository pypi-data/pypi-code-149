from sts_credentials.credentials.oss import get_credential_oss
from sts_credentials.credentials.cos import get_credential_cos
from sts_credentials.utils.decorators import ttl_lru_cache

__version__ = "0.0.3"
__all__ = [
    "get_credential_oss",
    "get_credential_cos",
    "ttl_lru_cache",
]
