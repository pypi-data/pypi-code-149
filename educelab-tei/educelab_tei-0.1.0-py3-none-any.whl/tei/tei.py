from __future__ import annotations

from importlib import resources

from lxml import etree

from constants import ElementTags, NAMESPACES
from file_desc import FileDescription
from profile_desc import ProfileDescription
from utils import TEIElement, _check_tag, _add_tei_class
from .exceptions import ParseError


class TEIDocument(TEIElement):

    def __init__(self, file_desc: FileDescription, profile_desc: ProfileDescription):
        self.file_desc = file_desc
        self.profile_desc = profile_desc
        self._namespaces = NAMESPACES['tei']

        return

    @staticmethod
    def tag() -> str:
        return ElementTags.TEI.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(TEIDocument.NAMESPACE, ElementTags.TEI.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname(), nsmap=self._namespaces)

        tree.append(self.file_desc.generate_tree())
        tree.append(self.profile_desc.generate_tree())

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> TEIDocument:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Only TEI element can be parsed.')

        file_desc = None
        profile_desc = None
        for child in tree:
            if child.tag == FileDescription.tag() or child.tag == str(FileDescription.qname()):
                file_desc = FileDescription.from_tree(child)
            elif child.tag == ProfileDescription.tag() or child.tag == str(ProfileDescription.qname()):
                profile_desc = ProfileDescription.from_tree(child)

        tei = TEIDocument(file_desc, profile_desc)

        tei._namespaces = tree.nsmap

        return tei

    @classmethod
    def validation(cls, tree: etree) -> bool:
        xsd_file = resources.files('educelab.tei.schemas') / 'tei_schema.xsd'
        xmlschema = etree.XMLSchema(file=xsd_file)
        if not xmlschema.validate(tree):
            log = xmlschema.error_log
            print('Failed to validate against TEI schema')
            print(log)
            return False
        else:
            return True

    @classmethod
    def from_file(cls, file: str) -> TEIDocument:
        try:
            parser = etree.XMLParser(remove_comments=True, remove_blank_text=True)
            tree = etree.parse(file, parser=parser).getroot()
        except:
            raise OSError('Could not open file ' + str(file))

        if cls.validation(tree):
            mets = cls.from_tree(tree)
            return mets
        else:
            raise ParseError('File does not adhere to the TEI schema')

    def write_to_file(self, file: str) -> None:
        tree = self.generate_tree()
        if TEIDocument.validation(tree):
            try:
                root = etree.ElementTree(tree)
                root.write(file, pretty_print=True, xml_declaration=True, encoding="utf-8")
            except Exception as e:
                raise OSError('Could not write to file ' + str(file) + '/nReason: ' + str(e))
        else:
            print('Error has occured. Generated file does not adhere to TEI schema')

        return

    def generate_string(self) -> str:
        tree = self.generate_tree()
        string = etree.tostring(tree, pretty_print=True).decode('UTF-8')
        return string

    @property
    def file_desc(self) -> FileDescription:
        return self._file_desc

    @file_desc.setter
    def file_desc(self, file_desc: FileDescription) -> None:
        self._file_desc = _add_tei_class(file_desc, FileDescription)
        return

    @property
    def profile_desc(self) -> ProfileDescription:
        return self._profile_desc

    @profile_desc.setter
    def profile_desc(self, profile_desc: ProfileDescription) -> None:
        self._profile_desc = _add_tei_class(profile_desc, ProfileDescription)
        return
