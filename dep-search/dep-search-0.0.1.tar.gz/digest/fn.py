"""Digest tools."""

from typing import Any, Dict, Sequence, Union

from logging import getLogger
from json import JSONEncoder, dumps
from hashlib import sha1

from pydantic import BaseModel

from shared.dep_search import shared_types

_digest_len = 7

log = getLogger(__name__)


class SafeEncoder(JSONEncoder):
    """Safe type json encode."""

    def default(self, obj):
        """Fallback encode."""
        return str(obj)


def digest(text: str) -> shared_types.TypeDigest:
    """Text digest."""

    hash_object = sha1(text.encode())
    return hash_object.hexdigest()[0: _digest_len]


def digest_dict(mapping: Dict) -> shared_types.TypeDigest:
    """Digest mapping."""

    return digest(
        dumps(mapping, sort_keys=True, ensure_ascii=False, cls=SafeEncoder),
    )


def digest_doc(
    doc: Dict[str, Union[BaseModel, Any]],
) -> shared_types.TypeDigest:
    """Digest doc."""

    return digest_dict({lang: i18n.dict() for lang, i18n in doc.items()})


def digest_gist(
    gist: shared_types.TypeGist,
) -> shared_types.TypeDigest:
    """Digest gist."""

    return digest_dict({
        'name': gist.name,
        'raw': gist.raw,
        'src': gist.src,
    })


def digest_branch(
    languages: Sequence[str],
    schema: shared_types.TypeIndexSchema,
) -> shared_types.TypeDigest:
    """Digest branch."""

    index_meta = {alias: digest_gist(gist) for alias, gist in schema.items()}
    return digest_dict({'languages': languages, 'meta': index_meta})


def digest_merge(merge: Dict[int, Any]) -> shared_types.TypeDigest:
    """Digest merge request."""

    return digest_dict({_: merge.checksum for _, merge in merge.items()})
