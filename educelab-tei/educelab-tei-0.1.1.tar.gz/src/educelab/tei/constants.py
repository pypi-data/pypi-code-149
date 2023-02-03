from enum import Enum

NAMESPACES = {
    'tei': 'http://www.tei.com/'  # TODO: this needs to be changed to correspond with tei namespace
}


TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
REQUIRED_FUNCTION = 'generate_tree'


class TEIEnum(Enum):
    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    @classmethod
    def has_value(cls, value: str) -> bool:
        if value in cls._value2member_map_:
            return True
        else:
            return False


class ElementTags(TEIEnum):
    TEI = 'teiHeader'
    FILE_DESC = 'fileDesc'
    PROFILE_DESC = 'profileDesc'
    TITLE_STATEMENT = 'titleStmt'
    TITLE = 'title'
    SOURCE_DESCRIPTION = 'sourceDesc'
    MS_DESC = 'msDesc'
    MS_IDENTIFIER = 'msIdentifier'
    PHYSICAL_DESCRIPTION = 'physDesc'
    HISTORY = 'history'
    ADDITIONAL = 'additional'
    IDNO = 'idno'
    OBJECT_DESC = 'objectDesc'
    SUPPORT_DESC = 'supportDesc'
    SUPPORT = 'support'
    MATERIAL = 'material'
    TEXT_CLASS = 'textClass'
    KEYWORDS = 'keywords'
    TERM = 'term'
    LANG_USAGE = 'langUsage'
    LANGUAGE = 'language'
    LAYOUT_DESC = 'layoutDesc'
    LAYOUT = 'layout'
    P = 'p'
    ADMIN_INFO = 'adminInfo'
    CUSTODIAN_HISTORY = 'custodialHist'
    CUSTODIAN_EVENT = 'custEvent'
    FORENAME = 'forename'
    SURNAME = 'surname'
    GRAPHIC = 'graphic'
    ORIGIN = 'origin'
    ORIGIN_PLACE = 'origPlace'
    ORIGIN_DATE = 'origDate'
    PROVENANCE = 'provenance'
    PLACE_NAME = 'placeName'


class AttributeTags(TEIEnum):
    ID = 'ID'
    TERM_TYPE = 'type'
    IDENT = 'ident'
    IDNO_TYPE = 'type'
    HEIGHT = 'height'
    DIAMETER = 'diameter'
    COLUMNS = 'columns'
    FORM = 'form'
    EVENT_TYPE = 'type'
    FROM = 'from'
    WHEN = 'when'
    TO = 'to'
    URL = 'url'
    NOT_BEFORE = 'notBefore'
    NOT_AFTER = 'notAfter'
    PRECISION = 'precision'
    PROVENANCE_TYPE = 'type'
    PLACE_TYPE = 'type'
    SUBTYPE = 'subtype'
    REF = 'ref'
    CERT = 'cert'
