"""Shared definitions."""

from ..internals import fn
# from .digest import fn

from ..internals.builtins import ( # noqa
    Branch,
    Commit,
    MergeRequest,
    TypeDigest,
    TypeGist,
    TypeIndexSchema,
    ImportQuerySecureSchema,
    StrictSecureQuerySchema,
    SecureQuery,
)

# from .schemas.raws.tag import Tag
from ..schemas.raw_tag import Tag
from ..schemas.src_tag import SourceTag, TagEventCategory  # noqa
# from .schemas.sources.tag import SourceTag, TagEventCategory  # noqa


lang_base = 'ru'
IndexLanguages = {
    lang_base: 'ru_RU',
    'en': 'en_US',
}

lang_foreign_only = list(IndexLanguages.keys())[1:]
all_languages = [lang_base, *lang_foreign_only]

fallback_digest = '000000'

IndexNameTag = 'Tag'

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


IndexMeta = _index_meta
branch_digest = fn.digest_branch(languages=all_languages, schema=_index_meta)


def internals():
    """Internal models."""

    return [Branch, Commit, MergeRequest]


def raws():
    """Raw models."""

    return [gist.model for name, gist in IndexMeta.items()]


init_models = (*internals(), *raws())
