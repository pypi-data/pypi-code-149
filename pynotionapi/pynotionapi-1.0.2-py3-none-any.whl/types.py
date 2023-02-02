from typing import Mapping, Optional, TypedDict, Union
from uuid import UUID

from pynotion.enums import (
    BlockType,
    DirectionType,
    EmojiType,
    FileType,
    FunctionType,
    MentionType,
    ParentType,
    RelationType,
    RichTextType,
)


class Sort(TypedDict):
    direction: Optional[DirectionType]
    property: Optional[str]
    timestamp: Optional[str]


class Filter(TypedDict):
    property: str
    value: str


class Pagination(TypedDict):
    start_cursor: Optional[str]
    page_size: Optional[int]


class Mention(TypedDict):
    type: Optional[MentionType]

    database: Optional[Mapping]
    date: Optional[Mapping]
    link_preview: Optional[Mapping]
    page: Optional[Mapping]
    template_mention: Optional[Mapping]
    user: Optional[Mapping]


class Equation(TypedDict):
    expression: str


class Annotation(TypedDict):
    bold: Optional[bool]
    italic: Optional[bool]
    strikethrough: Optional[bool]
    underline: Optional[bool]
    code: Optional[bool]
    color: Optional[str]


class RichText(TypedDict):
    type: Optional[RichTextType]

    text: Optional[Mapping]
    mention: Optional[Mention]
    equation: Optional[Equation]

    annotations: Optional[Annotation]
    plain_text: Optional[str]
    href: Optional[str]


class Number(TypedDict):
    format: Optional[str]


class SelectOptions(TypedDict):
    name: str
    color: Optional[str]


class Select(TypedDict):
    options: SelectOptions


class Formula(TypedDict):
    expression: str


class Relation(TypedDict):
    database_id: UUID
    type: Optional[RelationType]


class Rollup(TypedDict):
    relation_property_name: Optional[str]
    relation_property_id: Optional[str]

    rollup_property_name: Optional[str]
    rollup_property_id: Optional[str]

    function: Optional[FunctionType]


class Property(TypedDict):
    title: Optional[Mapping]
    rich_text: Optional[RichText]
    number: Optional[Number]
    select: Optional[Select]
    multi_select: Optional[Select]
    date: Optional[Mapping]
    people: Optional[Mapping]
    files: Optional[Mapping]
    checkbox: Optional[Mapping]
    url: Optional[Mapping]
    email: Optional[Mapping]
    phone_number: Optional[Mapping]
    formula: Optional[Formula]
    relation: Optional[Relation]
    rollup: Optional[Rollup]
    created_time: Optional[Mapping]
    created_by: Optional[Mapping]
    last_edited_time: Optional[Mapping]
    last_edited_by: Optional[Mapping]


class Parent(TypedDict):
    type: Optional[ParentType]

    database_id: Optional[Union[UUID, str]]
    page_id: Optional[Union[UUID, str]]
    workspace: Optional[bool]
    block_id: Optional[Union[UUID, str]]


class File(TypedDict):
    name: Optional[str]
    type: Optional[FileType]

    external: Optional[Mapping[str, str]]
    file: Optional[Mapping[str, str]]


class Emoji(TypedDict):
    type: Optional[EmojiType]
    emoji: str


class PageDecoration(TypedDict):
    icon: Optional[Emoji]
    cover: Optional[File]


class Block(TypedDict):
    object: Optional[str]
    id: Optional[Union[UUID, str]]

    parent: Optional[Parent]
    type: Optional[BlockType]

    created_time: Optional[str]
    created_by: Optional[str]

    last_edited_time: Optional[str]
    last_edited_by: Optional[str]

    archived: Optional[bool]
    has_children: Optional[bool]
