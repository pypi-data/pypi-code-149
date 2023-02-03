"""Common index types."""

from __future__ import annotations

from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field
from collections import namedtuple
from typing import Any, Dict, Optional, List, Type, Union, Set

from dep_mongo import Indexed, MongoModel, Link
from pydantic import AnyUrl, BaseModel, Field


TypePK = int
TypeLang = str

TypeDigest = str
TypeName = str
TypeReason = str

TypeTranslate = str
TypeI18Field = Dict[TypeLang, TypeTranslate]

TypeDoc = Type[Union[Any, BaseModel]]
Type18nDoc = Dict[TypeLang, TypeDoc]
TypeLookup = Dict[TypePK, Type18nDoc]

TypeRequestID = Union[str, int, None]
TypeRequestParams = Union[Dict[str, Any], None]
TypeSorting = Dict[str, int]

TypeRawName = str
TypeSchemaRaw = Dict
TypeSchemaSrc = Dict

TypeGist = namedtuple(
    'TypeGist',
    ['name', 'raw', 'src', 'method', 'model', 'parser'],
)

TypeIndexSchema = Dict[TypeRawName, TypeGist]


class QuerySchema(BaseModel):
    """Base query schema."""

    page: Optional[int] = 1
    limit: Optional[int] = 25

    lang: Optional[str] = 'ru'

    expression: Optional[Dict] = None
    sorting: TypeSorting = None


class StrictSecureQuerySchema(QuerySchema):
    """Strict secure query schema."""

    token: str
    version: TypeDigest


class ImportQuerySecureSchema(BaseModel):
    """Strict secure query schema."""

    token: str
    version: TypeDigest


class SecureQuery(BaseModel):
    """Query schema."""

    token: str


class PaginatedResponse(BaseModel):
    """Paginated response - overload your results."""

    page: int = Field(example=1)
    limit: int = Field(example=25)
    count: int = Field(example=25)
    last_page: int = Field(example=5)
    total: int = Field(example=125)

    results: List[Dict]


class SizedImages(BaseModel):
    """Sizes images schema."""

    src: Optional[AnyUrl] = None
    sm: Optional[AnyUrl] = None
    md: Optional[AnyUrl] = None
    lg: Optional[AnyUrl] = None

    src_market: Optional[AnyUrl] = None
    sm_market: Optional[AnyUrl] = None
    md_market: Optional[AnyUrl] = None
    lg_market: Optional[AnyUrl] = None


class Meta(BaseModel):
    """Meta schema."""

    pk: int
    lang: str

    checksum: TypeDigest
    commit: TypeDigest
    branch: TypeDigest


class BaseSource(BaseModel):
    """Any removable type source."""

    delete: Optional[bool] = False
    hidden: Optional[bool] = False
    is_hidden: Optional[bool] = False
    is_delete: Optional[bool] = False


class TypeSource(BaseSource):
    """Type source."""

    @classmethod
    def exclude_fields(cls) -> Set[str]:
        """Not used fields."""

        return {
            'id',
            'delete',
            'is_delete',
            'is_deleted',
            'hidden',
            'is_hidden',
        }

    @classmethod
    def __normalize__(cls, source: BaseModel) -> Dict[str, Any]:
        """Normalize source data.  Override in child model if needed.

        Accepts validated source.
        Returns a normalized dict for raw model constructor, except meta.
        """

        normalized = source.dict(exclude=cls.exclude_fields())
        return normalized


class TypeRaw(MongoModel):
    """Base raw schema."""

    meta: Meta

    @classmethod
    def __normalize__(cls, normalized_doc: Dict, meta: Meta):
        """Raw doc normalizer.  Override in child model if needed.

        Accepts clean and normalized for raw model dict, except meta.
        Returns raw model instance from raw doc.
        """

        normalized_doc.update({'meta': meta})

        return cls(**normalized_doc)


@dataclass(frozen=True)
class DataRequest:
    """Request data."""

    method: TypeName
    params: TypeRequestParams = field(default_factory=dict)

    id: TypeRequestID = 'unnamed'

    __rpc_version__ = '2.0'

    def as_dict(self) -> Dict:
        """Request obj as dict."""

        return {
            'id': self.id,
            'jsonrpc': self.__rpc_version__,
            'method': self.method,
            'params': self.params,
        }


@dataclass(frozen=True)
class DataResponse:
    """Response data."""

    request: DataRequest
    execution_time_sec: int
    status: int

    result: Optional[Dict] = None


class CommitStatus(str, Enum):
    """Commit status."""

    new = 'new'
    prepare = 'prepare'
    ready = 'ready'
    fail = 'fail'


class DocState(str, Enum):
    """Merge doc state."""

    create = 'create'
    modify = 'modify'
    steady = 'steady'
    unwant = 'unwant'

    @staticmethod
    def request_merges(
        request: MergeRequest,
    ) -> Dict[DocState, List[DocMerge]]:
        """Get request merges by state."""

        states = dict()
        for pk, merge in request.changes.items():
            if merge.alter not in states.keys():
                states[merge.alter] = list()
            states[merge.alter].append(merge)
        return states


class DocMerge(BaseModel):
    """Document merge."""

    pk: int
    alter: DocState
    checksum: Union[None, TypeDigest]
    doc: Union[None, Dict[str, BaseModel]]


class Branch(MongoModel):
    """Branch."""

    digest: Indexed(str, unique=True)
    backward: TypeDigest

    definitions: Dict[str, Dict]
    changes: List[str]
    switch_at: datetime

    class Config:  # noqa

        name = 'Branch'


class MergeRequest(MongoModel):
    """MergeRequest."""

    digest: TypeDigest
    gist: TypeName
    branch: Link['Branch']
    changes: Dict[str, DocMerge]
    pull_at: datetime

    class Config:  # noqa

        name = 'MergeRequest'


class Commit(MongoModel):
    """Commit merge changes."""

    digest: TypeDigest
    request: Link['MergeRequest']
    backward: TypeDigest

    persistent: Optional[Dict[str, List[int]]]
    comments: Optional[List[str]]
    commit_at: datetime

    status: CommitStatus

    class Config:  # noqa

        name = 'Index'
