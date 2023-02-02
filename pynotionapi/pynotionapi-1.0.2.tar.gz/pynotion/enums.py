from enum import Enum, auto


class AutoName(Enum):
    @staticmethod
    def _generate_next_value_(name: str, *_) -> str:
        return name.lower()


class BlockType(AutoName):
    PARAGRAPH = auto()
    HEADING_1 = auto()
    HEADING_2 = auto()
    HEADING_3 = auto()
    BULLETED_LIST_ITEM = auto()
    NUMBERED_LIST_ITEM = auto()
    TO_DO = auto()
    TOGGLE = auto()
    CHILD_PAGE = auto()
    CHILD_DATABASE = auto()
    EMBED = auto()
    IMAGE = auto()
    VIDEO = auto()
    FILE = auto()
    PDF = auto()
    BOOKMARK = auto()
    CALLOUT = auto()
    QUOTE = auto()
    EQUATION = auto()
    DIVIDER = auto()
    TABLE_OF_CONTENTS = auto()
    COLUMN = auto()
    COLUMN_LIST = auto()
    LINK_PREVIEW = auto()
    SYNCED_BLOCK = auto()
    TEMPLATE = auto()
    LINK_TO_PAGE = auto()
    TABLE = auto()
    TABLE_ROW = auto()
    UNSUPPORTED = auto()


class DirectionType(AutoName):
    ASCENDING = auto()
    DESCENDING = auto()


class FunctionType(AutoName):
    COUNT_ALL = auto()


class FileType(AutoName):
    FILE = auto()
    EXTERNAL = auto()


class EmojiType(AutoName):
    EMOJI = auto()


class ParentType(AutoName):
    DATABASE_ID = auto()
    PAGE_ID = auto()
    WORKSPACE = auto()
    BLOCK_ID = auto()


class PropertyType(AutoName):
    TITLE = auto()
    RICH_TEXT = auto()
    NUMBER = auto()
    SELECT = auto()
    MULTI_SELECT = auto()
    DATE = auto()
    PEOPLE = auto()
    FILES = auto()
    CHECKBOX = auto()
    URL = auto()
    EMAIL = auto()
    PHONE_NUMBER = auto()
    FORMULA = auto()
    RELATION = auto()
    ROLLUP = auto()
    CREATED_TIME = auto()
    CREATED_BY = auto()
    LAST_EDITED_TIME = auto()
    LAST_EDITED_BY = auto()
    STATUS = auto()


class ResponseType(AutoName):
    BLOCK = auto()
    PAGE = auto()
    USER = auto()
    DATABASE = auto()
    PROPERTY_ITEM = auto()
    PAGE_OR_DATABASE = auto()


class RelationType(AutoName):
    SINGLE_PROPERTY = auto()
    DUAL_PROPERTY = auto()


class RichTextType(AutoName):
    TEXT = auto()
    MENTION = auto()
    EQUATION = auto()


class MentionType(AutoName):
    DATABASE = auto()
    DATE = auto()
    LINK_PREVIEW = auto()
    PAGE = auto()
    TEMPLATE_MENTION = auto()
    USER = auto()


class UserType(AutoName):
    PERSON = auto()
    BOT = auto()
