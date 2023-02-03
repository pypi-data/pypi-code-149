from __future__ import annotations

from typing import Union

from lxml import etree

from .constants import AttributeTags, ElementTags
from .exceptions import ParseError
from .utils import TEIElement, _add_attribute_to_tree, _check_tag, \
    _add_tei_class, _get_string_value, _get_element_list, \
    _get_integer_value


class FileDescription(TEIElement):
    def __init__(self, title_statement: TitleStatement, source_description: SourceDescription) -> None:
        self.title_statement = title_statement
        self.source_description = source_description

        return

    @staticmethod
    def tag() -> str:
        return ElementTags.FILE_DESC.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(FileDescription.NAMESPACE, ElementTags.FILE_DESC.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        tree.append(self.title_statement.generate_tree())
        tree.append(self.source_description.generate_tree())

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> FileDescription:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('File Description Element cant be parsed.')

        title_statement = None
        source_description = None
        for child in tree:
            if child.tag == TitleStatement.tag() or child.tag == str(TitleStatement.qname()):
                title_statement = TitleStatement.from_tree(child)
            elif child.tag == SourceDescription.tag() or child.tag == str(SourceDescription.qname()):
                source_description = SourceDescription.from_tree(child)

        file_desc = FileDescription(title_statement=title_statement, source_description=source_description)

        return file_desc

    @property
    def title_statement(self) -> TitleStatement:
        return self._title_statement

    @title_statement.setter
    def title_statement(self, title_statement: TitleStatement) -> None:
        self._title_statement = _add_tei_class(title_statement, TitleStatement, False)
        return

    @property
    def source_description(self) -> SourceDescription:
        return self._source_description

    @source_description.setter
    def source_description(self, source_description: SourceDescription) -> None:
        self._source_description = _add_tei_class(source_description, SourceDescription, False)
        return


class TitleStatement(TEIElement):
    def __init__(self, titles: Union[Title, list[Title]]) -> None:
        self.titles = titles
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.TITLE_STATEMENT.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(TitleStatement.NAMESPACE, ElementTags.TITLE_STATEMENT.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        for title in self.titles:
            tree.append(title.generate_tree())

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> TitleStatement:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Title Statement Element cant be parsed.')

        titles = []
        for child in tree:
            if child.tag == Title.tag() or child.tag == str(Title.qname()):
                titles.append(Title.from_tree(child))

        title_stmt = TitleStatement(titles=titles)

        return title_stmt

    @property
    def titles(self) -> list[Title]:
        return self._titles

    @titles.setter
    def titles(self, titles: Union[Title, list[Title]]) -> None:
        self._titles = _get_element_list(titles, Title, False)
        return


class Title(TEIElement):
    def __init__(self, title: str) -> None:
        self.title = title
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.TITLE.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(Title.NAMESPACE, ElementTags.TITLE.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        tree.text = self.title

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> Title:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Title element can be parsed.')

        title = Title(tree.text)
        return title

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = _get_string_value(title, False)
        return


class SourceDescription(TEIElement):
    def __init__(self, ms_identifier, physical_description, history, additional) -> None:
        self.ms_identifier = ms_identifier
        self.physical_description = physical_description
        self.history = history
        self.additional = additional

        return

    @staticmethod
    def tag() -> str:
        return ElementTags.SOURCE_DESCRIPTION.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(SourceDescription.NAMESPACE, ElementTags.SOURCE_DESCRIPTION.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())

        sub_tree = etree.Element(etree.QName(SourceDescription.NAMESPACE, ElementTags.MS_DESC.value))

        sub_tree.append(self.ms_identifier.generate_tree())
        sub_tree.append(self.physical_description.generate_tree())
        sub_tree.append(self.history.generate_tree())
        sub_tree.append(self.additional.generate_tree())

        tree.append(sub_tree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> SourceDescription:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Source Description Element cant be parsed.')

        ms_ident = None
        phys_desc = None
        history = None
        additional = None
        for child in tree[0]:
            if child.tag == MsIdentifier.tag() or child.tag == str(MsIdentifier.qname()):
                ms_ident = MsIdentifier.from_tree(child)
            elif child.tag == PhysicalDescription.tag() or child.tag == str(PhysicalDescription.qname()):
                phys_desc = PhysicalDescription.from_tree(child)
            elif child.tag == History.tag() or child.tag == str(History.qname()):
                history = History.from_tree(child)
            elif child.tag == Additional.tag() or child.tag == str(Additional.qname()):
                additional = Additional.from_tree(child)

        source_desc = SourceDescription(ms_identifier=ms_ident, physical_description=phys_desc, history=history,
                                        additional=additional)

        return source_desc

    @property
    def ms_identifier(self) -> TitleStatement:
        return self._ms_identifier

    @ms_identifier.setter
    def ms_identifier(self, ms_identifier: TitleStatement) -> None:
        self._ms_identifier = _add_tei_class(ms_identifier, TitleStatement, False)
        return

    @property
    def physical_description(self) -> TitleStatement:
        return self._physical_description

    @physical_description.setter
    def physical_description(self, physical_description: TitleStatement) -> None:
        self._physical_description = _add_tei_class(physical_description, TitleStatement, False)
        return

    @property
    def history(self) -> TitleStatement:
        return self._history

    @history.setter
    def history(self, history: TitleStatement) -> None:
        self._history = _add_tei_class(history, TitleStatement, False)
        return

    @property
    def additional(self) -> TitleStatement:
        return self._additional

    @additional.setter
    def additional(self, additional: TitleStatement) -> None:
        self._additional = _add_tei_class(additional, TitleStatement, False)
        return


class MsIdentifier(TEIElement):
    def __init__(self, idnos: Union[Idno, list[Idno]]) -> None:
        self.idnos = idnos
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.MS_IDENTIFIER.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(MsIdentifier.NAMESPACE, ElementTags.MS_IDENTIFIER.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        sub_tree = etree.Element(etree.QName(Idno.NAMESPACE, ElementTags.IDNO.value))
        for idno in self.idnos:
            sub_tree.append(idno)

        tree.append(sub_tree)
        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> MsIdentifier:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only MsIdentifier element can be parsed.')

        idnos = []
        for child in tree[0]:
            if child.tag == Idno.tag() or child.tag == str(Idno.qname()):
                idnos.append(Idno.from_tree(child))

        ms_ident = MsIdentifier(idnos=idnos)
        return ms_ident

    @property
    def idnos(self) -> list[Idno]:
        return self._idnos

    @idnos.setter
    def idnos(self, idnos: Union[Idno, list[Idno]]) -> None:
        self._idnos = _get_element_list(idnos, Idno, False)
        return


class Idno(TEIElement):
    def __init__(self, idno_type: str, content: str) -> None:
        self.idno_type = idno_type
        self.content = content
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.IDNO.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(Idno.NAMESPACE, ElementTags.IDNO.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        tree.text = self.content
        _add_attribute_to_tree(tree, AttributeTags.IDNO_TYPE, self.idno_type)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> Idno:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Idno element can be parsed.')

        idno = Idno(idno_type=tree.get(AttributeTags.IDNO_TYPE.value), content=tree.text)
        return idno

    @property
    def idno_type(self) -> str:
        return self._idno_type

    @idno_type.setter
    def idno_type(self, idno_type: str) -> None:
        self._idno_type = _get_string_value(idno_type)
        return

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = _get_string_value(content)
        return


class PhysicalDescription(TEIElement):
    def __init__(self, support_desc: SupportDescription, layout_desc: LayoutDescription, height: int = None,
                 diameter: int = None, columns: int = None, form: str = None) -> None:
        self.support_desc = support_desc
        self.layout_desc = layout_desc
        self.height = height
        self.diameter = diameter
        self.columns = columns
        self.form = form
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.PHYSICAL_DESCRIPTION.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(PhysicalDescription.NAMESPACE, ElementTags.PHYSICAL_DESCRIPTION.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        _add_attribute_to_tree(tree, AttributeTags.HEIGHT, str(self.height))
        _add_attribute_to_tree(tree, AttributeTags.DIAMETER, str(self.diameter))
        _add_attribute_to_tree(tree, AttributeTags.COLUMNS, str(self.columns))

        subtree = etree.Element(etree.QName(PhysicalDescription.NAMESPACE, ElementTags.OBJECT_DESC.value))
        _add_attribute_to_tree(subtree, AttributeTags.FORM, self.form)

        subtree.append(self.support_desc.generate_tree())
        subtree.append(self.layout_desc.generate_tree())

        tree.append(subtree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> PhysicalDescription:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Physical Description element can be parsed.')

        support_desc = None
        layout_desc = None
        for child in tree[0]:
            if child.tag == SupportDescription.tag() or child.tag == str(SupportDescription.qname()):
                support_desc = SupportDescription.from_tree(child)
            elif child.tag == LayoutDescription.tag() or child.tag == str(LayoutDescription.qname()):
                layout_desc = LayoutDescription.from_tree(child)

        phys_desc = PhysicalDescription(support_desc=support_desc, layout_desc=layout_desc,
                                        height=tree.get(AttributeTags.HEIGHT.value),
                                        diameter=tree.get(AttributeTags.DIAMETER.value),
                                        columns=tree.get(AttributeTags.COLUMNS.value),
                                        form=tree[0].get(AttributeTags.FORM.value))

        return phys_desc

    @property
    def support_desc(self) -> SupportDescription:
        return self._support_desc

    @support_desc.setter
    def support_desc(self, support_desc: SupportDescription) -> None:
        self._support_desc = _add_tei_class(support_desc, SupportDescription)
        return

    @property
    def layout_desc(self) -> LayoutDescription:
        return self._layout_desc

    @layout_desc.setter
    def layout_desc(self, layout_desc: LayoutDescription) -> None:
        self._layout_desc = _add_tei_class(layout_desc, LayoutDescription)
        return

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = _get_integer_value(height)
        return

    @property
    def diameter(self) -> int:
        return self._diameter

    @diameter.setter
    def diameter(self, diameter: int) -> None:
        self._diameter = _get_integer_value(diameter)
        return

    @property
    def columns(self) -> int:
        return self._columns

    @columns.setter
    def columns(self, columns: int) -> None:
        self._columns = _get_integer_value(columns)
        return

    @property
    def form(self) -> str:
        return self._form

    @form.setter
    def form(self, form: str) -> None:
        self._form = _get_string_value(form)
        return


class SupportDescription(TEIElement):
    def __init__(self, content: str) -> None:
        self.content = content
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.SUPPORT_DESC.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(SupportDescription.NAMESPACE, ElementTags.SUPPORT_DESC.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        subtree = etree.Element(etree.QName(SupportDescription.NAMESPACE, ElementTags.SUPPORT.value))
        subsubtree = etree.Element(etree.QName(SupportDescription.NAMESPACE, ElementTags.MATERIAL.value))
        subsubtree.text = self.content

        subtree.append(subsubtree)
        tree.append(subtree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> SupportDescription:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Support Description element can be parsed.')

        support_desc = SupportDescription(content=tree[0][0].text)
        return support_desc

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = _get_string_value(content)
        return


class LayoutDescription(TEIElement):
    def __init__(self, content: str) -> None:
        self.content = content
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.SUPPORT_DESC.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(LayoutDescription.NAMESPACE, ElementTags.LAYOUT_DESC.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        subtree = etree.Element(etree.QName(LayoutDescription.NAMESPACE, ElementTags.LAYOUT.value))
        subsubtree = etree.Element(etree.QName(LayoutDescription.NAMESPACE, ElementTags.P.value))
        subsubtree.text = self.content

        subtree.append(subsubtree)
        tree.append(subtree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> LayoutDescription:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Support Description element can be parsed.')

        layout_desc = LayoutDescription(content=tree[0][0].text)
        return layout_desc

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = _get_string_value(content)
        return


class Additional(TEIElement):
    def __init__(self, cust_events: Union[CustodialEvent, list[CustodialEvent]]) -> None:
        self.cust_events = cust_events
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.ADDITIONAL.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(Additional.NAMESPACE, ElementTags.ADDITIONAL.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        subtree = etree.Element(etree.QName(Additional.NAMESPACE, ElementTags.ADMIN_INFO.value))
        subsubtree = etree.Element(etree.QName(Additional.NAMESPACE, ElementTags.CUSTODIAN_HISTORY.value))
        for event in self.cust_events:
            subsubtree.append(event.generate_tree())

        subtree.append(subsubtree)
        tree.append(subtree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> Additional:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Additional element can be parsed.')

        cust_events = []
        for child in tree[0][0]:
            if child.tag == CustodialEvent.tag() or child.tag == str(CustodialEvent.qname()):
                cust_events.append(CustodialEvent.from_tree(child))

        layout_desc = Additional(cust_events=cust_events)
        return layout_desc

    @property
    def cust_events(self) -> list[CustodialEvent]:
        return self._cust_events

    @cust_events.setter
    def cust_events(self, cust_events: Union[CustodialEvent, list[CustodialEvent]]) -> None:
        self._cust_events = _get_element_list(cust_events, CustodialEvent)
        return


class CustodialEvent(TEIElement):
    def __init__(self, forename: str, surname: str, event_type: str, graphic: str = None, when: int = None,
                 time_from: int = None, to: int = None) -> None:
        self.forename = forename
        self.surname = surname
        self.event_type = event_type
        self.graphic = graphic
        self.when = when
        self.time_from = time_from
        self.to = to

        return

    @staticmethod
    def tag() -> str:
        return ElementTags.CUSTODIAN_EVENT.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(CustodialEvent.NAMESPACE, ElementTags.CUSTODIAN_EVENT.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        _add_attribute_to_tree(tree, AttributeTags.EVENT_TYPE, self.event_type)
        _add_attribute_to_tree(tree, AttributeTags.FROM, self.time_from)
        _add_attribute_to_tree(tree, AttributeTags.TO, self.to)
        _add_attribute_to_tree(tree, AttributeTags.WHEN, self.when)

        subtree = etree.Element(etree.QName(CustodialEvent.NAMESPACE, ElementTags.FORENAME.value))
        subtree.text = self.forename
        tree.append(subtree)

        subtree = etree.Element(etree.QName(CustodialEvent.NAMESPACE, ElementTags.SURNAME.value))
        subtree.text = self.surname
        tree.append(subtree)

        subtree = etree.Element(etree.QName(CustodialEvent.NAMESPACE, ElementTags.GRAPHIC.value))
        _add_attribute_to_tree(subtree, AttributeTags.URL, self.to)
        tree.append(subtree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> CustodialEvent:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Custodial Event element can be parsed.')

        forename = None
        surname = None
        graphic = None
        for child in tree:
            if child.tag == ElementTags.FORENAME.value or \
                    child.tag == str(etree.QName(CustodialEvent.NAMESPACE, ElementTags.FORENAME.value)):
                forename = child.text
            elif child.tag == ElementTags.SURNAME.value or \
                    child.tag == str(etree.QName(CustodialEvent.NAMESPACE, ElementTags.SURNAME.value)):
                surname = child.text
            elif child.tag == ElementTags.GRAPHIC.value or \
                    child.tag == str(etree.QName(CustodialEvent.NAMESPACE, ElementTags.GRAPHIC.value)):
                graphic = child.get(AttributeTags.IDNO_TYPE.value)

        cust_event = CustodialEvent(forename=forename, surname=surname,
                                    event_type=tree.get(AttributeTags.IDNO_TYPE.value),
                                    graphic=graphic,
                                    when=tree.get(AttributeTags.WHEN.value),
                                    time_from=tree.get(AttributeTags.FROM.value),
                                    to=tree.get(AttributeTags.TO.value))

        return cust_event

    @property
    def forename(self) -> str:
        return self._forename

    @forename.setter
    def forename(self, forename: str) -> None:
        self._forename = _get_string_value(forename)
        return

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, surname: str) -> None:
        self._surname = _get_string_value(surname)
        return

    @property
    def event_type(self) -> str:
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: str) -> None:
        self._event_type = _get_string_value(event_type)
        return

    @property
    def graphic(self) -> str:
        return self._graphic

    @graphic.setter
    def graphic(self, graphic: str) -> None:
        self._graphic = _get_string_value(graphic)
        return

    @property
    def time_from(self) -> int:
        return self._time_from

    @time_from.setter
    def time_from(self, time_from: int) -> None:
        self._time_from = _get_integer_value(time_from)
        return

    @property
    def when(self) -> int:
        return self._when

    @when.setter
    def when(self, when: int) -> None:
        self._when = _get_integer_value(when)
        return

    @property
    def to(self) -> int:
        return self._to

    @to.setter
    def to(self, to: int) -> None:
        self._to = _get_integer_value(to)
        return


class History(TEIElement):
    def __init__(self, origin: Origin, provenance: Union[Provenance, list[Provenance]]) -> None:
        self.origin = origin
        self.provenance = provenance
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.HISTORY.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(History.NAMESPACE, ElementTags.HISTORY.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        tree.append(self.origin.generate_tree())
        for prov in self.provenance:
            tree.append(prov.generate_tree())

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> History:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only History element can be parsed.')

        origin = None
        provenance = []
        for child in tree:
            if child.tag == Origin.tag() or child.tag == str(Origin.qname()):
                origin = Origin.from_tree(child)
            elif child.tag == Provenance.tag() or child.tag == str(Provenance.qname()):
                provenance.append(Provenance.from_tree(child))

        history = History(origin=origin, provenance=provenance)
        return history

    @property
    def origin(self) -> Origin:
        return self._origin

    @origin.setter
    def origin(self, origin: Origin) -> None:
        self._origin = _get_element_list(origin, Origin)
        return

    @property
    def provenance(self) -> list[Provenance]:
        return self._provenance

    @provenance.setter
    def provenance(self, provenance: Union[Provenance, list[Provenance]]) -> None:
        self._provenance = _get_element_list(provenance, Provenance)
        return


class Origin(TEIElement):
    def __init__(self, place: str, date: str, not_before: int, not_after: int, precision: str) -> None:
        self.place = place
        self.date = date
        self.not_before = not_before
        self.not_after = not_after
        self.precision = precision
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.ORIGIN.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(History.NAMESPACE, ElementTags.ORIGIN.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        subtree = etree.Element(etree.QName(Origin.NAMESPACE, ElementTags.ORIGIN_PLACE.value))
        subtree.text(self.place)
        tree.append(subtree)

        subtree = etree.Element(etree.QName(Origin.NAMESPACE, ElementTags.ORIGIN_DATE.value))
        subtree.text(self.date)
        _add_attribute_to_tree(subtree, AttributeTags.NOT_BEFORE, self.not_before)
        _add_attribute_to_tree(subtree, AttributeTags.NOT_AFTER, self.not_after)
        _add_attribute_to_tree(subtree, AttributeTags.PRECISION, self.precision)
        tree.append(subtree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> Origin:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Origin element can be parsed.')

        place = None
        date = None
        not_before = None
        not_after = None
        precision = None
        for child in tree:
            if child.tag == ElementTags.ORIGIN_PLACE.value or \
                    child.tag == str(etree.QName(Origin.NAMESPACE, ElementTags.ORIGIN_PLACE.value)):
                place = child.text
            elif child.tag == ElementTags.ORIGIN_DATE.value or \
                    child.tag == str(etree.QName(Origin.NAMESPACE, ElementTags.ORIGIN_DATE.value)):
                date = child.text
                not_before = child.get(AttributeTags.NOT_BEFORE.value)
                not_after = child.get(AttributeTags.NOT_AFTER.value)
                precision = child.get(AttributeTags.PRECISION.value)

        history = Origin(place=place, date=date, not_after=not_after, not_before=not_before, precision=precision)
        return history

    @property
    def place(self) -> str:
        return self._place

    @place.setter
    def place(self, place: str) -> None:
        self._place = _get_string_value(place)
        return

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, date: str) -> None:
        self._date = _get_string_value(date)
        return

    @property
    def not_before(self) -> int:
        return self._not_before

    @not_before.setter
    def not_before(self, not_before: int) -> None:
        self._not_before = _get_integer_value(not_before)
        return

    @property
    def not_after(self) -> int:
        return self._not_after

    @not_after.setter
    def not_after(self, not_after: int) -> None:
        self._not_after = _get_integer_value(not_after)
        return

    @property
    def precision(self) -> str:
        return self._precision

    @precision.setter
    def precision(self, precision: str) -> None:
        self._precision = _get_string_value(precision)
        return


class Provenance(TEIElement):
    def __init__(self, provenance_type: str, place_names: Union[PlaceName, list[PlaceName]]) -> None:
        self.provenance_type = provenance_type
        self.place_names = place_names
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.PROVENANCE.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(Provenance.NAMESPACE, ElementTags.PROVENANCE.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        _add_attribute_to_tree(tree, AttributeTags.PROVENANCE_TYPE, self.provenance_type)
        subtree = etree.Element(etree.QName(Provenance.NAMESPACE, ElementTags.P.value))

        for place in self.place_names:
            tree.append(place.generate_tree())

        tree.append(subtree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> Provenance:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Provenance element can be parsed.')

        place_names = []
        for child in tree[0]:
            if child.tag == PlaceName.tag() or child.tag == str(PlaceName.qname()):
                place_names.append(PlaceName.from_tree(child))

        provenance = Provenance(provenance_type=tree.get(AttributeTags.PROVENANCE_TYPE.value),
                                place_names=place_names)
        return provenance

    @property
    def provenance_type(self) -> str:
        return self._provenance_type

    @provenance_type.setter
    def provenance_type(self, provenance_type: str) -> None:
        self._provenance_type = _get_string_value(provenance_type)
        return

    @property
    def place_names(self) -> list[PlaceName]:
        return self._place_names

    @place_names.setter
    def place_names(self, place_names: Union[PlaceName, list[PlaceName]]) -> None:
        self._place_names = _get_element_list(place_names, PlaceName)
        return


class PlaceName(TEIElement):
    def __init__(self, content: str, place_type: str, subtype: str, ref: str, cert: str) -> None:
        self.content = content
        self.place_type = place_type
        self.subtype = subtype
        self.ref = ref
        self.cert = cert

        return

    @staticmethod
    def tag() -> str:
        return ElementTags.PLACE_NAME.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(PlaceName.NAMESPACE, ElementTags.PLACE_NAME.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        _add_attribute_to_tree(tree, AttributeTags.PLACE_TYPE, self.place_type)
        _add_attribute_to_tree(tree, AttributeTags.SUBTYPE, self.subtype)
        _add_attribute_to_tree(tree, AttributeTags.REF, self.ref)
        _add_attribute_to_tree(tree, AttributeTags.CERT, self.cert)
        tree.text = self.content

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> PlaceName:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only Place Name element can be parsed.')

        place_name = PlaceName(content=tree.text,
                               place_type=tree.get(AttributeTags.PLACE_TYPE.value),
                               subtype=tree.get(AttributeTags.SUBTYPE.value),
                               ref=tree.get(AttributeTags.REF.value),
                               cert=tree.get(AttributeTags.CERT.value))
        return place_name

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = _get_string_value(content)
        return

    @property
    def place_type(self) -> str:
        return self._place_type

    @place_type.setter
    def place_type(self, place_type: str) -> None:
        self._place_type = _get_string_value(place_type)
        return

    @property
    def subtype(self) -> str:
        return self._subtype

    @subtype.setter
    def subtype(self, subtype: str) -> None:
        self._subtype = _get_string_value(subtype)
        return

    @property
    def ref(self) -> str:
        return self._ref

    @ref.setter
    def ref(self, ref: str) -> None:
        self._ref = _get_string_value(ref)
        return

    @property
    def cert(self) -> str:
        return self._cert

    @cert.setter
    def cert(self, cert: str) -> None:
        self._cert = _get_string_value(cert)
        return
