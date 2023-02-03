from __future__ import annotations

from typing import Union

from lxml import etree

from .constants import ElementTags, AttributeTags
from .exceptions import ParseError
from .utils import TEIElement, _check_tag, _add_tei_class, _get_element_list, \
    _get_string_value, _add_attribute_to_tree


class ProfileDescription(TEIElement):
    def __init__(self, text_class: TextClass, lang_usage: LangUsage) -> None:

        self.text_class = text_class
        self.lang_usage = lang_usage

        return

    @staticmethod
    def tag() -> str:
        return ElementTags.PROFILE_DESC.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(ProfileDescription.NAMESPACE, ElementTags.PROFILE_DESC.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())

        tree.append(self.text_class.generate_tree())
        tree.append(self.lang_usage.generate_tree())

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> ProfileDescription:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Profile Description Element cant be parsed.')

        text_class = None
        lang_usage = None
        for child in tree:
            if child.tag == TextClass.tag() or child.tag == str(TextClass.qname()):
                text_class = TextClass.from_tree(child)
            elif child.tag == LangUsage.tag() or child.tag == str(LangUsage.qname()):
                lang_usage = LangUsage.from_tree(child)

        struct_map = ProfileDescription(text_class=text_class, lang_usage=lang_usage)

        return struct_map

    @property
    def text_class(self) -> TextClass:
        return self._text_class

    @text_class.setter
    def text_class(self, text_class: TextClass) -> None:
        self._text_class = _add_tei_class(text_class, TextClass, False)
        return

    @property
    def lang_usage(self) -> LangUsage:
        return self._lang_usage

    @lang_usage.setter
    def lang_usage(self, lang_usage: LangUsage) -> None:
        self._lang_usage = _add_tei_class(lang_usage, LangUsage, False)
        return


class TextClass(TEIElement):
    def __init__(self, terms: Union[Term, list[Term]]) -> None:
        self.terms = terms

        return

    @staticmethod
    def tag() -> str:
        return ElementTags.TEXT_CLASS.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(TextClass.NAMESPACE, ElementTags.TEXT_CLASS.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        sub_tree = etree.Element(etree.QName(TextClass.NAMESPACE, ElementTags.KEYWORDS.value))
        for item in self.terms:
            sub_tree.append(item.generate_tree())

        tree.append(sub_tree)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> TextClass:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Text Class Element cant be parsed.')

        terms = []
        for child in tree[0]:
            if child.tag == Term.tag() or child.tag == str(Term.qname()):
                terms.append(Term.from_tree(child))

        text_class = TextClass(terms=terms)

        return text_class

    @property
    def terms(self) -> list[Term]:
        return self._terms

    @terms.setter
    def terms(self, terms: Union[Term, list[Term]]) -> None:
        self._terms = _get_element_list(terms, Term, False)
        return


class Term(TEIElement):
    def __init__(self, term: str, term_type: str = None) -> None:
        self.term = term
        self.term_type = term_type
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.TERM.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(Term.NAMESPACE, ElementTags.TERM.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())

        tree.text = self.term
        _add_attribute_to_tree(tree, AttributeTags.TERM_TYPE, self.term_type)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> Term:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Term Element cant be parsed.')

        term = Term(term=tree.text, term_type=tree.get(AttributeTags.TERM_TYPE.value))

        return term

    @property
    def term(self) -> str:
        return self._term

    @term.setter
    def term(self, term: str) -> None:
        self._term = _get_string_value(term, False)
        return

    @property
    def term_type(self) -> str:
        return self._term_type

    @term_type.setter
    def term_type(self, term_type: str) -> None:
        self._term_type = _get_string_value(term_type, False)
        return


class LangUsage(TEIElement):
    def __init__(self, languages: Union[Language, list[Language]]) -> None:
        self.languages = languages
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.LANG_USAGE.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(LangUsage.NAMESPACE, ElementTags.LANG_USAGE.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())

        for item in self.languages:
            tree.append(item.generate_tree())

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> LangUsage:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Language Usage Element cant be parsed.')

        languages = []
        for child in tree:
            if child.tag == Language.tag() or child.tag == str(Language.qname()):
                languages.append(Language.from_tree(child))

        lang_use = LangUsage(languages=languages)

        return lang_use

    @property
    def languages(self) -> list[Language]:
        return self._languages

    @languages.setter
    def languages(self, languages: Union[Language, list[Language]]) -> None:
        self._languages = _get_element_list(languages, Language, False)
        return


class Language(TEIElement):
    def __init__(self, language: str, ident: str) -> None:
        self.language = language
        self.ident = ident
        return

    @staticmethod
    def tag() -> str:
        return ElementTags.LANGUAGE.value

    @staticmethod
    def qname() -> etree.QName:
        return etree.QName(Language.NAMESPACE, ElementTags.LANGUAGE.value)

    def generate_tree(self) -> etree:
        tree = etree.Element(self.qname())
        tree.text(self.language)
        _add_attribute_to_tree(tree, AttributeTags.IDENT, self.ident)

        return tree

    @classmethod
    def from_tree(cls, tree: etree) -> Language:
        if not _check_tag(tree.tag, cls.tag()):
            raise ParseError('Language Element cant be parsed.')

        language = Language(language=tree.text, ident=tree.get(AttributeTags.IDENT.value))

        return language

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        self._language = _get_string_value(language, False)
        return

    @property
    def ident(self) -> str:
        return self._ident

    @ident.setter
    def ident(self, ident: str) -> None:
        self._ident = _get_string_value(ident, False)
        return
