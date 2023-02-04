"""Shared definitions."""

from ..internals import fn
# from .digest import fn

from ..internals.builtins import ( # noqa
    TypeDigest,
    TypeGist,
    TypeIndexSchema,
    ImportQuerySecureSchema,
    StrictSecureQuerySchema,
    SecureQuery,
)

from ..schemas.raws import TypeTag  # noqa
from ..schemas.sources import SourceTag, TagEventCategory  # noqa


lang_base = 'ru'
IndexLanguages = {
    lang_base: 'ru_RU',
    'en': 'en_US',
}

lang_foreign_only = list(IndexLanguages.keys())[1:]
all_languages = [lang_base, *lang_foreign_only]

fallback_digest = '000000'

IndexNameTag = 'Tag'

'''
_index_meta = {
    IndexNameTag: TypeGist(
        name=IndexNameTag,
        method='raw_tags',
        raw=Tag.schema(),
        model=Tag,
        parser=SourceTag,
        src=SourceTag.schema(),
    ),
}
'''


_index_meta = {
    IndexNameTag: TypeGist(
        name=IndexNameTag,
        method='raw_tags',
        raw=TypeTag.schema(),
        parser=SourceTag,
        src=SourceTag.schema(),
        model=None,
    ),
}


IndexMeta = _index_meta
branch_digest = fn.digest_branch(languages=all_languages, schema=_index_meta)
